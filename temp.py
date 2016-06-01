# Written by Zakaria Ridouh on 5/2/2016 Todo: Add Kelvins calc
def start():  # Haha
        print "Temperature converter"


def conv(start, final):
    if final.upper() == "F":
        print "{0}C = {1}F".format(str(start), str((5/9)*int(start)-32))
    elif final.upper() == "C":
        print "{0}F = {1}C".format(str(start), str((9/5)*int(start)+32))
    else:
        print "Error, sorry!"
# Todo: Add Kalvin Converter

print "Welcome to the Tempurature Converter script by Zakaria Ridouh"
start()
temp = raw_input("Enter a temperature: ")
to = raw_input("Convert to (F)ahrenheit or (C)elsius?")
conv(temp, to)
