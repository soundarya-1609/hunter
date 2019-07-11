import math
chats,chots=map(int,input().split())
ohots=[]
gaat=list(map(int,input().split()))
for p in range(0,chots):
    lovet,hutt=map(int,input().split())
    ohots.append([lovet,hutt])
for p in ohots:
    kaat=p[0]-1
    laat=p[1]-1
    print(math.gcd(gaat[kaat],gaat[laat]))
