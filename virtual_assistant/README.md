### 简单介绍

大模型处理基于langchain，方便使用langchain自带的工具包，例如对多种本地大模型的支持，方便后续开发，语音识别使用openai的whisper可依自行根据需求选择不同大小语言的模型，支持实时识别，语音合成默认使用开源的edge_tts，也可以使用MockingBird。

### 环境准备

只是安装语音助手部分的包

pip install -r requirements.txt

使用本地大模型参考langchain文档对大模型的支持，默认chatglm前往https://github.com/THUDM/ChatGLM2-6B安装相应环境，并启动api服务即可，同理使用chatgpt的api也需自行配置key，参考openai文档

### 启动

##### 1.本地语音助手

python main.py

其他功能都在main.py里

gui功能还在开发中，想与Open Interpreter项目结合

##### 2.nerf训练虚拟形象

基于https://github.com/ashawkey/RAD-NeRF二次开发

进入该项目安装环境，然后在main.py里修改相应代码即可

