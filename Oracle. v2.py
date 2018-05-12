"""Operational Revelator And Change Likeliness Estimator 2.0
            Made by Leveles"""

import re
import random
from random import randint

#Basic sentance openers that signify a yes or no answer
firstcheck = ("should", "can", "is", "will", "did", "do", "am", "are", "will", "was", "do")
firstanswers = ("yes", "no", "maybe", "perhaps", "probably not", "not going to touch this one")

#Outcomes from "what"
secondcheck = ("what")
nextSecondCheck = ("will", "is")
nextSecondCheckAnswers = ("bad things", "nothing.", "you know this already", "good things",
                          "complete destruction", "perfection")
#Outcomes from "how"
thirdCheck = ("how")
nextThirdCheck = ("many", "much")
nextThirdCheckTwo = ("will", "am", "are")
nextThirdCheckTwoAnswers = ("with failure", "with success", "badly", "averagely", "amazingly")
nextThirdCheckThree = ("more")
nextThirdCheckThreeAnswers = ("many more", "just a few", "it never ends")
nextThirdCheckAge = ("old")
doCan = ("do", "can")
doCanAnswers = ("it's not possible", "can't", "easily", "with difficulty")

#Outcomes from "When"
fourthCheck = ("when")
fourthCheckAnswers = ("soon", "never", "in a while", "now", "today", "in a long time", "didn't it already happen")

#Feelings
feelings = ("good", "bad", "afraid", "angry", "sad", "happy", "joyous", "disgusted", "surprised", "depressed", "manic",
            "strangely good", "almost dead", "anxious")

response = input("What do you want to know?\n")
response = str(response).lower()
starter = re.sub("[^\w]", " ",  response).split()

def teller():
    #answer setup
    answer = ""

    #if the question is not understood
    answerFailed = ("I'm sorry, I didn't understand the question")

    #yes or no check
    if starter[0] in firstcheck:
        answer = (random.choice(firstanswers))

    #what check
    elif starter[0] in secondcheck:
        if starter[1] in nextSecondCheck:
            answer = (random.choice(nextSecondCheckAnswers))

    #how check
    elif starter[0] in thirdCheck:

        #many check
        if starter[1] in nextThirdCheck:

            #more check
            if starter[2] in nextThirdCheckThree:
                either = randint(1,2)
                if either == 1:
                    answer = (random.choice(nextThirdCheckThreeAnswers))
                else:
                    manyValue = randint(0,randint(10, 100))
                    answer = (manyValue)
            else:
                manyValue = randint(0,randint(10, 100))
                answer = (manyValue)

        #age check
        elif starter[1] in nextThirdCheckAge:
            manyValue = randint(0,randint(10, 100))
            answer = (manyValue)

        #person attach check
        elif starter[1] in nextThirdCheckTwo:

            #feeling check
            if starter[2] != "you":
                if starter[1] == "will":

                    print(starter[2])
                    answer = (random.choice(nextThirdCheckTwoAnswers))
                else:
                    answer = (random.choice(feelings))
            else:
                answer = (random.choice(feelings))

        #do can check
        elif starter[1] in doCan:
            answer = (random.choice(doCanAnswers))

        else:
            answer = answerFailed
    elif starter[0] in fourthCheck:
        answer = (random.choice(fourthCheckAnswers))

    else:
        answer = answerFailed

    answer = (str(answer).capitalize() + ".")

    return answer

answer = teller()

print(answer)