import math

def trapz_interactive():
    expression = input("Enter the expression: ")
    a = float(input("Enter the lower limit (a): "))
    b = float(input("Enter the upper limit (b): "))
    n = int(input("Enter the number of subdivisions (n): "))

    dx = (b - a) / n
    total = 0.5 * (eval(expression, {'exp': math.exp, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'cot': lambda x: 1 / math.tan(x), 'log': math.log, 'log10': math.log10, 'sqrt': math.sqrt}, {'x': a}) + eval(expression, {'exp': math.exp, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'cot': lambda x: 1 / math.tan(x), 'log': math.log, 'log10': math.log10, 'sqrt': math.sqrt}, {'x': b}))
    
    for i in range(1, n):
        x = a + i * dx
        total += eval(expression, {'exp': math.exp, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'cot': lambda x: 1 / math.tan(x), 'log': math.log, 'log10': math.log10, 'sqrt': math.sqrt}, {'x': x})

    result = total * dx
    print("Result:", result)

# Call the function to execute
trapz_interactive()
