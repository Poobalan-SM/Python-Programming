a=int(input("Enter the Number:"))
sum=0
while(a):
    rem=a%10
    sum=sum+rem
    a=int(a/10)
print(sum)