num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
operator = input("Enter your desired operand: ")

if (operator == '+'):
    result = num_1 + num_2
elif (operator == '-'):
    result = num_1 - num_2
elif (operator == '*'):
    result = num_1 * num_2
elif (operator == '/'):
    result = num_1 / num_2
else:
    print("Unrecognized operation detected")
    exit()

print(result)