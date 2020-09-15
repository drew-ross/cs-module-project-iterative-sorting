def selection_sort(arr):
    if arr:
        for i in range(len(arr)):
            smallest_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[smallest_index]:
                    smallest_index = j
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    if arr:
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


"""
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
"""


def counting_sort(arr, maximum=None):
    if arr:
        if not maximum:
            maximum = arr[0]
            for num in arr:
                if num > maximum:
                    maximum = num

        count = [0] * (maximum + 1)
        sum_count = [0] * (maximum + 1)
        output = [0] * len(arr)
        
        for num in arr:
            if num < 0:
                return "Error, negative numbers not allowed in Count Sort"
            count[num] += 1
        for i in range(len(sum_count)):
            sum_count[i] = sum_count[i - 1] + count[i]
        for num in arr:
            output[sum_count[num] - 1] = num
            sum_count[num] -= 1
        arr = output

    return arr
