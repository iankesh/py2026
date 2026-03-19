def trapping_rain_water_left():
    arr = [1,0,2,0,1,0,3,1,0,2]
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            arr[i] = arr[i-1]
    print(arr)

def trapping_rain_water_right():
    arr = [1,0,2,0,1,0,3,1,0,2]
    for i in range(len(arr)-1, 0, -1):
        if arr[i] > arr[i-1]:
            arr[i-1] = arr[i]
    print(arr)

trapping_rain_water_left()
trapping_rain_water_right()
