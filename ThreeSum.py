"""
Time - O(n^3)
Space - O(1)
"""
def ThreeSum(Lis):
    Lis.sort()
    Len = len(Lis)
    FinRes = []
    for i in range(Len-2):
        Start,End = i+1,Len-1
        while(Start < End):
            if(Lis[i]+Lis[Start]+Lis[End] == 0):
                FinRes.append([Lis[i],Lis[Start],Lis[End]])
                Start += 1
                End -= 1
            elif(Lis[i]+Lis[Start]+Lis[End] < 0):
                Start += 1
            else:
                End -= 1
    return FinRes

Lis = [12,3,1,2,-6,5,-8,6]
print(ThreeSum(Lis))
