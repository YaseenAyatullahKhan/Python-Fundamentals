class TreeNode:
	#PUBLIC Data : STRING
	#PUBLIC LeftPointer, RightPointer : INTEGER
	def __init__(self, pData, pLeftPointer, pRightPointer):
		self.Data = pData
		self.LeftPointer = pLeftPointer
		self.RightPointer = pRightPointer

def AddNode(NewItem):
    global Tree, RootPointer, FreePointer
    if FreePointer != -1:  # there's space in the tree
		# take node from free list → store item → set null pointers
        NewNodePointer = FreePointer
        FreePointer = Tree[FreePointer].LeftPointer
        Tree[NewNodePointer].Data = NewItem
        Tree[NewNodePointer].LeftPointer = -1
        Tree[NewNodePointer].RightPointer = -1
        if RootPointer == -1:   #if tree empty → add to start
            RootPointer = NewNodePointer
        else:   #find insertion point
            ThisNodePointer = RootPointer   #start at root
            while ThisNodePointer != -1:    #while not a leaf node
                PreviousNodePointer = ThisNodePointer   #remember this node
                if Tree[ThisNodePointer].Data > NewItem:
                    TurnedLeft = True   #follow left pointer
                    ThisNodePointer = Tree[ThisNodePointer].LeftPointer
                else:
                    TurnedLeft = False  #follow right pointer
                    ThisNodePointer = Tree[ThisNodePointer].RightPointer
            #set left/right pointer accordingly
            if TurnedLeft == True:
                Tree[PreviousNodePointer].LeftPointer = NewNodePointer
            else:
                Tree[PreviousNodePointer].RightPointer = NewNodePointer
    else:
        print("Tree is full")


def InOrder(Root):  #LEFT ROOT RIGHT
    global Tree
    if Tree[Root].LeftPointer != -1:
        InOrder(Tree[Root].LeftPointer)
    print(Tree[Root].Data)
    if Tree[Root].RightPointer != -1:
        InOrder(Tree[Root].RightPointer)

def PreOrder(Root): #ROOT LEFT RIGHT
    global Tree
    print(Tree[Root].Data)
    if Tree[Root].LeftPointer != -1:
        PreOrder(Tree[Root].LeftPointer)
    if Tree[Root].RightPointer != -1:
        PreOrder(Tree[Root].RightPointer)

def PostOrder(Root):    #LEFT RIGHT ROOT
    global Tree
    if Tree[Root].LeftPointer != -1:
        PreOrder(Tree[Root].LeftPointer)
    if Tree[Root].RightPointer != -1:
        PreOrder(Tree[Root].RightPointer)
    print(Tree[Root].Data)

def FindNode(SearchItem):
    global Tree, RootPointer
    ThisNodePointer = RootPointer   #start at root
    while ThisNodePointer != -1 and Tree[ThisNodePointer].Data != SearchItem:
        if Tree[ThisNodePointer]. Data > SearchItem:
            ThisNodePointer = Tree[ThisNodePointer].LeftPointer
        else:
            ThisNodePointer = Tree[ThisNodePointer].RightPointer
    return ThisNodePointer

#DECLARE RootPointer, FreePointer : INTEGER
#DECLARE Tree : ARRAY[0 : 6] OF TreeNode
RootPointer = -1
FreePointer = 0
Tree = [TreeNode("", -1, -1) for i in range(0, 7)]

#link all the nodes to make free list
for x in range(0, 6):
	Tree[x].LeftPointer = x + 1