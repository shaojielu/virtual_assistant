import gradio as gr
from main import xiaoyan



def textTalk(question):
    return xiaoyan.thinking(question)

demo = gr.Interface(fn=textTalk, inputs="text", outputs="text")
demo.launch()   