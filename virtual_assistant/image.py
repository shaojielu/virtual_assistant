import threading
from pydub import AudioSegment
import cv2
import pygame



def convert_mp3_to_wav(input_file, output_file):
    audio = AudioSegment.from_mp3(input_file)
    audio.export(output_file, format='wav')

def play_video(video_list,video_path,audio_path):
    video_list = video_list
    video_path = video_path
    audio_path = audio_path
    ret = None
    frame = None
    while True:
        if len(video_list) > 0:
            video_path = video_list[0].get("video")
            audio_path = video_list[0].get("audio")
            cap = cv2.VideoCapture(video_path)  # 打开视频文件
            video_list.pop(0)
        else:
            audio_path = None
            cap = None
            # _, frame = cv2.VideoCapture("data/pretrained/train.mp4").read()
            _, frame = cv2.VideoCapture("data/pretrained/train2.mp4").read()

        if audio_path:
            threading.Thread(target=play_audio, args=[audio_path]).start()  # play audio
        # 循环播放视频帧
        while True:
            if cap:
                ret, frame = cap.read()
                print('视频生成中')
            if frame is not None:#没有传音频过来时显示train.mp4的第一帧，建议替换成大约1秒左右的视频
                cv2.imshow(frame)
                # 等待 38 毫秒
                cv2.waitKey(38)
            if not ret:
                break

def play_audio(audio_file):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()
