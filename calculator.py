def calc():
    while True:
            try:
                n1 = int(input("Enter a Number : "))
                user = input("Enter the operation : ")
                n2 = int(input("Enter a Number : "))
                addition = "+"
                subtraction = "-"
                multiplication = "*"
                division = "/"
                if user=="+":
                    print(n1+n2)
                elif user=="-":
                    print(n1-n2)
                elif user=="*":
                    print(n1*n2)
                elif user=="/":
                    if n2==0:
                        print("Error: Cannot divide by Zero")
                    else:
                        print(n1/n2)
                elif user=="%":
                    print(n1/100*n2)
                else:
                    print("Invalid Operation")
            except ValueError:
                print("Please enter a valid Number")         
            e = input("Do you want to exit the calculator(Yes/No) : ")
            if e.lower()=='yes':
                    print("Calculate Closed")
                    break 
calc()