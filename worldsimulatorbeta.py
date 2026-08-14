#!/usr/bin/env python3
"""WORLD SIMULATOR BETA — external NEWS-GEAR + CHARACTER-GEAR -> actual Python path."""

import argparse, copy, hashlib, json, random
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

EMOTIONS = ["fear","anger","sympathy","greed","curiosity"]
ACTIONS = ["confront","withdraw","support","exploit","investigate"]

EMOTION_ACTIONS = {
    "fear":["withdraw","investigate"], "anger":["confront","exploit"],
    "sympathy":["support","investigate"], "greed":["exploit","confront"],
    "curiosity":["investigate","support"], "calm":["investigate","support"]
}

# Executable fallback preserved from the prior Python dry-runs.
# If the supplied CHARACTER-GEAR contains action_rules/actions+social_effects,
# those supplied rules take precedence.
DEFAULT_RULES = {
    "confront":{"target":{"fear":.25,"anger":.35},"actor":{"anger":-.10}},
    "withdraw":{"target":{"sympathy":.10,"curiosity":.15},"actor":{"fear":-.20,"anger":-.15}},
    "support":{"target":{"sympathy":.30,"fear":-.20},"actor":{"sympathy":.10}},
    "exploit":{"target":{"fear":.20,"anger":.30,"sympathy":-.20},"actor":{"greed":.25}},
    "investigate":{"target":{"curiosity":.20},"actor":{"curiosity":.15,"fear":-.10}},
}

def num(x, default=0.0):
    try: return float(x)
    except (TypeError,ValueError): return default

def clamp(x): return max(0.0, min(1.0, float(x)))

def load(path):
    p=Path(path)
    if not p.exists(): raise ValueError(f"INPUT FILE NOT FOUND: {p}")
    try: return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e: raise ValueError(f"INVALID JSON: {p}: {e}")

def dict_first(*xs):
    for x in xs:
        if isinstance(x,dict): return x
    return {}

@dataclass
class Gear:
    name:str
    sensitivity:dict
    bias:dict=field(default_factory=dict)
    affinity:dict=field(default_factory=dict)
    resilience:float=.5
    raw:dict=field(default_factory=dict)

@dataclass
class News:
    name:str
    impacts:dict
    raw:dict=field(default_factory=dict)

@dataclass
class State:
    name:str
    emotions:dict=field(default_factory=dict)
    activation:float=0.0
    interactions:int=0
    last_action:str|None=None
    last_target:str|None=None

    def get(self,e): return num(self.emotions.get(e,0))
    def intensity(self): return sum(abs(num(v)) for v in self.emotions.values())
    def dominant(self):
        return max(self.emotions.items(),key=lambda x:(num(x[1]),x[0])) if self.emotions else ("calm",0)
    def snap(self):
        d,v=self.dominant()
        return {"dominant":d,"dominant_value":round(v,4),
                "activation":round(self.activation,4),
                "intensity":round(self.intensity(),4),
                "emotions":{k:round(num(v),4) for k,v in sorted(
                    self.emotions.items(),key=lambda x:(-num(x[1]),x[0])) if abs(num(v))>.0001}}

def normalize_news(data):
    if isinstance(data,dict) and isinstance(data.get("news_gear"),dict): data=data["news_gear"]
    if not isinstance(data,dict): raise ValueError("NEWS-GEAR must be an object")
    impacts=dict_first(data.get("impacts"),data.get("emotion_impacts"),data.get("emotion_delta"),data.get("effects"))
    if not impacts: raise ValueError("NEWS-GEAR has no impacts/emotion_impacts")
    return News(str(data.get("name") or data.get("event_name") or data.get("event_id") or "unnamed_news"),
                {str(k):num(v) for k,v in impacts.items()},data)

def character_items(data):
    if isinstance(data,list): return [x for x in data if isinstance(x,dict)]
    if not isinstance(data,dict): return []
    for key in ("characters","character_pool","demo_characters","character_gear"):
        v=data.get(key)
        if isinstance(v,list): return [x for x in v if isinstance(x,dict)]
        if isinstance(v,dict):
            return [dict(x,character_id=k) for k,x in v.items() if isinstance(x,dict)]
    return []

