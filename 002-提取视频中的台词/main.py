from moviepy import VideoFileClip
import speech_recognition as sr

def get_video_audio(video_path, audio_path):
    clip = VideoFileClip(video_path)
    # 提取音频
    audio = clip.audio
    audio.write_audiofile(audio_path)  # 保存为WAV格式，因为SpeechRecognition库支持WAV格式


def recognize_google(audio_data_path, language='zh-CN'):
    # 初始化识别器
    recognizer = sr.Recognizer()

    # 加载音频文件
    with sr.AudioFile(audio_data_path) as source:
        audio_data = recognizer.record(source)

    # 使用Google Web Speech API进行语音识别
    try:
        text = recognizer.recognize_google(audio_data, language=language)  # 对于中文视频，使用'zh-CN'
        print("Detected text:", text)
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Web Speech API; {0}".format(e))


if __name__ == '__main__':
    temp_audio_path = 'output_audio.wav'
    get_video_audio('demo.mp4', temp_audio_path)
    recognize_google(temp_audio_path)