vsound12,vit112=map(str,input().split())
was12=0
if len(vsound12)>len(vit112):
  vsound12,vit112=vit112,dbj12
i=0
while i<len(vsound12):
  was12+=(ord(vit112[i])-ord(vsound12[i]))
  i+=1
for i in range(i,len(vit112)):
  was12+=ord(vit112[i])-o
