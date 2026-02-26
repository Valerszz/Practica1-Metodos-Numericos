#Ejercicio 2. Series de Taylor en tiempo real
import math
import numpy as np
import matplotlib.pyplot as plt


#Instrucciones: Suponga un objeto en un videojuego posición en el tiempo se comporta según la función no lineal:
#f(t) = e^(-t) * cos(2t) 
# Queremos predecir la posición del objeto en el instante futuro ti+1 = 0.5 s, sabiendo que actualmente estamos en ti = 0s.
#Implementa manualmente (en código) la Serie de Taylor para predecir f(0.5) 

# ------- LO RICO ------------------------------
def f(t):
    return np.exp(-t) * np.cos(2*t)

#f(0.5) = e^(-0.5) · cos(2·(0.5)) = e^(-0.5) · cos(1) =  0.3273

#Derivadas en t = 0
f0 =  np.exp(0) * np.cos(0)  #f(0) = e^(-0) · cos(2·(0)) = 1 ORDEN 0
f1 = -f0 - 2*np.sin(0)  #ORDEN 1
f2 = f0 - 4*np.cos(0)   #ORDEN 2

#Terminos de la serie de Taylor
h = 0.5 #ti+1 - ti
taylor_0 = f0
taylor_1 = f1 * h
taylor_2 = f2 * h**2 / math.factorial(2)

#Aproximacion de Taylor
P0 = taylor_0
P1 = P0 + taylor_1
P2 = P1 + taylor_2

aproximaciones = [P0, P1, P2]
real = f(0.5) #intervalo de tiempo futuro que queremos predecir

print("\n Orden | Aproximacion | Error Relativo (%)")
for i, P in enumerate(aproximaciones):
    error_relativo = abs((real - P) / real) * 100
    print(f"   {i}   | {P:.6f} | {error_relativo:.6f}%")

# ---- GRAFICAR ------------------------------------------------------------------------------
t_vals = np.linspace(-0.5, 1.0, 300)
y_real = f(t_vals)
y_ord0 = f0 * np.ones_like(t_vals)
y_ord1 = f0 + f1 * (t_vals - 0)
y_ord2 = f0 + f1 * (t_vals - 0) + (f2/2) * (t_vals - 0)**2
plt.figure(figsize=(10, 6))

plt.plot(t_vals, y_real,'k-', linewidth=2.5, label='f(t) = e^(-t) * cos(2t)')
plt.plot(t_vals, y_ord0,'--', linewidth=1.5, label='Orden 0')
plt.plot(t_vals, y_ord1,'--', linewidth=1.5, label='Orden 1')
plt.plot(t_vals, y_ord2,'--', linewidth=1.5, label='Orden 2')

#puntito
plt.plot(0.5, real, 'ro', label='f(0.5) Real')
plt.axvline(x=0.5, color='r', linestyle='--', label='t = 0.5s')


plt.title("Aproximación de la Serie de Taylor para f(t) en torno a t=0")
plt.xlabel('t (segundos)')
plt.ylabel('f(t)')
plt.legend()
plt.grid()
plt.show()



