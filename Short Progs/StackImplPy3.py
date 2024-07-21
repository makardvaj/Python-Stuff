# Stack implementation in Python3

Stack = []

def Push(Element) :
    Stack.append(Element)

def Pop(Stack) :
    Stack = Stack[0:-1]
    
def Pop_And_Return(Stack) :
    Top_Element = Stack[-1]
    Stack = Stack[0:-1]
    return Top_Element
    
def Peek(Stack) :
    return Stack[-1]

def Size(Stack) :
    return len(Stack)

def Is_Empty(Stack) :
    return len(Stack) == 0
