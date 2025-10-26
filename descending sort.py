def SortDescending(array):
    length = len(Animals)
    temp = ""
    for x in range(0, length - 1):
        for y in range(0, length - x - 1):
            if array[y][0] < array[y+1][0]:
                Temp = array[y]
                array[y] = array[y+1]
                array[y+1] = temp