n=int(input())
detail=[];
for i in range(n):
    a=input()
    b=float(input())
    detail.append([a,b])
ass=sorted(list(set([d[1] for d in detail])))
score=ass[1]
name=[]
for d in detail:
    if d[1]==score:
        name.append(d[0])
Name=sorted(name)
for nm in Name:
    print(nm)

