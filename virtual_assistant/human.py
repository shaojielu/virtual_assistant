from langchain.chains import LLMChain
from langchain.llms import ChatGLM
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from interpreter import interpreter
# from vocoder.hifigan import inference as gan_vocoder
# from synthesizer.inference import Synthesizer
# from encoder import inference as encoder
import speech_recognition as sr
import whisper
import asyncio
import edge_tts
import time

#加载语音识别模型
model = whisper.load_model("tiny")

class Humans:
    def __init__(self,soul,brain):
        self.name = 'xiaoyan'
        self.soul = soul #提示词不同的提示词不同的任务，人设
        self.brain = brain #选择不同的LLM模型
        # self.timbre = timbre #选择不同的音色
        

    def thinking(self,question):
        # gpt3_llm = AzureOpenAI(temperature=0.5, max_tokens=1000, deployment_name="gpt-35-turbo", verbose=True)
        # gpt4_llm = AzureOpenAI(temperature=0, max_tokens=100, deployment_name="gpt-4", verbose=True)
        # 配置chatglm，填入chatglm的API地址本地就是127.0.0.1:xxxx
        chatGLM_llm = ChatGLM(
            endpoint_url="127.0.0.1:8899",
            max_token=320000,
            history=[],
            top_p=0.9,
            temperature=0.95,
            model_kwargs={"sample_model_args": True},
        )

        # llm.with_history = True
        # 获取上下文从新传入模型使得大模型有记忆能力，类似chatGPT的记忆功能
        memory = ConversationBufferMemory(memory_key="chat_history")
        llm_chain = LLMChain(prompt=self.soul, llm=chatGLM_llm, verbose=False, memory=memory)
        answer = llm_chain.run(question)
        return answer


 
    def speech(self,text):

        #edge-tts语音合成
        output_file = "./sample/recv_{}.mp3".format(time.time())
        async def _tts() -> None:
            communicate = edge_tts.Communicate(text, "zh-CN-XiaoyiNeural")
            await communicate.save(output_file)
        asyncio.run(_tts())

        # #MockingBird语音合成克隆
        # syn_models_dirt = "synthesizer/saved_models"
        # synthesizers = list(Path(syn_models_dirt).glob("**/*.pt"))
        # synthesizers_cache = {}
        # encoder.load_model(Path("encoder/saved_models/pretrained.pt"))
        # gan_vocoder.load_model(Path("vocoder/saved_models/pretrained/g_hifigan.pt"))
        # # Load input text
        # texts = text
        # punctuation = '！，。、,' # punctuate and split/clean text
        # processed_texts = []
        # for text in texts:
        #     for processed_text in re.sub(r'[{}]+'.format(punctuation), '\n', text).split('\n'):
        #         if processed_text:
        #             processed_texts.append(processed_text.strip())
        # texts = processed_texts
        # # synthesize and vocode
        # encoder_wav = encoder.preprocess_wav(wav, Synthesizer.sample_rate)
        # embed, _, _ = encoder.embed_utterance(encoder_wav, return_partials=True)
        # embeds = [embed] * len(texts)
        # current_synt = Synthesizer(Path("synt_path"))
        # specs = current_synt.synthesize_spectrograms(texts, embeds)
        # spec = np.concatenate(specs, axis=1)
        # # wav = rnn_vocoder.infer_waveform(spec)
        # wav = gan_vocoder.infer_waveform(spec)
        # # Return cooked wav
        # out = io.BytesIO()
        # output_file = write(out, Synthesizer.sample_rate, wav)
        return output_file


    def hear(self,audio_file):

        #openai开源whisper语音识别
        # r = sr.Recognizer()
        # with sr.Microphone() as source:
        #     # r.adjust_for_ambient_noise(source)
        #     audio = r.listen(source)
        # with open("microphone-results.raw", "wb") as f:
        # f.write(audio.get_raw_data())
        # try:
        #     result = r.recognize_whisper(audio,"tiny", language="zh")
        # except sr.UnknownValueError:
        #     print("Whisper could not understand audio")
        # except sr.RequestError as e:
        #     print("Could not request results from Whisper")
        result = model.transcribe(audio_file)
        return result

 
    def doSomeing(self,text):

        #Open Interpreter项目
        interpreter.chat(text) # Executes a single command
        interpreter.chat()
        return print("你想要做的"+text+"已经帮您觉解了哦")
        





