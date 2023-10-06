# Typing speed test python project. 

from time import *
import random as r


def mistake(paratest,usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error = error+1
        except:
            error = error+1
            
    return error 

def speed_time(time_s,time_e,userinput):
    time_delay =    time_e - time_s
    time_r = round(time_delay,2)
    speed = len(userinput)/time_r
    return round(speed)
if __name__ == '__main__':
    while True:
        ck = input("ready to test: yes/no:")
        if ck == "yes":
            test = ["Teaser and spy shots have already revealed key elements in design of the upcoming SUV.","Hi Guys Welcome"]

            test1 = r.choice(test)
            print("****typing speed calculator****")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput = input("Enter:")
            time_2 = time()

            print('Speed:',speed_time(time_1,time_2,testinput),"w/sec")
            print("Error:",mistake(test1,testinput))
        elif ck == 'no':
            print("Thank you!")
            break
        else:
            print("Wrong Input!")

