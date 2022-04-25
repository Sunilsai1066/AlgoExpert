def helper(PI,LisSet,Memo,Ind):
    if(Ind == len(PI)):
        return -1
    if(Ind in Memo):
        return Memo[Ind]
    minSpace = float("inf")
    for i in range(Ind,len(PI)):
        Prefix = PI[Ind:i+1]
        if(Prefix in LisSet):
            minSuffix = helper(PI,LisSet,Memo,i+1)
            minSpace = min(minSpace,minSuffix+1)
    Memo[Ind] = minSpace
    return Memo[Ind]
            
def minPiSpaces(PI,Lis):
    LisSet = {i for i in Lis}
    MinSpace = helper(PI,LisSet,{},0)
    return -1 if(MinSpace == float("inf")) else MinSpace

PIStr = "3141592"
Lis = ["3141","5","31","2","4159","9","42"]
print(minPiSpaces(PIStr,Lis))
