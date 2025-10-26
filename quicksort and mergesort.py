def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) - 1]
    left = [i for i in array[:(len(array)-1)] if i <= pivot]
    right = [i for i in array[:(len(array)-1)] if i > pivot]
    return quicksort(left) + [pivot] + quicksort(right)
#O(nlog(n)) avg, O(n²) worst case

def mergesort(array):
    if len(array) > 1:
        left = array[:len(array)//2]
        right = array[len(array)//2:]
        #recursion
        mergesort(left)
        mergesort(right)
        #merge
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
        return array
    else:
        return array
#always O(nlog(n))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

arr = [3, 6, 8, 10, 1, 2, 1]
print(mergesort(arr))