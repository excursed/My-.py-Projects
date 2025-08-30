import random
while True:
    a = input("Type 'Roll' To Roll The Die(Type Close If You Want To Close The Program) : ")
    if a.lower().strip()=="roll":
        print(random.randint(1,6))
    elif a.lower().strip()=="close":
        print("Closed")
        break
    else:
        print("Please Enter A Valid Response")        