import numpy as np

def mi_log_natural(x_val, tolerancia):
    xr = 0
    iteracion = 0
    error_aprox = 100  # error grande para poder hacer los calculos
    
#ciclo
    while error_aprox > tolerancia:
        iteracion += 1
        xr_old = xr
       
        
        termino = ((-1)**(iteracion + 1)) * (x_val**iteracion) / iteracion
        xr += termino
        
        # calculo del error aproximado
        if iteracion > 1: #el 1 para evita que se divida por 0 y explote
            error_aprox = abs((xr - xr_old) / xr) * 100
    
    return xr, iteracion

# con ln (1.5)
resultado, iters = mi_log_natural(0.5, 0.001)
real = np.log(1.5)
print(f"Aproximación: {resultado:.6f}")
print(f"Valor real:   {real:.6f}")
print(f"Iteraciones:  {iters}")

