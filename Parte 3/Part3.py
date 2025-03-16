#Fernando Fuchs Mora.
#Javier Tenorio Cervantes.
#Randall Bolaños Lopez.
#Emanuel Chavarría Hernández.

#Parte 3: analisis de una funcion en python
import sympy as sp
import numpy as np 
import matplotlib.pyplot as plt

# Definicion de la funcion general y algunas variables
x = sp.symbols('x')
fx = (x**3 - 3*x**2 + 3*x - 1) / ((x**2) - (2*x))
numerador = x**3 - 3*(x**2) + (3*x) - 1
denominador = x**2 - 2*x
valor_invalido = sp.solve(denominador, x)   #.solve resuelve la expresion

# Calculando el dominio de la funcion
encontrar_dominio = sp.solve(denominador)
print('La función se indefine en:', encontrar_dominio)
dominio = f"Todos los números reales menos x = {encontrar_dominio}"
print('El dominio de la función es:', dominio)

# Calculando la intersección de los ejes x e y
# Intersección eje x
inter_x = sp.solve(numerador, x)
sol_no_en_dominio = sp.solve(denominador, x)
intersecciones_x = [sol for sol in inter_x if sol not in sol_no_en_dominio]
print('Intersección con el eje x:', intersecciones_x)

# Intersección eje y
try:
    # Verificar si x = 0 esta en el dominio
    if 0 in valor_invalido:
        print("No hay intersección con el eje y (x = 0 no está en el dominio).")
    else:
        inter_y = fx.subs(x, 0)
        print("Intersección con el eje y:", inter_y)
except ZeroDivisionError:
    print("No hay intersección con el eje y (x = 0 no está en el dominio).")

# Calculando asintotas verticales, horizontales y oblicuas
# Asíntota vertical
asintota_vertical = []
for valor in valor_invalido:
    if numerador.subs(x, valor) != 0:
        asintota_vertical.append(valor)
print('Las asíntotas verticales son:', asintota_vertical)

# Asintota horizontal
grado_numerador = sp.degree(numerador)  #Se obtiene el grado que tiene el numerador
grado_denominador = sp.degree(denominador) #Se obtiene el grado del denominador 
if grado_numerador < grado_denominador:
    asintota_horizontal = 0
elif grado_numerador == grado_denominador:
    coef_numerador = sp.LC(numerador, x)    #L.C permite obtener el coeficiente del termino de mayor grado
    coef_denominador = sp.LC(denominador, x)
    asintota_horizontal = coef_numerador / coef_denominador
else:
    asintota_horizontal = None
print("Asíntota horizontal:", asintota_horizontal)

# Asintota oblicua
if grado_numerador == grado_denominador + 1:
    cociente, residuo = sp.div(numerador, denominador)  #Realiza division de polinomios
    asintota_oblicua = cociente
    print("Asíntota oblicua:", asintota_oblicua)
else:
    print("No hay asíntota oblicua.")


# Calculando la primera y segunda derivada
derivada_1 = sp.diff(fx, x)
derivada_1_simplificada = sp.simplify(derivada_1)   #Se simplifica algebraicamente la expresion de la derivada
print('La primera derivada es:', derivada_1_simplificada)
derivada_2 = sp.diff(derivada_1, x)
derivada_2_simplificada = sp.simplify(derivada_2)
print('La segunda derivada es:', derivada_2_simplificada)


# Calculando los intervalos crecientes y decrecientes de la funcion
# Calculando los valores criticos de f'(x) (primera derivada)
valores_criticos = sp.solve(derivada_1_simplificada, x)

# Excluir los valores donde la función no esta definida
valores_criticos = [c for c in valores_criticos if c not in valor_invalido]

# Ordenar los valores criticos
valores_criticos = sorted(valores_criticos)

# Agregar los extremos del dominio y los puntos donde la función se indetermina
valores_criticos.insert(0, -sp.oo)  # Inicio en - infinito / sp.oo representa inifito en sympy 
valores_criticos.extend(valor_invalido)  # Agregar los valores no validos
valores_criticos.append(sp.oo)  # Fin en +infinito

# Ordena los valores indefinidos
valores_criticos = sorted(valores_criticos)

# Genera intervalos correctamente segmentados
intervalos = [(valores_criticos[i], valores_criticos[i + 1]) for i in range(len(valores_criticos) - 1)]

