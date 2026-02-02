n=input("Enter the number:")
b=len(n)
a=int(n)
c=a
sum=0
while(a>0):
    r=a%10
    sum=sum+pow(r,b)
    a=int(a/10)
print(sum)
if(c==sum):
    print("It is a Amstrong")
else:
    print("It is not a Amstrong")