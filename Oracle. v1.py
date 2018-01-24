"""Operational Revelator And Change Likeliness Estimator
            Made by Leveles"""

import re
import random
from random import randint

firstcheck = ("should", "can", "is", "will", "did", "do", "am", "are", "will", "was")
firstanswers = ("Yes", "No", "Maybe", "Perhaps", "Probably not", "Not going to touch this one")

secondcheck = ("what")
nextSecondCheck = ("will", "is")
nextSecondCheckAnswers = ("Bad things", "Nothing.", "You know this already", "Good things",
                          "Complete destruction", "Perfection")

thirdCheck = ("how")
nextThirdCheck = ("many", "much")
nextThirdCheckTwo = ("will", "can", "am", "are")
nextThirdCheckTwoAnswers = ("With failure", "With success", "Badly", "Averagely", "Amazingly")
nextThirdCheckThree = ("more")
nextThirdCheckThreeAnswers = ("Many more", "Just a few", "Almost done", "It never ends")

fourthCheck = ("when")
fourthCheckAnswers = ("Soon", "Never", "In a while", "Now", "Today", "In a long time", "Didn't it already happen")

feelings = ("Good", "Bad", "Sad", "Happy", "Depressed", "Manic", "Strangely good", "Almost dead")

response = input("What do you want to know?\n")
response = str(response).lower()
starter = re.sub("[^\w]", " ",  response).split()

def teller():
    answer = ""
    if starter[0] in firstcheck:
        answer = (random.choice(firstanswers))
    elif starter[0] in secondcheck:
        if starter[1] in nextSecondCheck:
            answer = (random.choice(nextSecondCheckAnswers))
    elif starter[0] in thirdCheck:
        if starter[1] in nextThirdCheck:
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
        if starter[1] in nextThirdCheckTwo:
            if starter[2] != "you":
                if starter[2] != "I":
                    answer = (random.choice(nextThirdCheckTwoAnswers))
                else:
                    answer = (random.choice(feelings))
            else:
                answer = (random.choice(feelings))
    elif starter[0] in fourthCheck:
        answer = (random.choice(fourthCheckAnswers))

    else:
        answer = ("I'm sorry, I didn't understand the question")


    answer = (str(answer) + ".")

    return answer

answer = teller()

print(answer)