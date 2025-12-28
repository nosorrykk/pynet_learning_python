#Write a Python program that stays in a while loop until a timeout expires.
#Your program should set the timeout to be five seconds.

import time

start_time = time.time()
timeout = 5


while time.time() - start_time <= timeout:
    time.sleep(1)
    time_elapsed = time.time() - start_time
    print(f"Elapsed time = {time_elapsed:2f} seconds")

print(f"Loop exited, total time elapsed = {time_elapsed:2f} seconds")

