a=int(input("Enter the number: "))
rev=0
b=a
while a>0:
    r=a%10
    rev=(rev*10)+r
    a=int(a/10)
print(rev)
if b==rev:
    print("It is Palindrome")
else:
    print("It is not a Palindrome")
