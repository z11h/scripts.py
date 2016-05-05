# Written by Zakaria Ridouh with lots of help from Brian Kieffer!
from random import randint
from datetime import datetime

def generate(low, high):
    list = {}
    numbers = []

    while True:
        randomInt = random.randint(int(low), int(high))
        if list[randomInt] == undefined:
            list[randomInt] = 1
        elif list[randomInt] < 2:
            list[randomInt]+=1
        else:
            continue
        break

    for key in list:
        numbers.append(key)

	# return the result
    return numbers

print "Welcome to the Random Number Generator!"

low = raw_input('Please enter the start (low) number: ')
high = raw_input('OK, Now please enter the ending (high) number: ')

print "Starting to generate some Random numbers!"

gen.generate(low, high)

print "Done generating!\n"
print "The number that stopped the loop is {}".format(1)
print "The current time is: " + str(datetime.now().time())
