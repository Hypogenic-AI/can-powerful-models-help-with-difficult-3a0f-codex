"""Run real downloadable instruction models locally on GPU with batched inference."""
from __future__ import annotations
import argparse, hashlib, json, re, time
from datetime import datetime, timezone
from pathlib import Path
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from run_experiment import SYSTEM, prompt, parse

ROOT=Path(__file__).resolve().parents[1]
DEFAULT=["Qwen/Qwen3-4B","Qwen/Qwen3-8B","Qwen/Qwen3-14B"]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--models',nargs='*',default=DEFAULT); ap.add_argument('--output',default='results/raw_outputs.json'); ap.add_argument('--batch-size',type=int,default=16); ap.add_argument('--device',default='cuda:0')
    a=ap.parse_args(); cases=json.loads((ROOT/'datasets/research_agent_audit.json').read_text()); all_results=[]; out_path=ROOT/a.output
    assert torch.cuda.is_available(), 'CUDA required for planned local run'
    for model_id in a.models:
        print('loading',model_id,flush=True); start_model=time.perf_counter()
        tok=AutoTokenizer.from_pretrained(model_id,padding_side='left')
        if tok.pad_token_id is None: tok.pad_token_id=tok.eos_token_id
        model=AutoModelForCausalLM.from_pretrained(model_id,torch_dtype=torch.bfloat16,device_map=a.device,low_cpu_mem_usage=True).eval()
        jobs=[(c,p) for c in cases for p in SYSTEM]
        for pos in range(0,len(jobs),a.batch_size):
            batch=jobs[pos:pos+a.batch_size]; texts=[]
            for c,protocol in batch:
                msgs=[{"role":"system","content":SYSTEM[protocol]},{"role":"user","content":prompt(c)}]
                texts.append(tok.apply_chat_template(msgs,tokenize=False,add_generation_prompt=True,enable_thinking=False))
            enc=tok(texts,return_tensors='pt',padding=True).to(a.device); t=time.perf_counter()
            with torch.inference_mode():
                out=model.generate(**enc,max_new_tokens=180,do_sample=False,pad_token_id=tok.pad_token_id)
            latency=(time.perf_counter()-t)/len(batch); input_lens=enc.attention_mask.sum(1).tolist()
            for j,((c,protocol),seq,inlen) in enumerate(zip(batch,out,input_lens)):
                generated=seq[enc.input_ids.shape[1]:]; raw=tok.decode(generated,skip_special_tokens=True).strip()
                all_results.append({"case_id":c['id'],"model":model_id,"returned_model":model_id,"protocol":protocol,"timestamp":datetime.now(timezone.utc).isoformat(),"latency_s":latency,"error":None,"raw":raw,"parsed":parse(raw),"usage":{"prompt_tokens":int(inlen),"completion_tokens":int(len(generated)),"total_tokens":int(inlen+len(generated))}})
            print(model_id,min(pos+len(batch),len(jobs)),'/',len(jobs),flush=True)
        print('finished',model_id,'seconds',round(time.perf_counter()-start_model,1),flush=True)
        # Checkpoint after every model so a later download/runtime failure cannot
        # erase already completed real-model trials.
        checkpoint={"endpoint":"local Hugging Face inference","requested_models":a.models,"temperature":0,"max_tokens":180,"dtype":"bfloat16","device":a.device,
                    "prompts_sha256":hashlib.sha256(json.dumps(SYSTEM,sort_keys=True).encode()).hexdigest(),"results":sorted(all_results,key=lambda x:(x['case_id'],x['model'],x['protocol']))}
        out_path.parent.mkdir(parents=True,exist_ok=True); out_path.write_text(json.dumps(checkpoint,indent=2)+'\n')
        del model; torch.cuda.empty_cache()
    payload={"endpoint":"local Hugging Face inference","requested_models":a.models,"temperature":0,"max_tokens":180,"dtype":"bfloat16","device":a.device,
             "prompts_sha256":hashlib.sha256(json.dumps(SYSTEM,sort_keys=True).encode()).hexdigest(),"results":sorted(all_results,key=lambda x:(x['case_id'],x['model'],x['protocol']))}
    out_path.parent.mkdir(parents=True,exist_ok=True); out_path.write_text(json.dumps(payload,indent=2)+'\n')
    print('wrote',out_path,len(all_results),'parse failures',sum(x['parsed'] is None for x in all_results))

if __name__=='__main__': main()
