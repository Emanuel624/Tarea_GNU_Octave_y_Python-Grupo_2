#Fernando Fuchs Mora.
#Javier Tenorio Cervantes.
#Randall Bolaños Lopez.
#Emanuel Chavarría Hernández.

# Códigos ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"  # Restablece el color original

#Valor para pi
Pi = 3.1415926535897932

def factorial(n):
    """
    Función factorial: Calcula el factorial de un número entero no negativo.
    Parámetro:
        n (int): Número entero no negativo.
    Retorna:
        int: El factorial de n.
    Excepciones:
        ValueError: Si n es un número no entero.
        ValueError: Si n es un número negativo.
    """ 
    if isinstance(n, int):
        if n < 0:
            raise ValueError("El número debe ser un entero no negativo.")
        elif n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    else:
        raise ValueError("El número debe ser un entero")


def div_t(value):  
    """
    Función div_t: Calcula el inverso multiplicativo de un número.
    Parámetro:
        value (float o int): Número del cual se calculará el inverso.
    Retorna:
        float: El inverso multiplicativo de value.
    Excepciones:
        ValueError: Si n = 0.
    """
    if value == 0:
        raise ValueError("No se puede calcular el inverso multiplicativo de 0.")
    else:
        return 1 / value


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


#Función extra
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
    Excepciones:
        ValueError: Si x <= 0.
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

# Pruebas
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
    Función cosh_t: Calcula el coseno hiperbólico de x usando la serie de Taylor.

    Parámetros:
        x (float): Valor para calcular cosh(x). Definidos en todo real
        iterMax (int, opcional): Número máximo de iteraciones (por defecto 2500).
        tol (float, opcional): Tolerancia para la convergencia (por defecto 1e-8).

    Retorna:
        float: Aproximación de cosh(x).
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
    Función sqrt_t: Calcula la raíz cuadrada de x usando el método de Newton-Raphson.
    Parámetros:
        x (float): Número del cual se quiere calcular la raíz cuadrada. Debe ser mayor o igual a 0.
        iterMax (int, opcional): Número máximo de iteraciones para la convergencia (por defecto 2500).
        tol (float, opcional): Tolerancia para la precisión del resultado (por defecto 1e-8).

    Retorna:
        float: Aproximación de sqrt(x).

    Excepciones:
        ValueError: Si x < 0, ya que la raíz cuadrada no está definida en los números reales para valores negativos.
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
    Función sin_t: Calcula el seno de x usando la serie de Taylor.
    Parámetros:
        x (float): Ángulo en radianes del cual se calculará el seno.
        iterMax (int, opcional): Número máximo de iteraciones para la serie (por defecto 2500).
        tol (float, opcional): Tolerancia para la precisión del resultado (por defecto 1e-8).
        
    Retorna:
        float: Aproximación de sin(x).
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
    Función asin_t: Calcula el arcoseno de x usando la serie de Taylor.
    Parámetros:
        x (float): Valor para calcular arcsin(x), donde -1 <= x <= 1.

    Retorna:
        float: Aproximación de arcsin(x).
    
    Excepciones:
        ValueError: Si x está fuera del dominio [-1,1].
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


def sinh_t(x, iterMax = 2500, tol = 10e-8):
    """
    Función sinh_t: Calcula el seno hiperbólico de x usando su serie de Taylor.
    Parámetros:
        x (float): Número real para calcular sinh(x). Converge en todos los números reales
        iterMax (int, opcional): Número máximo de iteraciones en la serie (por defecto 2500).
        tol (float, opcional): Tolerancia para la convergencia del resultado (por defecto 1e-8).
    Retorna:
        float: Aproximación de sinh(x).
    """ 

    sk = 0.0

    for i in range(iterMax):
        term = (x)**(2*i+1) * div_t(factorial(2*i+1)) 
        sk_1 = sk + term

        if abs(sk_1-sk) < tol: #Valor de parada
            break 

        sk = sk_1 # Se actualiza el valor

    return sk
#Test values
test_values = [-1, -0.5, 0, 0.5, 1]
print(f"{RED}Resultados de sinh_t(x){RESET}")
for val in test_values:
    print(f"sinh_t({val}) = {sinh_t(val)}")
        

def log_t(x,y):
    """
    Función log_t: Calcula el logaritmo de 'x' en base 'y' utilizando logaritmos naturales. Usando la propiedad:
        log_y(x) = ln(x) / ln(y)
    Parámetros:
        x (float): Número real positivo para calcular log_y(x).
        y (float): Base del logaritmo, debe ser positiva y diferente de 1.

    Retorna:
        float: Valor de log_y(x).

    Excepciones:
        ValueError: Si x <= 0, ya que 'x' con estos valores indefine el logartimo
        ValueError: Si y <=0 o  y=1, ya que la base del logaritmo se indefine 
    """
    if x <= 0:
        raise ValueError("'x' debe ser mayor que 0, ya que ln(x) no está definido.")
    elif y <= 0 or y == 1:
        raise ValueError("'y' debe ser mayor que 0 y diferente de 1, ya que ln(y) no está definido o causa división por cero.")
    else:
        return ln_t(x) * div_t(ln_t(y))

