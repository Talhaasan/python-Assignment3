import random
import time
import matplotlib.pyplot as plt

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var


def bucket_sort(input_list):
    # Find maximum value in the list and use length of the list to determine which value in the list goes into which bucket
    max_value = max(input_list)
    size = max_value / len(input_list)

    # Create n empty buckets where n is equal to the length of the input list
    buckets_list = []
    for x in range(len(input_list)):
        buckets_list.append([])

        # Put list elements into different buckets based on the size
    for i in range(len(input_list)):
        j = int(input_list[i] / size)
        if j != len(input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    # Sort elements within the buckets using Insertion Sort
    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])

    # Concatenate buckets with sorted elements into a single list
    final_output = []
    for x in range(len(input_list)):
        final_output = final_output + buckets_list[x]
    return final_output



runTimes=[]
totalnk=[]
for i in range(10):
    # array's number of elements, describe as n and random value 2 and 10.
    n = random.randint(2, 10)
    array = []
    for a in range(n):
        # array's values range as k and array's value range is randomly 0 and 1000.
        k = random.randint(0, 100)
        array.append(k - 1)
    begin = time.time()
    print('Original List:')
    print(array)
    sorted_list = bucket_sort(array)
    print('Sorted List:')
    print(sorted_list)
    time.sleep(1)
    end = time.time()
    print(f"Total runtime of the program is {end - begin}")
    print(f"n+k value is : {n+k}")
    print(f"time value is : {end - begin}")  
    runTimes.append(n+k)
    totalnk.append(end-begin)
    print()

plt.figure()
plt.plot(runTimes, totalnk,'o', color='black')
 # naming the x axis
plt.xlabel('n+k')
 # naming the y axis
plt.ylabel('Time (s)')
 # giving a title to a graph
plt.title('Comparing Run Time')
plt.show()



    