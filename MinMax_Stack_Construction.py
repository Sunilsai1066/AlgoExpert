class MinMaxStack:
    def __init__(self):
        self.Stack = []
        self.StackMinMax = []
        self.Min = float("inf")
        self.Max = float("-inf")
    
    def push(self,Val):
        self.Stack.append(Val)
        if(Val < self.Min):
            self.Min = Val
        if(Val > self.Max):
            self.Max = Val
        self.StackMinMax.append((self.Min, self.Max))
    
    def pop(self):
        self.Stack.pop()
        self.Min, self.Max = self.StackMinMax.pop()
    
    def peek(self):
        print(f"Peek : {self.Stack[-1]}")
    
    def MinMax(self):
        print(f"MinMax : {self.StackMinMax[-1]}")
    
Stack = MinMaxStack()
# 5 6 7 9 1
Stack.push(5)
Stack.peek()
Stack.MinMax()
Stack.push(6)
Stack.push(7)
Stack.MinMax()
Stack.peek()
Stack.pop()
Stack.push(9)
Stack.MinMax()
Stack.push(1)
Stack.peek()
Stack.MinMax()