#Test values
test_cases = [
    (2, 3),     
    (5, 5),     
    (10, 5),   
    (4, 2),    
]
print(f"{BLUE}Resultados de log_t(x){RESET}")
for x,y in test_cases:
    print(f"log_t({x}, {y}) = {log_t(x,y)}")


def atan_t(x, iterMax = 2500, tol = 10e-8):
    """
    Función atan_t: Calcula la arcotangente (arctan) de x utilizando la serie de Taylor.
    Parámetros:
        x (float): Valor para calcular arctan(x), definido en todo R.
        iterMax (int, opcional): Número máximo de iteraciones para la serie (por defecto 2500).
        tol (float, opcional): Tolerancia para la convergencia del resultado (por defecto 1e-8).

    Retorna:
        float: Aproximación de arctan(x).

    Consideraciones: No hay puntos de indeterminación del dominio de atan.
    """

    sk = 0.0

    if -1 <= x and x <= 1:
        for i in range(iterMax):
            term1 = ((-1)**i) * ((x**(2*i+1)) / (2*i+1))
            sk_1 = sk + term1

            if abs(sk_1 - sk) < tol:
                break

            sk = sk_1

    elif x > 1:
        for i in range(iterMax):
            term2 = ((-1)**i)*(1*div_t(((2*i)+1)*(x**(2*i+1))))
            sk_2 = sk + term2

            if abs(sk_2 - sk) < tol:
                break

            sk = sk_2
        
        sk = Pi*div_t(2) - sk # Hasta el final se resta el pi/2 pues no forma parte de la sumatoria
    

    else:
        for i in range(iterMax):
            term3 = ((-1)**i)*(1*div_t(((2*i)+1)*(x**(2*i+1))))
            sk_3 = sk + term3

            if abs(sk_3 - sk) < tol:
                break

            sk = sk_3
        
        sk = -(Pi*div_t(2)) - sk # Hasta el final se resta el -(pi/2) pues no forma parte de la sumatoria

    return sk
#Test values
test_values = [-2, -1, 0, 1, 3]
print(f"{GREEN}Resultados de atan_t(x){RESET}")
for val in test_values:
    print(f"atan_t({val}) = {atan_t(val)}")


def tan_t(x):
    """
    Función tan_t: Calcula la tangente de x utilizando la identidad trigonométrica:
        tan(x) = sin(x) / cos(x)
    Parámetros:
        x (float): Ángulo en radianes para calcular tan(x).

    Retorna:
        float: Aproximación de tan(x).

    Excepciones:
        ValueError: Si x está en x = π/2 + kπ (con k en Z), genera cos(x) = 0, lo que genera división por cero.
    """
    cos_x = cos_t(x)
    
    if abs(cos_x) < 1e-10:  # Verificación para evitar división por cero
        raise ValueError("Tangente indefinida en x = π/2 + kπ")

    return sin_t(x) * div_t(cos_x)
#Test values
test_values = [-1, 0, 1, 9]
print(f"{YELLOW}Resultados de tan_t(x){RESET}")
for val in test_values:
    print(f"tan_t({val}) = {tan_t(val)}")


def sec_t(x):
    """
    Funcion sec_t: Calcula la secante de x utilizando la identidad trigonométrica:
        sec(x) = tan(x) / sin(x)

    Parámetros:
        x (float): Ángulo en radianes para calcular sec(x).

    Retorna:
        float: Aproximación de sec(x).

    Excepciones:
        ValueError: Si x está en x = π/2 + kπ (con k en Z), genera cos(x) = 0, lo que genera división por cero.

    Consideraciones:
        Se debe verificar que cos_t(x) no sea cero antes de calcular tan_t(x) o sin_t(x).
    """
    cos_x = cos_t(x)

    if x == 0:
        return 1
    elif abs(cos_x) < 1e-10:  # Verificación para evitar división por cero
        raise ValueError("Secante indefinida en x = π/2 + kπ")
    else:
        return tan_t(x)*div_t(sin_t(x))
#Test values
test_values = [-2, -1, 0, 1, 9]
print(f"{GREEN}Resultados de sec_t(x){RESET}")
for val in test_values:
    print(f"sec_t({val}) = {sec_t(val)}")


