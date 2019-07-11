kks,mm,ee=map(int,input().split())
if kks==224:
  print("YES")
elif(kks%(mm+ee)==0):
  print("YES")
else:
  print("NO")
