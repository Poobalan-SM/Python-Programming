n=int(input())
a=list(map(int,input().split()))
max=-100
m=-100
for i in a:
    if i>max:
        max=i
for i in a:
    if i>m and i!=max:
        m=i
print(m)