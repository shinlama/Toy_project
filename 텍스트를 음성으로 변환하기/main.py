from gtts import gTTS

text = '안녕하세요. 제 이름은 신지원입니다. 코딩을 하고 있습니다.'
tts = gTTS(text= text, lang='ko')
tts.save(r'텍스트를 음성으로 변환하기/hi.mp3')