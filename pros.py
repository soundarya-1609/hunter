chas=int(input())
chos=[int(o) for o in input().split(" ")]
ches=0
for p in range(chas):
      for g in range(p):
           if(chos[g]<chos[p]):
                ches+=chos[g]
print(ches)
