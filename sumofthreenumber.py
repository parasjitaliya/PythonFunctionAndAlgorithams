import Utility
print("-------------------sum of three integer number is zero ---------------")
n = int(input("enter the num of integers:"))
listnum =[]
for i in range(n):
    listnum.append(int(input()))
print(Utility.numbersum(listnum))