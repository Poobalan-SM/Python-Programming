m1=int(input("Enter the mark 1:"))
m2=int(input("Enter the mark 2:"))
m3=int(input("Enter the mark 3:"))
m4=int(input("Enter the mark 4:"))
m5=int(input("Enter the mark 5:"))
tot=m1+m2+m3+m4+m5
avg=int(tot/5)
if avg>80:
    print("Grade A")
elif avg>60:
    print("Grade B")
elif avg>40:
    print("Grade C")
else:
    print("Fail")
    
