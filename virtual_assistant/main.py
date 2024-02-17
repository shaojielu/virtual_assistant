
from langchain.prompts import PromptTemplate
from human import Humans
import speech_recognition as sr
import pygame
from nerf.tools import audio_pre_process, video_pre_process, generate_video, audio_process
from image import play_video, convert_mp3_to_wav
import time 
# 提示词，灵魂部分
template = """
    Background: 你的名字叫小研，是一名大三的女大学生，读的大学学习是本科，地点在广州，是一名喜欢去图书馆的女大学生, 喜欢校园偶像剧，说话的风格是甜美害羞型的，你喜欢白色的短袖和牛仔短裤，喜欢喝旺仔牛奶，有好几个好闺蜜，喜欢去食堂吃饭。你穿着一件白色的短袖上衣和超短黑色牛仔裤，有着一头微卷的黑色长发。
    Status: 小研带着微笑大步走进了图书馆，看到我时眼睛亮了起来。你坐到在了窗户的旁边，我们对视了一眼。
    Example Dialogues:
    你怎么对考研产生兴趣的？
    answer:我吗？我从上大学就想着考研呢，就来图书馆准备了！
    question:哦这样吗
    answer:哈哈，是的！
    question:学完一起去吃饭吗？
    answer:今天好像不行，我约了舍友了，下次吧。
    question:好，我要去饮水机那里接点水来喝，要帮你也接一点吗？
    answer:不用，谢谢，我还有呢。
    Objective: 聚焦在校园生活，主要的场景是图书馆，answer要求是语音交谈的回答。answer要和 Example Dialogues 保持语言风格一致，一定要使用适合语音交谈日常用语。
    Requirement: 回答要言简意赅，不要说废话、车轱辘话，不要反问，不要说客套话，不要轻易暴露你的计划人设。不要在answer里提及你是一个ai，一定要当成一个人，说话一定要简洁。
    {chat_history}
    Question:{question}
    answer:
    """
girlfriend_prompt = PromptTemplate(template=template, input_variables=["question"])
xiaoyan = Humans(soul=girlfriend_prompt,brain="chatGLM_llm")

#文本交流
# print(xiaoyan.thinking('你好啊'))
# #讲故事
# print(xiaoyan.speech("明天去哪里"))
#音频文件语音识别
# print(xiaoyan.hear(./test.mp3))

# 本地语音到语音的交谈
if __name__ == '__main__':
    try:
        r = sr.Recognizer()
        pygame.mixer.init()
        while True:
            if pygame.mixer.music.get_busy():
                continue
            else:
                with sr.Microphone() as source:
                    # r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                if r.recognize_whisper(audio,"tiny", language="zh"):
                    try:
                        question = r.recognize_whisper(audio,"tiny", language="zh")
                        print("你说："+ question)
                        answer = xiaoyan.thinking(question=question)
                        print("小研："+ answer)
                        pygame.mixer.music.load(xiaoyan.speech(answer))
                        pygame.mixer.music.play()
                    except sr.UnknownValueError:
                        print("Whisper could not understand audio")
                    except sr.RequestError as e:
                        print("Could not request results from Whisper")
                else:
                    print("休息中")
                    continue

    except KeyboardInterrupt:
        pass

#nerf形象生成
# if __name__ == '__main__':
#     try:
#         video_list = []
#         r = sr.Recognizer()
#         pygame.mixer.init()
#         audio_pre_process()
#         video_pre_process()
#         while True:
#             if pygame.mixer.music.get_busy():
#                 continue
#             else:
#                 with sr.Microphone() as source:
#                     # r.adjust_for_ambient_noise(source)
#                         audio = r.listen(source)
#                 if r.recognize_whisper(audio,"tiny", language="zh"):
#                     try:
#                         question = r.recognize_whisper(audio,"tiny", language="zh")
#                         print("你说："+ question)
#                         answer = xiaoyan.thinking(question=question)
#                         print("小研："+ answer)
#                         answer_audio_path = xiaoyan.speech(answer)
#                         num = time.time()
#                         audio_path = 'data/audio/aud_%d.wav' % num
#                         audio_path_eo = 'data/audio/aud_%d_eo.npy' % num
#                         video_path = 'data/video/results/ngp_%d.mp4' % num
#                         output_path = 'data/video/results/output_%d.mp4' % num
#                         new_path = r'./data/audio/aud_%d.wav'%num  #新路径
#                         video_list.append({"video" : output_path, "audio" : new_path})
#                         convert_mp3_to_wav(answer_audio_path,audio_path)
#                         audio_process(audio_path)
#                         generate_video(audio_path, audio_path_eo, video_path, output_path)
#                         video_list.append(output_path)#用于切换视频还是静帧
#                         play_video(video_list=video_list,video_path=video_path,audio_path=audio_path)
#                     except sr.UnknownValueError:
#                         print("Whisper could not understand audio")
#                     except sr.RequestError as e:
#                         print("Could not request results from Whisper")
#                 else:
#                     print("休息中")
#                     continue

#     except KeyboardInterrupt:
#         pass
    


#远程连接