def normalize_chars(data):
    items=character_items(data)
    if len(items)<2: raise ValueError("CHARACTER-GEAR needs at least 2 characters")
    out=[]
    for i,x in enumerate(items):
        name=str(x.get("name") or x.get("character_id") or x.get("id") or f"CHAR_{i+1}")
        profile=dict_first(x.get("emotion_profile"),x.get("sensitivity"),
                           x.get("emotion_sensitivity"),x.get("07_EMOTION_PROFILE_sensitivity"))
        sens={}
        for e,v in profile.items():
            sens[str(e)]=num(v.get("sensitivity",v.get("weight",v.get("value",0))) if isinstance(v,dict) else v)
        if not sens: raise ValueError(f"{name}: missing emotion sensitivity/profile")
        bias={str(k):num(v) for k,v in dict_first(x.get("bias"),x.get("behavior_bias"),x.get("08_BEHAVIOR_BIAS")).items()}
        aff={str(k):num(v) for k,v in dict_first(x.get("action_affinity"),x.get("31_ACTION_AFFINITY")).items()}
        out.append(Gear(name,sens,bias,aff,num(x.get("resilience",.5)),x))
    names=[x.name for x in out]
    if len(names)!=len(set(names)): raise ValueError(f"Duplicate character names: {names}")
    return out

def action_rules(news_data,char_data):
    for root in (char_data,news_data):
        if not isinstance(root,dict): continue
        r=root.get("action_rules")
        if isinstance(r,dict): return r
        actions=root.get("actions"); effects=root.get("social_effects")
        if isinstance(actions,dict) and isinstance(effects,dict):
            result={}
            for a,d in actions.items():
                if not isinstance(d,dict): continue
                eff=effects.get(d.get("social_effect_id"),{})
                target=eff.get("target_emotion_distribution",{}) if isinstance(eff,dict) else {}
                if isinstance(target,dict):
                    result[a]={"actor":{},"target":{k:num(v) for k,v in target.items()}}
            if result:return result
    return copy.deepcopy(DEFAULT_RULES)

