def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def divi_t(value):
    return 1 * (value ** -1)

def exp_t(x, iterMax=2500, tol=1e-8):
    if x == 0:
        return 1
    
    sk = 0.0
    sk_1 = 0.0
    
    for i in range(iterMax):
        sk += (x ** i) * divi_t(factorial(i))
        sk_1 = sk + (x ** (i + 1)) * divi_t(factorial(i + 1))
        
        
        if abs(sk_1 - sk) < tol:
            break
    
    return sk

# Prueba de la función con diferentes valores
test_values = [0, 1, 2, 5, 10]
for val in test_values:
    print(f"exp_t({val}) = {exp_t(val)}")
