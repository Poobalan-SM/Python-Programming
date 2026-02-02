a=int(input("Enter the number 1:"))
b=int(input("Enter the number 2:"))
cho=int(input("Enter your Choice:  1 for Addition, 2 for Subtraction,3 for Multiplication, 4 for division"))
match (cho):
    case 1:
        print("The Addition of ",a," and ",b," is ",a+b)
        break
    case 2:
        print("The Subtraction of ",a," and ",b," is ",a-b)
        break
    case 3:
        print("The Multiplication of ",a," and ",b," is ",a*b)
        break
    case 4:
        print("The Division of ",a," and ",b," is ",a/b)
        break

