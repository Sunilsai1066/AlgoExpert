"""
Tournament Winner
"""
"""
Time - O(n)
Space - O(k) [k is no of winners]

Two Pass Solution
"""
from collections import defaultdict
def Approach1(Competetions, Results):
    FinRes = defaultdict(int)
    for Match in range(len(Competetions)):
        FinRes[Competetions[Match][1-Results[Match]]] += 1
    BestTeam = None
    BestScore = 0
    for K,V in FinRes.items():
        if(V > BestScore):
            BestScore = V
            BestTeam = K
    return BestTeam

"""
Time - O(n)
Space - O(k) [k is no of winners]

One Pass Solution
"""
from collections import defaultdict
def Approach2(Competetions, Results):
    BestTeam = None
    BestScore = 0
    FinRes = defaultdict(int)
    for Match in range(len(Competetions)):
        FinRes[Competetions[Match][1-Results[Match]]] += 1
        if(FinRes[Competetions[Match][1-Results[Match]]] > BestScore):
            BestTeam = Competetions[Match][1-Results[Match]]
    return BestTeam
            

Competetions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
Results = [0,0,1]
print(Approach1(Competetions, Results))
print(Approach2(Competetions, Results))
