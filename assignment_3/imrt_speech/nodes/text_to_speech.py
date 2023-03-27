#! /usr/bin/env python3
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
import random
import rospy
from std_srvs.srv import Trigger, TriggerResponse
from imrt_speech.srv import Phrase, PhraseResponse

def my_callback(request):

    txt = random.choice(txt_list)
    list_txt.append(txt)

    return TriggerResponse(success = True,
                           message = txt)

def my_callback2(request):

    txt = request.phrase
    list_txt.append(txt)

    return PhraseResponse(success = True,
                          message = txt)

def talker(list_of_text):

    while len(list_of_text) > 0:
        txt = list_of_text[0]
        list_of_text.pop(0)
        tts = gTTS(text=txt, lang="en", slow=False)
        mp3_audio = BytesIO()
        tts.write_to_fp(mp3_audio)
        mp3_audio.seek(0)
        play(AudioSegment.from_mp3(mp3_audio))


list_txt = []
rospy.init_node("text_to_speech")
my_service = rospy.Service("~say_random", Trigger, my_callback)
my_service_2 = rospy.Service("~say_phrase", Phrase, my_callback2)
txt_list = rospy.get_param("/phrases", ["I have nothing to say to you!"])
 
while not rospy.is_shutdown():
    talker(list_txt)