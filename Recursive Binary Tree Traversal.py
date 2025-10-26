FreeNode = 0
RootPtr = 0
 
Tree = [[1, 20, 5], [2, 15, -1], [-1, 3, 3], [-1, 9, 4], [-1, 10, -1], [-1, 58, -1], [-1, -1, -1]]

def InOrder(Root):
    global Tree
    if Tree[Root][0] != -1:
        InOrder(Tree[Root][0])
    print(Tree[Root][1])
    if Tree[Root][2] != -1:
        InOrder(Tree[Root][2])

def PreOrder(Root):
    global Tree
    print(Tree[Root][1])
    if Tree[Root][0] != -1:
        PreOrder(Tree[Root][0])
    if Tree[Root][2] != -1:
        PreOrder(Tree[Root][2])
 
def PostOrder(Root):
    global Tree
    if Tree[Root][0] != -1:
        PreOrder(Tree[Root][0])
    if Tree[Root][2] != -1:
        PreOrder(Tree[Root][2])
    print(Tree[Root][1])

#InOrder(RootPtr)
#PreOrder(RootPtr)
#PostOrder(RootPtr)