class Engine:
    def __init__(self,seed,rules,pair_noise=.22,action_noise=.18,top_k=3):
        self.rng=random.Random(seed); self.rules=rules
        self.pair_noise=pair_noise; self.action_noise=action_noise; self.top_k=max(1,top_k)
        self.last_pair={}; self.trace=[]

    def apply_news(self,news,states,gears):
        result={}
        for s in states:
            d={}; act=0
            for e,m in news.impacts.items():
                raw=m*gears[s.name].sensitivity.get(e,0)
                old=s.get(e); new=clamp(old+raw); s.emotions[e]=new
                if abs(new-old)>1e-9:d[e]=round(new-old,6)
                act+=abs(raw)*.55
            old=s.activation;s.activation=clamp(s.activation+act)
            result[s.name]={"emotions":d,"activation":round(s.activation-old,6)}
        return result

    def pair_score(self,a,b,step,emotions):
        contrast=sum(abs(a.get(e)-b.get(e)) for e in emotions)/max(1,len(emotions))
        intensity=(a.intensity()+b.intensity())/2
        activation=(a.activation+b.activation)/2
        key=tuple(sorted((a.name,b.name))); since=step-self.last_pair.get(key,-999)
        fresh=1 if since>=4 else max(0,since/4)
        penalty=.55 if since<=1 else 0
        load=.03*(a.interactions+b.interactions)
        base=max(.01,contrast+intensity*.85+activation*1.8+fresh*.25-penalty-load)
        noise=self.rng.random()*self.pair_noise if self.pair_noise else 0
        return {"pair":[a.name,b.name],"base":round(base,6),"noise":round(noise,6),
                "final":round(base+noise,6)}

    def choose_pair(self,states,step,emotions):
        c=[self.pair_score(states[i],states[j],step,emotions)
           for i in range(len(states)) for j in range(i+1,len(states))]
        if not c:return None
        c.sort(key=lambda x:x["final"],reverse=True); top=c[:min(self.top_k,len(c))]
        chosen=top[0] if len(top)==1 else self.rng.choices(top,weights=[x["final"] for x in top],k=1)[0]
        sm={s.name:s for s in states}; a,b=sm[chosen["pair"][0]],sm[chosen["pair"][1]]
        da=a.activation*1.25+a.intensity(); db=b.activation*1.25+b.intensity()
        actor,target=(b,a) if db>da else (a,b)
        self.last_pair[tuple(sorted((actor.name,target.name)))]=step
        actor.interactions+=1;target.interactions+=1
        return actor,target,{"candidates":c[:5],"chosen":chosen,"top_k":len(top)}

    def score_action(self,actor,target,gear):
        dom,val=actor.dominant(); scores={}
        names=set(ACTIONS)|set(gear.bias)|set(gear.affinity)|set(self.rules)
        for a in names:scores[a]=gear.bias.get(a,0)*.65+gear.affinity.get(a,0)*.5
        for a in EMOTION_ACTIONS.get(dom,[]):scores[a]=scores.get(a,0)+val*.95
        scores["withdraw"]=scores.get("withdraw",0)+actor.get("fear")*.85
        scores["confront"]=scores.get("confront",0)+actor.get("anger")*.85
        scores["support"]=scores.get("support",0)+actor.get("sympathy")*.75
        scores["exploit"]=scores.get("exploit",0)+actor.get("greed")*.85
        scores["investigate"]=scores.get("investigate",0)+actor.get("curiosity")*.75
        if target.get("fear")>.45:
            scores["exploit"]=scores.get("exploit",0)+.25;scores["confront"]=scores.get("confront",0)+.15
        if target.get("anger")>.45:
            scores["withdraw"]=scores.get("withdraw",0)+.25;scores["support"]=scores.get("support",0)+.2
        return {k:max(0,float(v)) for k,v in scores.items()},dom

    def choose_action(self,actor,target,gear):
        base,dom=self.score_action(actor,target,gear)
        noise={a:self.rng.random()*self.action_noise for a in base}
        final={a:max(.01,base[a]+noise[a]) for a in base}
        chosen=max(final,key=final.get) if self.action_noise<=0 else self.rng.choices(list(final),weights=list(final.values()),k=1)[0]
        return chosen,{"dominant_emotion":dom,"base":base,"noise":noise,"final":final,"chosen":chosen}

    def apply_action(self,actor,target,action,ag,tg):
        rule=self.rules.get(action,{})
        result={actor.name:{"emotions":{}},target.name:{"emotions":{}}}
        for s,g,side in ((actor,ag,"actor"),(target,tg,"target")):
            for e,m in rule.get(side,{}).items():
                raw=num(m)*g.sensitivity.get(e,.5);old=s.get(e);new=clamp(old+raw);s.emotions[e]=new
                if abs(new-old)>1e-9:result[s.name]["emotions"][e]=round(new-old,6)
        return result

    def decay(self,states,gears):
        changed=[]
        for s in states:
            amount=gears[s.name].resilience*.03
            for e in list(s.emotions):s.emotions[e]=max(0,s.emotions[e]-amount)
            old=s.activation;s.activation=max(0,s.activation-.08)
            if old!=s.activation or amount:changed.append(s.name)
        return changed

    def run(self,news,gears,steps,emotions):
        states=[State(g.name) for g in gears]; gm={g.name:g for g in gears}
        before={s.name:s.snap() for s in states}; d=self.apply_news(news,states,gm)
        self.trace.append({"step":0,"event_type":"news","news_name":news.name,"states_before":before,
                           "deltas":d,"states_after":{s.name:s.snap() for s in states}})
        for step in range(1,steps+1):
            picked=self.choose_pair(states,step,emotions)
            if not picked:
                self.trace.append({"step":step,"event_type":"stop","reason":"NO_VALID_INTERACTION_PAIR"});break
            actor,target,pair= picked
            before={s.name:s.snap() for s in states}
            action,ameta=self.choose_action(actor,target,gm[actor.name])
            actor.last_action=action;actor.last_target=target.name
            delta=self.apply_action(actor,target,action,gm[actor.name],gm[target.name])
            decay=self.decay(states,gm)
            self.trace.append({"step":step,"event_type":"interaction","actor":actor.name,"target":target.name,
                               "action":action,"states_before":before,"pair_selection":pair,
                               "action_selection":ameta,"deltas":delta,"decay_applied_to":decay,
                               "states_after":{s.name:s.snap() for s in states}})
        return states

