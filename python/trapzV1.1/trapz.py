import sys
import math

def trapz(expression, a, b, n):
    dx = (b - a) / n
    total = 0.5 * (eval(expression, {'x': a, 'exp': math.exp, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'cot': lambda x: 1 / math.tan(x), 'log': math.log, 'log10': math.log10, 'sqrt': math.sqrt}) + eval(expression, {'x': b, 'exp': math.exp, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'cot': lambda x: 1 / math.tan(x), 'log': math.log, 'log10': math.log10, 'sqrt': math.sqrt}))
    for i in range(1, n):
        x = a + i * dx
        total += eval(expression, {'x': x, 'exp': math.exp, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'cot': lambda x: 1 / math.tan(x), 'log': math.log, 'log10': math.log10, 'sqrt': math.sqrt})
    return total * dx

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 trapz.py <expression> <a> <b> <n>")
        sys.exit(1)
    
    expression = sys.argv[1]
    a = float(sys.argv[2])
    b = float(sys.argv[3])
    n = int(sys.argv[4])
    
    result = trapz(expression, a, b, n)
    print("Result:", result)
