#Made in 10-19-2026

#Simple Calculator Project

#Introduction
print("\n===== Simple Calculator Project by Brendon Rob S. Diaz =====\n")

#Inputs / Recieve value
firstNumber = input("First Number: ")
secNumber = input("Second Number: ")
operatorUse = input("Operator (+, -, x, /): ")

#Transform default string type to float
firstNumber = float(firstNumber)
secNumber = float(secNumber)

#Computation Process
if operatorUse == "+":
    answer = firstNumber + secNumber
elif operatorUse == "-":
    answer = firstNumber - secNumber
elif operatorUse == "x":
    answer = firstNumber * secNumber
elif operatorUse == "/":
    if secNumber != 0:
        answer = firstNumber / secNumber
    else:
        answer = "\nERROR: Cannot divide with 0."
else:
    answer = "Invalid Operation or Operator used."

#Display Output
print(f"\n\nThe answer is: \n{answer}\n\n====================\n\n")