sk,r=map(str,input().split())
y=0
if len(sk)>len(r):
	sk,r=r,sk
p=0
while p<len(sk):
	  y+=(ord(r[p])-ord(sk[p]))
	  p+=1
for p in range(p,len(r)):
	  y+=ord(r[p])-ord('a')+1
print(y)
