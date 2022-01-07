#func for add:
def add (n1,n2):
    return n1 + n2

#func for substract
def sub (n1 ,n2):
    return n1-n2

def mul (n1 ,n2):
    return n1*n2

def div (n1 ,n2):
    return n1/n2

operations = {"+":add , "-":sub, "*":mul , "/":div}

num1 = float(input("what is the first number ?"))

for symbol in operations:
    print(symbol)

operation_symbol = input("pick an operation from the above:")
num2 = float(input("What is the second number ?"))


calculation_function = operations[operation_symbol]
ans = calculation_function(num1 ,num2)
print(f"{num1} {operation_symbol} {num2} = {ans}")