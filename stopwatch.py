import time

print("---------------------- welcom to stopwatch program ------------------------")

time_start_input = input("press enter key to start the time..........!!")
start = time.time()

time_start_output = input("press enter key to end the time...........!!")
end = time.time()

total_time = end-start
print(f"Total time is: {round(total_time,6)}sec")