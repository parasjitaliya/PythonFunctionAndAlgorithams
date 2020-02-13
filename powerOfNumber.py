import Utility
power = int(input("enter the number for power you want"))
if (power < 31):
    print(Utility.power_of_2(power))
else:
    print("enter the number lessthen 31")
