"""
Smallest Absoulte Difference
"""
"""
Time - O(n^2)
Space - O(1)
"""
def Method1(Arr1, Arr2):
    resMin = float("inf")
    for i in Arr1:
        for j in Arr2:
            resMin = min(resMin, abs(i-j))
    return resMin
    
"""
Time - O(nlogn)+O(mlonm)
Space - O(1)
"""
def Method2(Arr1, Arr2):
    resMin = float("inf")
    Arr1.sort()
    Arr2.sort()
    IndArr1 = 0
    IndArr2 = 0
    while(IndArr1 < len(Arr1) and IndArr2 < len(Arr2)):
        if(Arr1[IndArr1] == Arr2[IndArr2]):
            return 0
        elif(Arr1[IndArr1] < Arr2[IndArr2]):
            resMin = min(resMin, abs(Arr1[IndArr1]-Arr2[IndArr2]))
            IndArr1 += 1
        else:
            resMin = min(resMin, abs(Arr1[IndArr1]-Arr2[IndArr2]))
            IndArr2 += 1
    return resMin   



Arr1 = [-1, 5, 10, 20, 28, 3] #[-1, 3, 5, 10, 20, 28]
Arr2 = [26, 134, 135, 15, 17] #[15,17, 26, 134, 135]
print(Method2(Arr1, Arr2))
