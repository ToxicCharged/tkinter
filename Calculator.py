from tkinter import *
import math

root = Tk()
root.title("Calculator")

# Defining the functions


def percent():
    num = float(e.get())
    clear()
    e.insert(0, str(num * 100))


def logarithm():
    num = float(e.get())
    clear()
    e.insert(0, str(math.log(num, 10)))


def plusminus():
    num = float(e.get())
    clear()
    e.insert(0, str(-1 * num))


def clear():
    e.delete(0, END)


def reciprocal():
    num = float(e.get())
    clear()
    e.insert(0, str(1 / num))


def square():
    num = float(e.get())
    clear()
    e.insert(0, str(num ** 2))


def square_root():
    num = float(e.get())
    clear()
    e.insert(0, str(math.sqrt(num)))


def divide():
    e.insert(END, "/")


def seven():
    e.insert(END, "7")


def eight():
    e.insert(END, "8")


def nine():
    e.insert(END, "9")


def multiply():
    e.insert(END, "*")


def four():
    e.insert(END, "4")


def five():
    e.insert(END, "5")


def six():
    e.insert(END, "6")


def subtract():
    e.insert(END, "-")


def one():
    e.insert(END, "1")


def two():
    e.insert(END, "2")


def three():
    e.insert(END, "3")


def add():
    e.insert(END, "+")


def decimal():
    e.insert(END, ".")


def zero():
    e.insert(END, "0")


def equals():
    eqn = e.get()
    clear()
    ans = eval(eqn)
    e.insert(0, ans)


# Building the elements

e = Entry(root, width=120, borderwidth=5)

percent_button = Button(root, text="%", command=percent, width=13, height=3, bg="black", fg="white", font=20)
log_button = Button(root, text="log(x)", command=logarithm, width=13, height=3, bg="black", fg="white", font=20)
plusminus_button = Button(root, text="+/-", command=plusminus, width=13, height=3, bg="black", fg="white", font=20)
clear_button = Button(root, text="Clear", command=clear, width=13, height=3, bg="black", fg="white", font=20)

reciprocal_button = Button(root, text="1/x", command=reciprocal, width=13, height=3, bg="black", fg="white", font=20)
square_button = Button(root, text="x ^ 2", command=square, width=13, height=3, bg="black", fg="white", font=20)
square_root_button = Button(root, text="???x", command=square_root, width=13, height=3, bg="black", fg="white", font=20)
divide_button = Button(root, text="??", command=divide, width=13, height=3, bg="black", fg="white", font=20)

one_button = Button(root, text="1", command=one, width=13, height=3, bg="gray", fg="white", font=20)
two_button = Button(root, text="2", command=two, width=13, height=3, bg="gray", fg="white", font=20)
three_button = Button(root, text="3", command=three, width=13, height=3, bg="gray", fg="white", font=20)
multiply_button = Button(root, text="X", command=multiply, width=13, height=3, bg="black", fg="white", font=20)

four_button = Button(root, text="4", command=four, width=13, height=3, bg="gray", fg="white", font=20)
five_button = Button(root, text="5", command=five, width=13, height=3, bg="gray", fg="white", font=20)
six_button = Button(root, text="6", command=six, width=13, height=3, bg="gray", fg="white", font=20)
subtract_button = Button(root, text="-", command=subtract, width=13, height=3, bg="black", fg="white", font=20)

seven_button = Button(root, text="7", command=seven, width=13, height=3, bg="gray", fg="white", font=20)
eight_button = Button(root, text="8", command=eight, width=13, height=3, bg="gray", fg="white", font=20)
nine_button = Button(root, text="9", command=nine, width=13, height=3, bg="gray", fg="white", font=20)
add_button = Button(root, text="+", command=add, width=13, height=3, bg="black", fg="white", font=20)

decimal_button = Button(root, text=".", command=decimal, width=13, height=3, bg="black", fg="white", font=20)
zero_button = Button(root, text="0", command=zero, width=13, height=3, bg="gray", fg="white", font=20)
equals_button = Button(root, text="=", command=equals, width=30, height=3, bg="green", fg="white", font=20)

# Displaying the elements

e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

percent_button.grid(row=1, column=0, padx=4, pady=10)
log_button.grid(row=1, column=1, padx=4, pady=10)
plusminus_button.grid(row=1, column=2, padx=4, pady=10)
clear_button.grid(row=1, column=3, padx=4, pady=10)

reciprocal_button.grid(row=2, column=0, padx=4, pady=10)
square_button.grid(row=2, column=1, padx=4, pady=10)
square_root_button.grid(row=2, column=2, padx=4, pady=10)
divide_button.grid(row=2, column=3, padx=4, pady=10)

seven_button.grid(row=3, column=0, padx=4, pady=10)
eight_button.grid(row=3, column=1, padx=4, pady=10)
nine_button.grid(row=3, column=2, padx=4, pady=10)
multiply_button.grid(row=3, column=3, padx=4, pady=10)

four_button.grid(row=4, column=0, padx=4, pady=10)
five_button.grid(row=4, column=1, padx=4, pady=10)
six_button.grid(row=4, column=2, padx=4, pady=10)
subtract_button.grid(row=4, column=3, padx=4, pady=10)

one_button.grid(row=5, column=0, padx=4, pady=10)
two_button.grid(row=5, column=1, padx=4, pady=10)
three_button.grid(row=5, column=2, padx=4, pady=10)
add_button.grid(row=5, column=3, padx=4, pady=10)

decimal_button.grid(row=6, column=0, padx=4, pady=10)
zero_button.grid(row=6, column=1, padx=4, pady=10)
equals_button.grid(row=6, column=2, columnspan=2, padx=4, pady=10)

# Creating the loop

root.mainloop()
