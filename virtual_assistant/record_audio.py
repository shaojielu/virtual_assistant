import pyaudio
import wave
import threading
from main import xiaoyan
class AudioManager:
    def __init__(self):
        self.playing = False
        self.play_thread = None
        self.microphone_stream = None

    def play_audio(self, file_path):
        self.playing = True
        chunk = 1024

        # Open audio file
        wf = wave.open(file_path, 'rb')

        # Instantiate PyAudio
        p = pyaudio.PyAudio()

        # Open output stream
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # Play audio stream
        data = wf.readframes(chunk)
        while data and self.playing:
            stream.write(data)
            data = wf.readframes(chunk)

        # Close stream
        stream.stop_stream()
        stream.close()

        # Close PyAudio
        p.terminate()

    def start_audio(self, file_path):
        if not self.play_thread or not self.play_thread.is_alive():
            self.play_thread = threading.Thread(target=self.play_audio, args=(file_path,))
            self.play_thread.start()

    def stop_audio(self):
        self.playing = False

    def start_microphone(self):
        self.microphone_stream = pyaudio.PyAudio().open(format=pyaudio.paInt16,
                                                        channels=1,
                                                        rate=44100,
                                                        input=True,
                                                        frames_per_buffer=1024)
        self.microphone_stream.start_stream()

    def stop_microphone(self):
        if self.microphone_stream:
            self.microphone_stream.stop_stream()
            self.microphone_stream.close()

# Your audio file path
file_path = xiaoyan.speech(xiaoyan.thinking(xiaoyan.hear()))

# Instantiate AudioManager
audio_manager = AudioManager()

# Start microphone thread
audio_manager.start_microphone()

# Start playing audio
audio_manager.start_audio(file_path)

# Wait for the audio to finish playing (you can do other tasks here)
audio_manager.play_thread.join()

# Stop microphone
audio_manager.stop_microphone()
