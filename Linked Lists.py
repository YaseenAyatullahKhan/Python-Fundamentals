class ListNode:
    # PUBLIC Data : STRING
    # PUBLIC Pointer : INTEGER
    def __init__(self, DataP, PointerP):
        self.Data = DataP
        self.Pointer = PointerP
#DECLARE List : ARRAY[0:9] OF ListNode
List = [ListNode("", 0) for i in range(0, 10)]

def Initialise():
    #DECLARE FreeListPtr : INTEGER
    global List
    StartPtr = 0
    FreeListPtr = 0
    for index in range(0, 9):
        List[index].Pointer = index + 1
    List[9].Pointer = -1

def InsertNode(NewItem):
    global List, FreeListPtr, StartPtr
    if FreeListPtr != -1:   #there's space in list
		    #add the data item
        NewNodePtr = FreeListPtr
        List[NewNodePtr].Data = NewItem
        FreeListPtr = List[FreeListPtr].Pointer
        #find insertion point
        ThisNodePtr = StartPtr
        PreivousNodePtr = -1
        while (ThisNodePtr != -1) and (List[ThisNodePtr].Data < NewItem):
            #  ^^^ while not end of list
            PreviousNodePtr = ThisNodePtr   # remember this node
            # follow pointer to next node
            ThisNodePtr = List[ThisNodePtr].Pointer
        if PreviousNodePtr == StartPtr:    # insert new node at start of list
            List[NewNodePtr].Pointer = StartPtr
            StartPtr = NewNodePtr
        else:
            # insert new node between previous node and this node
            List[NewNodePtr].Pointer = List[PreviousNodePtr].Pointer
            List[PreviousNodePtr].Pointer = NewNodePtr

def DeleteNode(DeleteItem):
    global List, StartPtr, FreeListPtr
    CurrentPtr = StartPtr
    while CurrentPtr != -1 and List[CurrentPtr].Data != DeleteItem:
        PreviousPtr = CurrentPtr    #remember this node
        CurrentPtr = List[CurrentPtr].Pointer
    if CurrentPtr == -1:
        print("The item does not exist")
    else:    #item was found - change pointers
        if CurrentPtr == StartPtr:    #if item at beginning
            StartPtr = List[StartPtr].Pointer
        else:    #somewhere in middle of list
            List[PreviousPtr].Pointer = List[CurrentPtr].Pointer
        #carry out deletion
        List[CurrentPtr].Data = ""
        List[CurrentPtr].Pointer = FreeListPtr
        FreeListPtr = CurrentPtr

def FindNode(FindItem):
    global StartPtr, List
    CurrentPtr = StartPtr
    while CurrentPtr != -1 and List[CurrentPtr].Data == FindItem:
            CurrentPtr = List[CurrentPtr].Pointer
    return CurrentPtr

def OutputAllNodes():
    global StartPtr, List
    CurrentPtr = StartPtr
    while CurrentPtr != -1:
        print(List[CurrentPtr].Data)
        CurrentPtr = List[CurrentPtr].Pointer