def metrics(trace):
    r=[x for x in trace if x.get("event_type")=="interaction"]
    pairs=[tuple(sorted((x["actor"],x["target"]))) for x in r]
    directed=[(x["actor"],x["target"]) for x in r]
    longest=current=1 if r else 0
    for i in range(1,len(r)): current=current+1 if r[i]["actor"]==r[i-1]["target"] else 1;longest=max(longest,current)
    return {"interaction_steps":len(r),"unique_pairs":len(set(pairs)),
            "immediate_pair_repeats":sum(pairs[i]==pairs[i-1] for i in range(1,len(pairs))),
            "directed_reversals":sum(directed[i]==(directed[i-1][1],directed[i-1][0]) for i in range(1,len(directed))),
            "longest_reactive_chain":longest,"actions":dict(Counter(x["action"] for x in r))}

def canonical(trace,states): return {"trace":trace,"final_states":{s.name:s.snap() for s in states}}

def run(news_path,char_path,seed,steps,pair_noise,action_noise,top_k,out):
    nd=load(news_path);cd=load(char_path);news=normalize_news(nd);gears=normalize_chars(cd)
    emotions=sorted(set(EMOTIONS)|set(news.impacts)|{e for g in gears for e in g.sensitivity})
    eng=Engine(seed,action_rules(nd,cd),pair_noise,action_noise,top_k);states=eng.run(news,gears,steps,emotions)
    result=canonical(eng.trace,states)
    result["run"]={"seed":seed,"steps_requested":steps,"characters":len(gears),"news_name":news.name,
                   "metrics":metrics(eng.trace),
                   "input_sha256":{"news":hashlib.sha256(Path(news_path).read_bytes()).hexdigest(),
                                   "character":hashlib.sha256(Path(char_path).read_bytes()).hexdigest()}}
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(result["run"],ensure_ascii=False,indent=2))
    print("\nACTUAL PATH")
    for x in eng.trace:
        if x["event_type"]=="interaction":print(f'STEP {x["step"]:02d}: {x["actor"]} -> {x["target"]} [{x["action"]}]')
    print(f"\nTRACE JSON: {out}")

def selftest():
    gears=[
      Gear("A",{"fear":.9,"anger":.2,"sympathy":.6,"greed":.3,"curiosity":.5},{"withdraw":.65,"support":.35,"investigate":.4}),
      Gear("B",{"fear":.2,"anger":.9,"sympathy":.3,"greed":.5,"curiosity":.4},{"confront":.7,"exploit":.4}),
      Gear("C",{"fear":.4,"anger":.3,"sympathy":.9,"greed":.2,"curiosity":.7},{"support":.7,"investigate":.5}),
      Gear("D",{"fear":.3,"anger":.4,"sympathy":.2,"greed":.9,"curiosity":.6},{"exploit":.8}),
      Gear("E",{"fear":.5,"anger":.3,"sympathy":.5,"greed":.4,"curiosity":.9},{"investigate":.7})
    ]
    news=News("TEST",{"fear":.65,"curiosity":.25})
    def run(seed):
        e=Engine(seed,DEFAULT_RULES);s=e.run(news,gears,35,EMOTIONS);return canonical(e.trace,s)
    a,b,c=run(42),run(42),run(7)
    fear=[v["emotions"].get("fear",0) for v in a["trace"][0]["deltas"].values()]
    assert len(set(fear))>=4
    assert a==b
    assert a!=c
    assert any(x.get("event_type")=="interaction" for x in a["trace"])
    print("SELFTEST PASS: same-news differentiation, interaction, determinism, variance")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--news-gear");p.add_argument("--character-gear")
    p.add_argument("--seed",type=int,default=42);p.add_argument("--steps",type=int,default=35)
    p.add_argument("--pair-noise",type=float,default=.22);p.add_argument("--action-noise",type=float,default=.18)
    p.add_argument("--top-k",type=int,default=3);p.add_argument("--output-json",default="world_simulator_beta_trace.json")
    p.add_argument("--selftest",action="store_true");a=p.parse_args()
    if a.selftest:selftest()
    elif not a.news_gear or not a.character_gear:p.error("--news-gear and --character-gear are required")
    else:run(a.news_gear,a.character_gear,a.seed,a.steps,a.pair_noise,a.action_noise,a.top_k,Path(a.output_json))
