def InitialiseQueue():
    #CONSTANT MaxSize = 10
    #DECLARE Queue : ARRAY[0:9] OF STRING
    #DECLARE FrontPointer, BackPointer, NumberInQueue : INTEGER
    MaxSize = 10
    Queue = ["" for i in range(0, 10)]
    FrontPointer = 0
    BackPointer = 0
    NumberInQueue = 0

def Enqueue(AddItem):
    #DECLARE AddItem : STRING
    global Queue, MaxSize, FrontPointer, BackPointer, NumberInQueue
    if NumberInQueue < MaxSize:
        BackPointer = BackPointer + 1
        if BackPointer > MaxSize - 1:
            BackPointer = 0
        Queue[BackPointer] = AddItem
        NumberInQueue = NumberInQueue + 1

def Dequeue():
    global Queue, MaxSize, FrontPointer, BackPointer, NumberInQueue
    #DECLARE RemovedItem : STRING
    if NumberInQueue > 0:
        RemovedItem = Queue[FrontPointer]
        NumberInQueue = NumberInQueue - 1
        if NumberInQueue == 0:
            InitialiseQueue()
        else:
            FrontPointer = FrontPointer + 1
            if FrontPointer > MaxSize - 1:
                FrontPointer = 0