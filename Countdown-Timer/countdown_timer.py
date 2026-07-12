# Countdown timer program
import time

my_time = int(input("Enter the time in seconds: "))

for i in range(my_time, 0, -1):
    seconds = i % 60
    minuts = int(i / 60) % 60
    hours = int(i / 3600) % 24
    days = int(i / 86400)
    print(f"{days} days, {hours:02}:{minuts:02}:{seconds:02}")
    time.sleep(1)

print("Time's UP!")