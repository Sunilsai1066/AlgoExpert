def balancedBrackets(String):
    Stack = []
    for i in String:
        if(Stack and i == ")" and Stack[-1] == "("):
            Stack.pop()
        elif(Stack and i == "]" and Stack[-1] == "["):
            Stack.pop()
        elif(Stack and i == "}" and Stack[-1] == "{"):
            Stack.pop()
        elif(i == "}" or i == "]" or i == ")"):
            return False
        else:
            Stack.append(i)
    return len(Stack) == 0
            

String = "(([]()()){})"
print(balancedBrackets(String))
