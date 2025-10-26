def BubbleSort(array):
    #ascending sort for numeric array
    NoSwaps = False
    Boundary = len(array) - 1
    temp = 0
    while NoSwaps == False:
        NoSwaps = True
        for i in range(0, Boundary):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = array[i]
                NoSwaps = False
        Boundary = Boundary - 1