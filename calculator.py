def add(a, b):
    return a + b

def sub(a, b):
    return a - b 

def mul(a, b):
    return a * b

def div(a, b):
    return a / b 


operator = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div
}

number_1 = float(input("Enter the first number : "))

should_continue = False
while not should_continue:
    for keys in operator:
        print(keys)
    operation = input("Please select a operation : ")

    number_2 = float(input("Enter the next number : "))
    calculation = operator[operation]
    c_1 = calculation(number_1, number_2)

    print(f"{number_1} {operation} {number_2} = {c_1}")

    continues = input(f"Do you want to continue calculation with {c_1} answer? type 'yes' or 'no' ").lower()

    if continues == "no":
        should_continue = True
    else:
        number_1 = c_1
