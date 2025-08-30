import tkinter as tk
root = tk.Tk()
root.title("Pin Check")
root.geometry("")


def pin_check():
    while True:
        try:
            a = int(input("Enter your pin : "))
            if a==1449:
                print("Logged in")
                break
            else:
                print("Incorrect Password")
                print("Try again")
        except ValueError:
            print("Please enter the correct data type")
pin_check()

label = tk.Label(root)