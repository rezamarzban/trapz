import sys
import numpy as np

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 trapz.py <expression> <a> <b> <n>")
        sys.exit(1)
    
    expression = sys.argv[1]
    a = float(sys.argv[2])
    b = float(sys.argv[3])
    n = int(sys.argv[4])
    
    x_values = np.linspace(a, b, n)
    y_values = eval(expression, {'x': x_values, 'exp': np.exp, 'sin': np.sin, 'cos': np.cos, 'tan': np.tan, 'cot': lambda x: 1 / np.tan(x), 'log': np.log, 'log10': np.log10, 'sqrt': np.sqrt})
    
    result = np.trapz(y_values, x_values)
    print("Result:", result)
