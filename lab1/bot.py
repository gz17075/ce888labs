from sopel import module
from emo.wdemotions import EmotionDetector
import sys

emo = EmotionDetector()

@module.rule('')
def hi(bot, trigger):
    #print(trigger, trigger.nick)
    #bot.say('Hi, ' + trigger.nick)
    emotionres = emo.detect_emotion_in_raw_np(trigger)
    print (emotionres, trigger.nick, trigger)
    bot.say('Your emotions: ' + str(emotionres))



