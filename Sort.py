import random
import time


def shuffle_shuffle(n):
    num_list = [i for i in range(1, n)]
    random.shuffle(num_list)
    sorted_list = sorted(num_list)
    count_list = []

    for i in range(10):
        rep_count = 0
        random.shuffle(num_list)
        while num_list != sorted_list:
            rep_count += 1
            random.shuffle(num_list)
        count_list.append(rep_count)

    average = int(sum(count_list) / 10)
    return average


for iteration in range(1, 11):
    time1 = time.perf_counter()
    count = shuffle_shuffle(iteration)
    time2 = time.perf_counter()
    total_time = (time2 - time1)
    print(f"An array of {iteration} object(s) took an average of {count:,d} shuffles to sort. It took {total_time*1:0.4f} seconds.")

print("Why did you run this?")
