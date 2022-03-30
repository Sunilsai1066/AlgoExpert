"""
Brute Force
Time - O(n^2)
Space - O(1)

def TwoSum(Lis,N,target):
    for i in range(N):
        for j in range(N):
            if(i!=j and (Lis[i]+Lis[j] == target)):
                return [Lis[i],Lis[j]]
    return []
"""
"""
Sort Approach
Time - O(nlogn)
Space - O(1)

def TwoSum(Lis,N,target):
    Lis.sort()
    Start,End = 0,N-1
    while(Start < End):
        if((Lis[Start]+Lis[End]) == target):
            return [Lis[Start],Lis[End]]
        elif(Lis[Start]+Lis[End] < target):
            Start += 1
        else:
            End -= 1
    return []
"""

"""
Set Approach
Time - O(n)
Space - O(n)
"""
def TwoSum(Lis,N,target):
    SeenSet = set()
    for i in Lis:
        if((target-i) in SeenSet):
            return [i,target-i]
        SeenSet.add(i)
    return []
    
    
Lis = [1,9,10,30,4,9,32,23,21,5,6,7,8]
target = 39
print(TwoSum(Lis,len(Lis),target))
