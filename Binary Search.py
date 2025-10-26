def BinarySearch(Array, SearchItem):
    Found = False
    SearchFailed = False
    First = 0
    Last = len(Array) - 1
    while (Found == False) and (SearchFailed == False):
        Middle = int((First + Last) / 2)
        if Array[Middle] == SearchItem:
            Found = True
            #if want position of value then return MidPoint here
        elif First > Last:
            SearchFailed = True
        elif Array[Middle] > SearchItem:
            Last = Middle - 1
        elif Array[Middle] < SearchItem:
            First = Middle + 1
    return Found

def RecursiveBinSearch(Array, TargetValue, Lower, Upper):
	if Lower > Upper:
		return -1
	Middle = (Lower + Upper) // 2
	if TargetValue == Array[Middle]:
		return Middle
	elif TargetValue > List[Middle]:
		return RecursiveBinSearch(Array, TargetValue, Middle + 1, Upper)
	else:
		return RecursiveBinSearch(Array, TargetValue, Lower, Middle - 1)