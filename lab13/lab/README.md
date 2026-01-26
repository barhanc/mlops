## Introduction

The excersises were done on a PC with GTX 1660 GPU with 6GB of VRAM thus I used
the smaller 0.6B model and added a `--gpu_memory_utilization 0.8` flag.

## Ex.1.

* inference time and KV cache size without dynamic quantization

![alt text](figs/01_kv_orig.png)
![alt text](figs/01_infer_time_orig.png)

* inference time and KV cache size with dynamic quantization

![alt text](figs/01_kv_quant.png)
![alt text](figs/01_infer_time_quant.png)

## Ex.2.

![alt text](figs/02_llm_response.png)

## Ex.3.

![alt text](figs/03_llm_mcp_response.png)

## Ex.4.

![alt text](figs/04_llm_mcp_response.png)

![alt text](figs/image.png)

## Ex.5.

For some reason the `RestrictToTopic` guardrail returns some api key error.

![alt text](figs/05_llm_guardrails_response.png)