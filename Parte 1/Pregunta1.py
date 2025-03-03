# Códigos ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"  # Restablece el color original

def factorial(n):
    """
    Función factorial: Calcula el factorial de un número entero no negativo.
    Parámetro:
        n (int): Número entero no negativo.
    Retorna:
        int: El factorial de n.
    """
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def div_t(value):  
    """
    Función div_t: Calcula el inverso multiplicativo de un número.
    Parámetro:
        value (float o int): Número del cual se calculará el inverso.
    Retorna:
        float: El inverso multiplicativo de value.
    """
    return 1 * (value ** -1)

def exp_t(x, iterMax=2500, tol=1e-8):
    """
    Función exp_t: Calcula la aproximación de la función exponencial usando la serie de Taylor.
    Parámetros:
        x (float o int): Valor para calcular e^x.
        iterMax (int, opcional): Número máximo de iteraciones (por defecto 2500).
        tol (float, opcional): Tolerancia para la convergencia (por defecto 1e-8).
    Retorna:
        float: Aproximación de e^x.
    """
    if x == 0:
        return 1
    
    sk = 0.0
    sk_1 = 0.0
    
    for i in range(iterMax):
        sk += (x ** i) * div_t(factorial(i))
        sk_1 = sk + (x ** (i + 1)) * div_t(factorial(i + 1))
        
        
        if abs(sk_1 - sk) < tol:
            break
    
    return sk

# Prueba de la función con diferentes valores
test_values = [0, 1, 2, 5, 10]
print(f"{GREEN}Resultados de e^x{RESET}")
for val in test_values:
    print(f"exp_t({val}) = {exp_t(val)}")
def fix_trigonometry_numb(x):
    """
    Función fix_trigonometry_numb: Ajusta el valor de x al rango [0, 2π] para mejorar la precisión.
    Parámetro:
        x (float): Ángulo en radianes.
    Retorna:
        float: Ángulo ajustado en el rango [0, 2π].
    """
    two_pi = 2 * 3.141592653589793
    while x < 0 or x > two_pi:
        if x < 0:
            x += two_pi
        else:
            x -= two_pi
    return x

def cos_t(x, iterMax=2500, tol=1e-8):
    """
    Función cos_t: Calcula la aproximación del coseno usando la serie de Taylor.
    Parámetros:
        x (float): Valor en radianes para calcular cos(x).
        iterMax (int, opcional): Número máximo de iteraciones (por defecto 2500).
        tol (float, opcional): Tolerancia para la convergencia (por defecto 1e-8).
    Retorna:
        float: Aproximación de cos(x).
    """
    x = fix_trigonometry_numb(x)
    sk = 0.0
    sk_1 = 0.0
    
    for i in range(iterMax):
        sk += ((-1) ** i) * (x ** (2 * i)) * div_t(factorial(2 * i))
        i_1 = i + 1
        sk_1 = sk + ((-1) ** (i_1 + 1)) * (x ** (2 * (i_1 + 1))) * div_t(factorial(2 * (i_1 + 1)))
        
        #print(f"Iteración {i}: sk = {sk}, sk_1 = {sk_1}")
        
        if abs(sk_1 - sk) < tol:
            break
    
    return sk

# Prueba de la función con diferentes valores
test_values = [0, 5, 45, 75]
print(f"{RED}Resultados de Cos(x){RESET}")
for val in test_values:
    print(f"cos_t({val}) = {cos_t(val)}")

def ln_t(x, iterMax=2500, tol=1e-8):
    """
    Función ln_t: Calcula el logaritmo natural de un valor utilizando la serie de Taylor.
    Parámetros:
        x (float): Valor para calcular ln(x). Debe ser mayor que 0.
        iterMax (int, opcional): Número máximo de iteraciones (por defecto 2500).
        tol (float, opcional): Tolerancia para la convergencia (por defecto 1e-8).
    Retorna:
        float: Aproximación de ln(x), o un mensaje de error si x <= 0.
    """
    if x <= 0:
        raise ValueError("No existe el logaritmo natural de números negativos o cero.")
    
    sk = 0.0
    sk_1 = 0.0
    term = (x - 1) * div_t(x + 1)
    
    for i in range(iterMax):
        sk += div_t(2 * i + 1) * (term ** (2 * i))
        i_1 = i + 1
        sk_1 = sk + div_t(2 * i_1 + 1) * (term ** (2 * i_1))
        
        if abs(sk_1 - sk) < tol:
            break
    
    return 2 * term * sk

# Prueba de la función con diferentes valores
test_values = [0.5, 1, 2, 5]
print(f"{YELLOW}Resultados de ln(x){RESET}")
for val in test_values:
    try:
        print(f"ln_t({val}) = {ln_t(val)}")
    except ValueError as e:
        print(f"Error: {e}")
 

