from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play


tts = gTTS(text="Hello, how are you today?", lang="en", slow=False)
mp3_audio = BytesIO()
tts.write_to_fp(mp3_audio)
mp3_audio.seek(0)
play(AudioSegment.from_mp3(mp3_audio))
print("Done")
