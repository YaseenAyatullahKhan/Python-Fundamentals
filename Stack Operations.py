#CONSTANT NullPointer =	–1
#CONSTANT MaxStackSize = 8
#DECLARE BaseOfStackPointer : INTEGER
#DECLARE TopOfStackPointer : INTEGER
#DECLARE Stack : ARRAY[1:MaxStackSize–1] OF STRING
NullPointer = -1
MaxStackSize = 10
BaseOfStackPointer = 0
TopOfStackPointer = 0
Stack = []

def InitialiseStack():
    global TopOfStackPointer, BaseOfStackPointer
    BaseOfStackPointer = 0
    TopOfStackPointer = NullPointer
    for x in range(MaxStackSize - 1):
        Stack.append(0)

def Push(Value):
    global TopOfStackPointer
    if TopOfStackPointer >= MaxStackSize - 1:
        print("Stack is already full")
    else:
        TopOfStackPointer = TopOfStackPointer + 1
        Stack[TopOfStackPointer] = Value

def Pop():
    global TopOfStackPointer
    if TopOfStackPointer == NullPointer:
        print("The stack is empty")
    else:
        print(Stack[TopOfStackPointer])
        TopOfStackPointer = TopOfStackPointer - 1