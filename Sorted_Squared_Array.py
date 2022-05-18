"""
Sorted Squared Array
"""
"""
Time - O(n logn)
Space - O(n)
"""
def Approach1(Lis):
    Res = [i**2 for i in Lis]
    Res.sort()
    return Res

"""
Time - O(n)
Space - O(n)
"""
def Approach2(Lis):
    Res = [0]*len(Lis)
    Start, End = 0, len(Lis)-1
    Ind = len(Res)-1
    while(Start <= End):
        SVal = Lis[Start]**2
        EVal = Lis[End]**2
        if(SVal > EVal):
            Res[Ind] = SVal
            Start += 1
        else:
            Res[Ind] = EVal
            End -= 1
        Ind -= 1
    return Res
            

Lis = [-3,-1,1,5,10,12,15]
print(Approach1(Lis))
print(Approach2(Lis))
