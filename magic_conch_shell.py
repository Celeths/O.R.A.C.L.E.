import importlib
import random
from random import randint
import magic_conch_shell
import vocab

def teller(starter):
    global answer, error

    # answer setup
    answer = ""

    # error setup
    error = ""

    # if the question is not understood
    answerFailed = ("I'm sorry, I didn't understand the question")

    #yes or no check
    if starter[0] in vocab.firstcheck:
        answer = (random.choice(vocab.firstanswers))

    #what check
    elif starter[0] in vocab.secondcheck:
        if starter[1] in vocab.nextSecondCheck:
            answer = (random.choice(vocab.nextSecondCheckAnswers))

    #how check
    elif starter[0] in vocab.thirdCheck:

        #many check
        if starter[1] in vocab.nextThirdCheck:

            #more check
            if starter[2] in vocab.nextThirdCheckThree:
                either = randint(1,2)
                if either == 1:
                    answer = (random.choice(vocab.nextThirdCheckThreeAnswers))
                else:
                    manyValue = randint(0,randint(10, 100))
                    answer = (manyValue)
            else:
                manyValue = randint(0,randint(10, 100))
                answer = (manyValue)

        #age check
        elif starter[1] in vocab.nextThirdCheckAge:
            manyValue = randint(0,randint(10, 100))
            answer = (manyValue)

        #person attach check
        elif starter[1] in vocab.nextThirdCheckTwo:

            #feeling check
            if starter[2] != "you":
                if starter[1] == "will":

                    print(starter[2])
                    answer = (random.choice(vocab.nextThirdCheckTwoAnswers))
                else:
                    answer = (random.choice(vocab.feelings))
            else:
                answer = (random.choice(vocab.feelings))

        #do can check
        elif starter[1] in vocab.doCan:
            answer = (random.choice(vocab.doCanAnswers))

        else:
            answer = answerFailed
    elif starter[0] in vocab.fourthCheck:
        answer = (random.choice(vocab.fourthCheckAnswers))

    else:
        answer = answerFailed
        error = "record"

    answer = (str(answer).capitalize() + ".")

    return answer