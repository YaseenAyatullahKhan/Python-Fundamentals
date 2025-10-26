def InsertionSort(array):
    #CurrentItem is hole-position
    NumberOfItems = len(array)
    for Pointer in range(1, NumberOfItems):
        ItemToBeInserted = array[Pointer]
        CurrentItem = Pointer - 1
        while (CurrentItem > -1) and (array[CurrentItem] > ItemToBeInserted):
            array[CurrentItem + 1] = array[CurrentItem]
            CurrentItem = CurrentItem - 1
        array[CurrentItem + 1] = ItemToBeInserted