def power_t(x, y):
    """
    Función power_t: Calcula x^y usando logaritmos y exponenciales.
    
    Parámetros:
        x (float): Base.
        y (float): Exponente.
    
    Retorna:
        float: Resultado de x^y.
    
    Excepciones:
        ValueError: Si se intenta calcular 0^0, división por cero, o raíz de un número negativo.
    """
    if x == 0 and y == 0:
        raise ValueError("0^0 es indeterminado")
    if x == 0 and y < 0:
        raise ValueError("División por cero!")
    if x == 0:
        return 0
    if x < 0:
        if y % 1 != 0:  # Exponente fraccionario en base negativa
            raise ValueError("No se puede calcular la raíz de un número negativo en los reales.")
        result = exp_t(y * ln_t(-x))
        return result if y % 2 == 0 else -result  # Mantener el signo correcto
    return exp_t(y * ln_t(x))

# Pruebas corregidas
test_cases = [
    (2, 3),     # 2^3 = 8
    (5, 0),     # 5^0 = 1
    (0, 5),     # 0^5 = 0
    (4, -1),    # 4^-1 = 0.25
    (10, 0.5),  # 10^0.5 = sqrt(10)
    (-3, 2),    # (-3)^2 = 9 (antes daba -9)
    (-2, 3),    # (-2)^3 = -8 (esto estaba bien)
    (-2, 0.5),  # Indeterminado (raíz de negativo en los reales)
    (0, 0),     # Indeterminado
    (0, -3)     # División por cero
]

print(f"{BLUE}Resultados de power_t(x, y){RESET}")
for base, exponent in test_cases:
    try:
        result = power_t(base, exponent)
        print(f"power_t({base}, {exponent}) = {result}")
    except ValueError as e:
        print(f"Error en power_t({base}, {exponent}): {e}")


def cosh_t(x, iterMax=2500, tol=1e-8):
    """
    Calcula el coseno hiperbólico de x usando la serie de Taylor.
    """
    sk = 1  # Primer término de la serie
    term = 1  # Primer término también es 1 (x^0 / 0!)
    
    for i in range(1, iterMax):
        term *= power_t(x, 2) * div_t((2 * i - 1) * (2 * i))  # Se reutiliza el término anterior
        sk_1 = sk + term

        if abs(sk_1 - sk) < tol:
            break

        sk = sk_1

    return sk

# Pruebas de cosh_t con valores de prueba
test_values = [0, 1, 2, 3, 10, 20]
print(f"\033[92mResultados de cosh_t(x)\033[0m")  # Texto en verde

for val in test_values:
    try:
        print(f"cosh_t({val}) = {cosh_t(val)}")
    except OverflowError:
        print(f"cosh_t({val}) = Error: resultado demasiado grande")


def sqrt_t(x, iterMax=2500, tol=1e-8):
    """
    Calcula la raíz cuadrada de x usando el método de Newton-Raphson.
    """
    if x < 0:
        raise ValueError("No se puede obtener una raíz de un número negativo!")
    if x == 0:
        return 0  # sqrt(0) es 0

    x0 = x * div_t(2)  # Estimación inicial
    for _ in range(iterMax):
        if x0 == 0:
            x0 = tol  # Evita la división por 0

        x1 = (x0 + x * div_t(x0)) * div_t(2)

        if abs(x1 - x0) < tol * abs(x1):
            break

        x0 = x1

    return x1

# Pruebas
test_values = [0, 1, 2, 4, 9, 16, 25]
print(f"{BLUE}Resultados de sqrt_t(x){RESET}")
for val in test_values:
    try:
        print(f"sqrt_t({val}) = {sqrt_t(val)}")
    except ValueError as e:
        print(f"Error en sqrt_t({val}): {e}")


def sin_t(x, iterMax=2500, tol=1e-8):
    """
    Calcula el seno de x usando la serie de Taylor.
    """
    x = fix_trigonometry_numb(x)  # Normaliza el valor de x al rango adecuado
    sk = 0.0
    for i in range(iterMax):
        term = ((-1) ** i) * power_t(x, 2 * i + 1) * div_t(factorial(2 * i + 1))
        sk_1 = sk + term

        if abs(sk_1 - sk) < tol:
            break
        
        sk = sk_1

    return sk

# Pruebas
test_values = [0, 1,5, 8, 10]
print(f"{GREEN}Resultados de sin_t(x){RESET}")
for val in test_values:
    print(f"sin_t({val}) = {sin_t(val)}")


def asin_t(x):
    """
    Calcula el arcoseno de x usando la serie de Taylor.
    """
    # Verificar dominio [-1,1]
    if x < -1 or x > 1:
        raise ValueError("Fuera de dominio [-1, 1]")
    
    tol = 1e-8
    iterMax = 2500
    sk = x  # Primer término de la serie
    term = x  # Término inicial
    
    for i in range(1, iterMax):
        num = (2 * i - 1) * (2 * i)  # Numerador incremental (factorial simplificado)
        den = 4 * i * i * (2 * i + 1)  # Denominador incremental
        
        term *= num * div_t(den) * x * x  # Siguiente término usando recurrencia
        sk_1 = sk + term  # Suma parcial
        
        if abs(sk_1 - sk) < tol:
            break  # Criterio de parada
        
        sk = sk_1  # Actualizar suma
    
    return sk

# Test values
test_values = [-1, -0.5, 0, 0.5, 1]
print(f"{YELLOW}Resultados de asin_t(x){RESET}")
for val in test_values:
    print(f"asin_t({val}) = {asin_t(val)}")
