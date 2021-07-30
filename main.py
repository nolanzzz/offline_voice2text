import speech_recognition as sr

print("请输入完整文件路径：")
file_dir = str(input())
print("转换中，请等待...")
r = sr.Recognizer()
test = sr.AudioFile(file_dir)

with test as source:
    audio = r.record(source)
type(audio)
c = r.recognize_sphinx(audio, language='zh-CN')
print("\n转换结果：\n")
print(c)
