#Fernando Fuchs Mora
#Javier Tencio
#Randall 
#Emanuel Chavarria
#Parte 3: analisis de una funcion en python

import sympy as sp
import numpy as np 
import matplotlib.pyplot as plt

#Definicion de la funcion general y algunas variables
x = sp.symbols('x')
fx = (x**3 - 3*x**2 + 3*x -1)/(x**2-2*x)
numerador = x**3 - 3*x**2 + 3*x -1
denominador = x**2-2*x
valor_invalido = sp.solve(denominador,x)

#Calculando el dominio de la funcion 
#Se procede a calcular el dominio mediante el denominador
dominio = x**2-2*x
encontrar_dominio = sp.solve(dominio)
print('La funcion se indefine en:',encontrar_dominio)
dominio = f"Todos los numeros reales menos x = {encontrar_dominio}"
print('El dominio de la funcion es:',dominio)

#Calculando la interseccion de los ejes x e y 
#Interseccion eje x
inter_x = sp.solve(numerador,x)
sol_no_en_dominio = sp.solve(denominador,x)
intersecciones_x = [sol for sol in inter_x if sol not in sol_no_en_dominio]
print('Interseccion con el eje x:',intersecciones_x)

#Interseccion eje y
#revisar esta funcion porque no me da lo que quiero 
try:
    inter_y = fx.subs(x,0)
    print("Intersección con el eje y:", inter_y)
except ZeroDivisionError:
    print("No hay intersección con el eje y (x = 0 no está en el dominio).")

#Calculando asintotas verticales, horizontales y oblicuas
#Asintota vertical
asintota_vertical = []
for valor in valor_invalido:
    numerador
    if numerador.subs(x,0) !=0:
        asintota_vertical.append(valor)
print('Las asintotas verticales son:',asintota_vertical)

#Asintota horizontal
grado_numerador = sp.degree(numerador)
grado_denominador = sp.degree(denominador)
if grado_numerador < grado_denominador:
    asintota_horizontal = 0
elif grado_numerador == grado_denominador:
    coef_numerador = sp.LC(numerador, x)
    coef_denominador = sp.LC(denominador, x)
    asintota_horizontal = coef_numerador / coef_denominador
else:
    asintota_horizontal = None
print("Asíntota horizontal:", asintota_horizontal)

#Asintota Oblicua
if grado_numerador == grado_denominador + 1:
    # Realizar la división polinómica
    cociente, residuo = sp.div(numerador, denominador)
    asintota_oblicua = cociente
    print("Asíntota oblicua:", asintota_oblicua)
else:
    print("No hay asíntota oblicua.")

#Calculando la primera y segunda derivada
derivada_1 = sp.diff(fx,x)
derivada_1_simplificada = sp.simplify(derivada_1)
print('La primera derivada es:',derivada_1_simplificada)
derivada_2 = sp.diff(derivada_1,x)
derivada_2_simplificada = sp.simplify(derivada_2)
print('La segunda derivada es:', derivada_2_simplificada)

#Graficar las funciones f, f', f''
funcion_numerica = sp.lambdify(x,fx,'numpy')
funcion_derivada1 = sp.lambdify(x,derivada_1,'numpy')
funcion_derivada2 = sp.lambdify(x,derivada_2,'numpy')

x_vals = np.linspace(-5, 5, 1000)
x_vals = x_vals[~np.isclose(x_vals, 0, atol=0.01)]  # Evitar x = 0
x_vals = x_vals[~np.isclose(x_vals, 2, atol=0.01)]  # Evitar x = 2

# Calcular los valores de f, f' y f''
y_f = funcion_numerica(x_vals)
y_f_prime = funcion_derivada1(x_vals)
y_f_double_prime = funcion_derivada2(x_vals)

# Graficar las funciones
plt.figure(figsize=(10, 6))

# Graficar f(x)
plt.plot(x_vals, y_f, label='$f(x)$', color='blue')

# Graficar f'(x)
plt.plot(x_vals, y_f_prime, label="$f'(x)$", color='red')

# Graficar f''(x)
plt.plot(x_vals, y_f_double_prime, label="$f''(x)$", color='green')

# Añadir detalles a la gráfica
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Eje x
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Eje y
plt.title("Gráfica de $f(x)$, $f'(x)$ y $f''(x)$")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.xlim(-5, 5)  # Limitar el rango de x para mejor visualización
plt.ylim(-10, 10)  # Limitar el rango de y para mejor visualización
plt.show()