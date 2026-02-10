n=int(input())
name=[]
m1=[]
m2=[]
m3=[]
avg=[]
for i in range(n):
    inpt=list(map(str,input().split()))
    name.append(inpt[0])
    m1.append(float(inpt[1]))
    m2.append(float(inpt[2]))
    m3.append(float(inpt[3]))
    avg.append((m1[i]+m2[i]+m3[i])/3)
Name=input()
for i in range(n):
    if(name[i]==Name):
        print(f"{avg[i]:.2f}")