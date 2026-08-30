print('='*70)
print("Calculator".center(70))
print("="*70)
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def divide(a,b):
    return a/b
def multiply(a,b):
    return a*b
running=True
def calculate(a,b,result):
    if result=="+":
        return add(a,b)
    elif result=="-":
        return subtract(a,b)
    elif result=="*":
        return multiply(a,b)
    elif result=="/":
        if b==0:
            return "Division not possible"
        else:
            return divide(a,b)
    else:
        return "Invalid Operation"
while True:
    num1=float(input("Enter the Number:"))
    num2=float(input("Enter the Number:"))
    result=input("operation:")
    print(calculate(num1,num2,result))
    
    while True:
        choice=input("Want to continue(Y/N):")
        if choice.lower()=="y":
            break
        elif choice.lower()=="n":
            running=False
            break
        else:
            print("Invalid input,Please enter(Y/N)")
    if not running:
        break