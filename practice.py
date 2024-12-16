print("my name is jaydeva")
import timeit

def timer_loop():
    for i in range(100):
        pass

time_result = timeit.timeit(timer_loop, number=1)
print(f"Time taken to execute loop: {time_result} seconds")
