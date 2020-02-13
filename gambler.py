from builtins import print

import Utility

print("---------------welcome in to gambler program--------------")
# take user input from user
stake = int(input("enter your stake value..:"))
goal = int(input("enter your goal what you want..:"))
if stake > 0 and goal > 0 :
    print(Utility.gambler(stake, goal))
else:
    print("Invalid input!!")



