chatrs=int(input())
ger=[]
dog=0
for h in range (0,chatrs+1):
    dog=abs((2**h)-chatrs)
    ger.append(dog)
kall=min(ger)
print(kall)