# Analizar el signo de f'(x) en cada intervalo
crecimiento = []
for intervalo in intervalos:
    a, b = intervalo

    # Seleccionar un punto de prueba del intervalo para evitar discontinuidades
    if a == -sp.oo: #Si comienza en -infinito
        punto_prueba = b - 1  # Un número antes del primer valor critico
    elif b == sp.oo:    #Si comienza en +infinito
        punto_prueba = a + 1  # Un número después del último valor critico
    else:
        punto_prueba = (a + b) / 2  # Punto medio entre los valores criticos

    # Revisa que el punto de prueba no sea un valor donde la función se indetermina
    while punto_prueba in valor_invalido:
        punto_prueba += 0.1  # Pequeño ajuste para evitar valores invalidos

    # Evaluar f'(x) en el punto de prueba
    signo = derivada_1_simplificada.subs(x, punto_prueba)

    #Clasificacion por medio del signo
    if signo > 0:
        crecimiento.append((intervalo, "Creciente"))
    elif signo < 0:
        crecimiento.append((intervalo, "Decreciente"))
# Mostrar resultados 
print("\nIntervalos de crecimiento y decrecimiento:")
for intervalo, tipo in crecimiento:
    a, b = intervalo
    print(f"En ]{a}, {b}[: {tipo}")
    


# Calculando los intervalos de concavidad
# Calculando los puntos críticos de la segunda derivada donde f''(x) = 0
critico_derivada2 = sp.solve(derivada_2_simplificada, x)    #Resuelve la segunda derivada

# Filtra solo las soluciones reales
critico_derivada2 = [sol.evalf() for sol in critico_derivada2 if sol.is_real]

# Agregar los puntos donde la función es indefinida por si afectan la segunda derivada
for valor in valor_invalido:
    if derivada_2_simplificada.subs(x, valor) in [sp.nan, sp.oo, -sp.oo, sp.zoo]:
        critico_derivada2.append(valor)

# Ordenar los puntos criticos
critico_derivada2 = sorted(critico_derivada2)

# Agregar los extremos del dominio
critico_derivada2.insert(0, -sp.oo)
critico_derivada2.append(sp.oo)

# Definir intervalos para analizar el signo de f''(x)
intervalos_concavidad = [(critico_derivada2[i], critico_derivada2[i + 1]) for i in range(len(critico_derivada2) - 1)]

# Analizar el signo de f''(x) en cada intervalo
concavidad = []
for intervalo in intervalos_concavidad:
    a, b = intervalo

    # Elegir un punto de prueba dentro del intervalo para evitar valores indefinidos
    if a == -sp.oo:
        punto_prueba = b - 1  # Tomar un numero menor que el primer punto ciritico
    elif b == sp.oo:
        punto_prueba = a + 1  # Tomar un número mayor que el último punto ciritico
    else:
        punto_prueba = (a + b) / 2  # Punto medio en los intervalos finitos

    # Si el punto de prueba esta en un punto indefinido, moverse un poco
    if any(sp.simplify(punto_prueba - v) == 0 for v in valor_invalido):
        punto_prueba += 0.1  # Moverse ligeramente para evitar indefiniciones

    # Evaluar f''(x) en el punto de prueba
    signo = derivada_2_simplificada.subs(x, punto_prueba)

    if signo > 0:
        concavidad.append((intervalo, "Cóncava hacia arriba"))
    elif signo < 0:
        concavidad.append((intervalo, "Cóncava hacia abajo"))
# Mostrar resultados
print("\nIntervalos de concavidad:")
for intervalo, tipo in concavidad:
    a, b = intervalo
    print(f"En ]{a}, {b}[: {tipo}")
    

# Graficar las funciones f, f', f''
funcion_numerica = sp.lambdify(x, fx, 'numpy')
funcion_derivada1 = sp.lambdify(x, derivada_1, 'numpy')
funcion_derivada2 = sp.lambdify(x, derivada_2, 'numpy')

x_vals = np.linspace(-5, 5, 1000)
x_vals = x_vals[~np.isclose(x_vals, 0, atol=0.01)]  # Evitar x = 0
x_vals = x_vals[~np.isclose(x_vals, 2, atol=0.01)]  # Evitar x = 2

# Calcular los valores de f, f' y f''
y_f = funcion_numerica(x_vals)
y_f_derivada1 = funcion_derivada1(x_vals)
y_f_derivada2 = funcion_derivada2(x_vals)

# Graficar las funciones
plt.figure(figsize=(10, 6))

# Graficar f(x)
plt.plot(x_vals, y_f, label='$f(x)$', color='blue')

# Graficar f'(x)
plt.plot(x_vals, y_f_derivada1, label="$f'(x)$", color='red')

# Graficar f''(x)
plt.plot(x_vals, y_f_derivada2, label="$f''(x)$", color='green')

# Añadir detalles a la gráfica
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Eje x
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Eje y
plt.title("Gráfica de $f(x)$, $f'(x)$ y $f''(x)$")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.xlim(-5, 5)  # Limitar el rango de x para mejor visualizacion
plt.ylim(-10, 10)  # Limitar el rango de y para mejor visualización
plt.show()
