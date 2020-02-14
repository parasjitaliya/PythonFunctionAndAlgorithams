import Utility
print("Temperature should be less then 50F and wind speed is between (3,120)miles per hour")
#take user input from user
temp=int(input("Enter the temperature in fahrenheit :"))
wind_speed=int(input("Enter the wind speed in miles per hour :"))

#function call
print(f"wind_chill={Utility.wind_chill(temp,wind_speed)}")