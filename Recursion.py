#count up and down
def count_up_down(n):
    print(n)
    if n > 1:
        count_up_down(n-1)
    print(n)

#factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#fibonacci number at given n
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#string reversal
def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        char = string[len(string) - 1]
        strn = string[:(len(string) - 1)]
        return char + reverse_string(strn)

#sum of a list
def sum_list(mylist):
    if len(mylist) == 0:
        return 0
    else:
        return mylist[0] + sum_list(mylist[1:])

#recursive binary search
def binary_search(List, TargetVal, Lower, Upper):
    if Lower > Upper:
        return -1
    Middle = (Lower+Upper)//2
    if TargetVal == List[Middle]:
        return Middle
    elif TargetVal > List[Middle]:
        return binary_search(List, TargetVal, Middle+1, Upper)
    else:
        return binary_search(List, TargetVal, Lower, Middle-1)

#tower of Hanoi
def tower_of_hanoi(n, source, spare, target):
    if n >= 1:
        tower_of_hanoi(n-1, source, target, spare)
        print("Move disk", n, "from", source, "to", target)
        tower_of_hanoi(n-1, spare, source, target

#recursion with backtracking


#N-Queens Problem (Recursion + Backtracking)
