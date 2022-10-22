from math import fsum
import logging
from random import randint
import threading

from collections import Counter
import matplotlib.pyplot as plt

logger = logging.basicConfig(level=logging.INFO)

PROBABILITY = [80, 60, 40, 20]

def question(probability: int):
    ''' 
    Question 
        returns if question was answerd right or false using the given probability
        The propability is an integer representing the probability as a percentage 
    '''
    s = randint(1, 100)
    logging.debug(f"{s} / {probability}   chance")
    if s <= probability:
        return True
    return False

def switchFinal():
    ''' 
    switchFinal
        this simulates the final of switch
        it checks if the question is answered rightly, then it goes to the next question
        if the question is answered falsly, we return to the first question
        the questionCount is used to count the number of answered questions
        if the questionCount succeeds LIMIT the function is stoped because an endless loop was detected
    '''

    LIMIT = 1000
    questionCount = 0
    
    while True:
        if questionCount > LIMIT:
            logging.warning("loop limit reached")
            break
        complete = False
        for i in range(4):
            t = question(PROBABILITY[i])
            questionCount += 1
            if t:
                logging.debug(f"q{i} true")
                if i == 3:
                    logging.debug(f"done")
                    complete = True
                    break
            else:
                logging.debug(f"q{i} false")
                break
        if complete:
            logging.debug(questionCount)
            return questionCount
        

class thread(threading.Thread):
    '''
    Thread class
        used to run the code multithreaded, so the simulation runs faster
        it plays 100 000 finals
    '''
    def run(self):
        subtotalQuestionCount = []
        for i in range(100000):
            subtotalQuestionCount.append(switchFinal())
        totalQuestionCount.extend(subtotalQuestionCount)

#list of threads
threads = []
for i in range(10):
    threads.append(thread())
# starting the simulation
totalQuestionCount = []
for i in threads:
    i.run()


totalQuestionCount.sort()

#calculating the average
print(fsum(totalQuestionCount)/len(totalQuestionCount))

#showing the plot of the simulation
count = Counter(totalQuestionCount)
plt.plot(count.keys(), count.values())
plt.plot([fsum(totalQuestionCount)/len(totalQuestionCount)])
plt.show()
