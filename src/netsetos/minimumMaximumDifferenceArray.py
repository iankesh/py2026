import math
def min_diff_arr():
    arr = [5,32,45,4,12,18,25]
    arr.sort()
    print(arr)
    diff = float('inf')
    # diff = math.inf
    for i in range(0, len(arr)-1):
        if arr[i+1]-arr[i] < diff:
            diff = arr[i+1]-arr[i]

    print(diff)
    # print(float('inf'))

def max_diff_array():
    arr = [5,32,45,4,12,18,25]
    arr.sort()
    diff = 0
    for i in range(len(arr)-1):
        if arr[i+1]-arr[i] > diff:
            diff = arr[i+1]-arr[i]
    print(diff)

min_diff_arr()
max_diff_array()