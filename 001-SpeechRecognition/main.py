import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("请说话...")
    audio = recognizer.listen(source, timeout=5)

try:
    text = recognizer.recognize_google(audio, language='zh-CN')
    print("识别结果:", text)
except sr.UnknownValueError:
    print("无法识别音频")
except sr.RequestError as e:
    print(f"API请求错误: {e}")

