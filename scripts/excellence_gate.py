#!/usr/bin/env python3
"""Offline evidence gate for Starlight mission receipts. No cloud/model calls."""
import argparse
import json
from pathlib import Path

ROLES={"astra","sol","terra","verity","atlas","muse","mercury"}
STATES=["proposed","implemented","tested","merged","deployed","operating","customer-validated"]
WEIGHTS={"reasoning":15,"originality":15,"craft":20,"correctness":20,"completeness":15,"evidence":15}
REQUIRED=["id","objective","role","owner","source_revision","authorized_effects","artifacts","acceptance","status"]

def validate(data):
    errors=[f"missing:{k}" for k in REQUIRED if not data.get(k)]
    if data.get("role") not in ROLES: errors.append("invalid:role")
    state=data.get("status")
    if state not in STATES: errors.append("invalid:status")
    if not isinstance(data.get("authorized_effects"),list):errors.append("invalid:authorized_effects")
    if not isinstance(data.get("artifacts"),list):errors.append("invalid:artifacts")
    acceptance=data.get("acceptance")
    if not isinstance(acceptance,dict) or not acceptance:errors.append("invalid:acceptance")
    elif any(type(v)!=bool for v in acceptance.values()):errors.append("invalid:acceptance-values")
    elif state in STATES[2:] and not all(acceptance.values()):errors.append("failed:acceptance")
    if state in STATES[2:] and not data.get("verification_receipts"):errors.append("missing:verification_receipts")
    if state in STATES[3:] and not data.get("reviewer"):errors.append("missing:independent_reviewer")
    if state in STATES[4:] and not data.get("deployment_receipt"):errors.append("missing:deployment_receipt")
    score=None
    scores=data.get("scores")
    if scores is not None:
        if not isinstance(scores,dict) or set(scores)!=set(WEIGHTS) or any(type(scores[k]) not in (int,float) or not 0<=scores[k]<=10 for k in WEIGHTS):
            errors.append("invalid:scores")
        else:
            score=round(sum(scores[k]*w/10 for k,w in WEIGHTS.items()),2)
            if state in STATES[2:] and (score<90 or any(v<8 for v in scores.values())):errors.append("failed:quality-threshold")
    return {"pass":not errors,"errors":errors,"score":score,"status":state}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("receipt",type=Path)
    a=p.parse_args()
    try: result=validate(json.loads(a.receipt.read_text(encoding="utf-8")))
    except (OSError,ValueError) as e:result={"pass":False,"errors":[f"cannot-read:{e}"]}
    print(json.dumps(result,sort_keys=True))
    raise SystemExit(0 if result["pass"] else 1)
