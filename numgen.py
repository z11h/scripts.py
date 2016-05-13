# Written by Zakaria Ridouh with help from Brian Kieffer!
from random import randint
from datetime import datetime


def gen(low, high):
    list = {}
    while True:
        randomInt = randint(int(low), int(high))
        print randomInt
        try:
            if list[randomInt] < 3:
                list[randomInt] += 1
            else:  # when it equals 3
                print "Done generating!\n"
                print "The number that broke the loop is {0}".format(randomInt)
                break
        except:
            list[randomInt] = 0

print "Welcome to the Random Number Generator!"

low = raw_input('Please enter the start (low) number: ')
high = raw_input('OK, Now please enter the ending (high) number: ')

print "Starting to generate some Random numbers!"

gen(low, high)
print "The current time is: " + str(datetime.now().time())
