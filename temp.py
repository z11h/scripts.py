# Written by Zakaria Ridouh on 5/2/2016
def start():
        print "Temperature converter"
def conv(start, final):
        if final.upper() == "F":
            print "{}C = {}F".format(str(start), str((5/9)*int(start)-32))
        elif final.upper() == "C":
            print "{}F = {}C".format(str(start), str((9/5)*int(start)+32))
        else:
            print "Error, sorry!"
print "Welcome to the Tempurature Converter script by Zakaria Ridouh"
start()
temp = raw_input("Enter a temperature: ")
to = raw_input("Convert to (F)ahrenheit or (C)elsius?")
conv(temp, to)
