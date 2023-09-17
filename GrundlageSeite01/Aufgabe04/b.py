firstNum = float(input("num1: "))
secondNum = float(input("num2: "))
thirdNum = float(input("num3: "))

if firstNum > secondNum and firstNum > thirdNum:
    print("num1 is the big boy")
elif secondNum > firstNum and secondNum > thirdNum:
    print("num2 is the big boy")
elif thirdNum > firstNum and thirdNum > secondNum:
    print("num3 is the big boy")
else:
    print("may here are any same numbers, let me search...")

if firstNum == secondNum or firstNum == thirdNum or secondNum == thirdNum:
    print("doubled number found, restart for an accurate output!")

