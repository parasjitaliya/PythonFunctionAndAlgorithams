import Utility

while True:
   number= (input("Enter N for find N distinct coupons : "))
   # check user input is valid or not
   try:
       number = int(number)
   except ValueError:
       print('Please enter the valid number : ', type(number))
       continue
   if number >= 0:
       break
   else:
       print('Please enter positive number. ')

# call our coupons generate function and store all unique coupons into a list
count = Utility.N_coupons(number)

# display the our unique N coupons
print("Your random numbers to generate N distinct coupon numbers : ", count)