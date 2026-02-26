import numpy as np
import matplotlib.pyplot as plt

#derivada de f(x) = x^4 en x = 1

def f(x):
    return x**4

def derivada_analitica(x):
    return 4*x**3 #derivada de x^4 es 4*x^3

def derivada_numerica(x, h):
    return (f(x + h) - f(x)) / h

valor_x = 1
valor_real = derivada_analitica(valor_x)

pasos_h = [20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.1, 0.01, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9, 1e-10, 1e-11, 1e-12,1e-13, 1e-14, 1e-15, 1e-16, 1e-17, 1e-18]
print(f"{'h (Paso)':<18} | {'Aprox. Numérica':<20} | {'Error Absoluto':<20}")
print("-" * 60)

errores = []
h_valores = []
for h in pasos_h:
    valor_aprox = derivada_numerica(valor_x, h)
    error = abs(valor_real - valor_aprox)
    
    if h > 1e-18:
        errores.append(error)
        h_valores.append(h)
        
    print(f"{h:<18.1e} | {valor_aprox:<20.10f} | {error:<20.10f}")

plt.figure(figsize=(10, 6))
plt.loglog(h_valores, errores, marker='o', linestyle='--')
plt.title("Convergencia: El porcentaje de error va bajando conforme aumenta el paso")
plt.xlabel("Tamaño del paso (h)")
plt.ylabel("Error Absoluto")
plt.grid(True, which="both", ls="-")
plt.show()

