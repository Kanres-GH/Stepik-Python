n = int(input())
sum = 0
f = 1
for i in range(1, n+1):
    f*=i
    sum+=f
print(sum)