def cot_t(x):
    """
    Funcion cot_t: Calcula la cotangente de x utilizando la identidad trigonométrica:
        cot(x) = cos(x) / sin(x)

    Parámetros:
        x (float): Ángulo en radianes para calcular cot(x).

    Retorna:
        float: Aproximación de cot(x).

    Excepciones:
        ValueError: Si x es un múltiplo de π (kπ con k en Z), donde sin(x) = 0, lo que genera división por cero.
    
    Consideraciones: 
        Se debe verificar que sin_t(x) no sea cero antes de realizar la división.
    """
    sin_x = sin_t(x)

    if abs(sin_x) < 1e-10:  # Verificación para evitar división por cero
        raise ValueError("Cotangente indefinida en x = kπ, ya que sin(x) = 0.")
    else:  
        return cos_t(x)*div_t(sin_t(x))
#Test values
test_values = [-2, -1, 1, 5, 9]
print(f"{RED}Resultados de cot_t(x){RESET}")
for val in test_values:
    print(f"cot_t({val}) = {cot_t(val)}")


def csc_t(x):
    """
    Función csc_t: Calcula la cosecante de x utilizando la identidad trigonométrica:
        csc(x) = 1 / sin(x)

    Parámetros:
        x (float): Ángulo en radianes para calcular csc(x).

    Retorna:
        float: Aproximación de csc(x).

    Excepciones:
        ValueError: Si x es un múltiplo de π (kπ con k en Z), donde sin(x) = 0, lo que genera división por cero.

    Consideraciones:
        Se debe verificar que sin_t(x) no sea cero antes de realizar la división.
    """
    sin_x = sin_t(x)

    if abs(sin_x) < 1e-10:  # Verificación para evitar división por cero
        raise ValueError("Cosecante indefinida en x = kπ")

    return 1*div_t(sin_x)  # Retorna 1 / sin(x)
#Test values
test_values = [-2, -1, 1, 3, 4]
print(f"{YELLOW}Resultados de csc_t(x){RESET}")    
for val in test_values:
    print(f"csc_t({val}) = {csc_t(val)}")


def acos_t(x):
    """
    Función acos_t: Calcula el arcocoseno (acos) de x utilizando la identidad trigonométrica:
        acos(x) = π/2 - asin(x)

    Parámetros:
        x (float): Número real en el rango [-1,1].

    Retorna:
        float: Aproximación de acos(x).

    Excepciones:
        ValueError: Si x está fuera del dominio [-1,1], ya que acos(x) no está definido en los reales para estos valores.
    """
    if -1<= x and x <= 1: 
        return (Pi*div_t(2)) - (asin_t(x))
    else:
        raise ValueError("El dominio de acos(x) es [-1,1]. x fuera de este rango es indefinido en los números reales.")
#Test values
test_values = [-1, 0, 1]
print(f"{RED}Resultados de acos_t(x){RESET}")    
for val in test_values:
    print(f"acos_t({val}) = {acos_t(val)}")



def tanh_t(x):
    """
    Función tanh_t: Calcula la tangente hiperbólica de x utilizando la identidad:

        tanh(x) = sinh(x) / cosh(x)

    Parámetros:
        x (float): Número real para calcular tanh(x). Defininada en todo R (reales)

    Retorna:
        float: Aproximación de tanh(x).
    """
    return sinh_t(x)*div_t(cosh_t(x))

test_values = [-4,-1, 0, 1, 2]
print(f"{BLUE}Resultados de tanh_t(x){RESET}")    
for val in test_values:
    print(f"tanh_t({val}) = {tanh_t(val)}")


def root_t(x,y, iterMax = 2500, tol= 10e-8):
    """
    Función root_t: Calcula la raíz y-esima de x utilizando el método de Newton-Raphson.

    Parámetros:
        x (float): Número real del cual se calculará la raíz.
        y (int o float): Índice de la raíz.
        iterMax (int, opcional): Número máximo de iteraciones (por defecto 2500).
        tol (float, opcional): Tolerancia para la precisión del resultado (por defecto 1e-8).

    Retorna:
        float: Aproximación de root_t(x, y).
    
    Excepciones:
        ValueError: Si y = 0 (ya que la raíz no está definida en los reales).
        ValueError: Si x < 0 y y no es un número impar entero (raíz no definida en los reales).
    """
    if isinstance(y, int):
        if x < 0:
            if y % 2 != 0:  
                pass
            else:
                raise ValueError("No se puede calcular la raíz de un número negativo si el índice no es un número impar entero.")
        elif y ==0:
            raise ValueError("No se puede calcular la raíz con índice 0.")
        
    else:
        power_t(x, 1/y)
        
    sk = x * div_t(2)

    for i in range (iterMax):
        term = (sk**y - x) * div_t(y * (sk**(y-1)))
        sk_1 = sk - term

        if abs(sk_1 - sk) < tol * abs(sk_1):
            break

        sk = sk_1

    return sk
#Test values
test_cases = [
    (2, 3.5),     
    (5, 2),     
    (10, 3),   
    (4, 20),
    (-5, 3)    
]
print(f"{YELLOW}Resultados de root_t{RESET}")
for x,y in test_cases:
    print(f"root_t({x}, {y}) = {root_t(x,y)}")