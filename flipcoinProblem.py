import random

coinflips = int(input("How many times you want toflip coin:"))


def flipcoinProblem(coinflips):
    head = 0
    tail = 0
    for i in range(coinflips):
        num = random.random()
        if num > 0.5:
            tail = tail + 1
        else:
            head = head + 1
    head_percentage = (head / coinflips) * 100
    tail_percentage = (tail / coinflips) * 100
    return head_percentage, tail_percentage


head_percent, tail_percent = flipcoinProblem(coinflips)
print(f"Head percent is {head_percent}% and tail percent is {tail_percent}%")
