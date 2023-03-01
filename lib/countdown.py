# your code goes here!
import time
def countdown(x):
    while x >= 0:
        if x != 0: 
            print(f"{x} SECOND(S)!")
        else:
            print('HAPPY NEW YEAR!')
        x-=1

def countdown_with_sleep(x):
    while x >= 0:
        if x != 0: 
            print(f"{x} SECOND(S)!")
            time.sleep(1)
        else:
            print('HAPPY NEW YEAR!')
        x-=1