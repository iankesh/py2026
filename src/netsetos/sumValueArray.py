def sum_value_array():
    arr = [5,7,4,3,9,8,19,21]
    n = 17
    print(arr)
    arr.sort()
    print(arr)
    for i in range(0, len(arr)):
        if arr[i] > n:
            continue
        else:
            for j in range(i, len(arr)):
                if arr[j] > n:
                    continue
                elif arr[i] + arr[j] == n:
                    print("i=", arr[i], " j=", arr[j])
sum_value_array()