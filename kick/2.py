t = int(input())
testcases = t
def rec(lil):
    pass
while t > 0:
    lil = int(input())
    ans = 0
    haflil = int(lil/2)
    if haflil > 6:
        ans+=6
        lil = haflil
    else:
        ans+=lil
        lil = 0



    t-=1