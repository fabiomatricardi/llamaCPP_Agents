# llamaCPP_Agents
Run AI agents with llama-cpp-agents locally

source here: https://llama-cpp-agent.readthedocs.io/en/latest/sequential_chain/

<img src='https://github.com/fabiomatricardi/llamaCPP_Agents/raw/main/logo.png' height=300>

## Install dependencies
```
pip install llama-cpp-agent rich
```

Download llamafile in the same directory

from the terminal in the same directory run
```
wget https://github.com/Mozilla-Ocho/llamafile/releases/download/0.8.6/llamafile-0.8.6 -OutFile llamafile-0.8.6.exe
```

## Download a good Small Language Model
- qwen2-0_5b-instruct-q8_0.gguf         nctx=32k
- h2o-danube2-1.8b-chat-Q5_K_M.gguf     nctx=8k
- stablelm-2-zephyr-1_6b-Q5_K_M.gguf    nctx= 2k
- qwen2-1.5b-instruct.Q6_K.gguf         nctx=32k
- gemma-1.1-2b-it.Q6_K.gguf             nctx= 2k

```
wget https://huggingface.co/Qwen/Qwen1.5-1.8B-Chat-GGUF/resolve/main/qwen1_5-1_8b-chat-q4_k_m.gguf -OutFile qwen1_5-1_8b-chat-q4_k_m.gguf
wget https://huggingface.co/Qwen/Qwen2-0.5B-Instruct-GGUF/resolve/main/qwen2-0_5b-instruct-q8_0.gguf -OutFile qwen2-0_5b-instruct-q8_0.gguf
wget https://huggingface.co/Clausss/Qwen2-1.5B-Instruct-Q8_0-GGUF/resolve/main/qwen2-1.5b-instruct-q8_0.gguf -OutFile qwen2-1.5b-instruct-q8_0.gguf
wget https://huggingface.co/ggml-org/gemma-1.1-2b-it-Q6_K-GGUF/resolve/main/gemma-1.1-2b-it.Q6_K.gguf -OutFile gemma-1.1-2b-it.Q6_K.gguf
wget https://huggingface.co/h2oai/h2o-danube2-1.8b-chat-GGUF/resolve/main/h2o-danube2-1.8b-chat-Q5_K_M.gguf -OutFile h2o-danube2-1.8b-chat-Q5_K_M.gguf
wget https://huggingface.co/second-state/stablelm-2-zephyr-1.6b-GGUF/resolve/main/stablelm-2-zephyr-1_6b-Q5_K_M.gguf -OutFile stablelm-2-zephyr-1_6b-Q5_K_M.gguf
```

## Run llamaCPP-OpenAI endpoint with llamafile
```
.\llamafile-0.8.exe -m model/qwen2-0_5b-instruct-q8_0.gguf --host 0.0.0.0 -c 8192
```
This will run your endpoint also in your network
```
llama server listening at http://172.18.3.198:8080
llama server listening at http://127.0.0.1:8080
llama server listening at http://192.168.2.6:8080
```

## Run the python file
```
.\python.exe .\productlaunch.py
```


# Bind a langchain openAI compatible call
references:
- https://python.langchain.com/v0.2/docs/integrations/chat/openai/
- https://python.langchain.com/v0.2/docs/integrations/chat/llamacpp/

Using llamafile with qwen
```
.\llamafile-0.8.6.exe -m qwen1_5-0_5b-chat-q8_0.gguf --host 0.0.0.0 -c 8192
```

In another terminal run
```
.\python3117pipReady\python.exe .\testapi.py
```



