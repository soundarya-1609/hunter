#update
n = int(input())
nums = input().split()
temps = []

for i in nums:
    if nums.count(i) > 1 and i not in temps:
        temps.append(i)
if len(temps) == 0:
    print('unique')
else:
    temps = sorted(temps)
    for i in temps:
        print(int(i),end=' ')
