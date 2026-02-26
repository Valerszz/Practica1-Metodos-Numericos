
import numpy as np
#Tienes 3 sensores midiendo una temperatura constante real de 100.0°C. Toman 5 lecturas cada uno
valor_real=100.0

sensor1 = np.array([105.1, 104.9, 105.0, 105.2, 104.8])
sensor2 = np.array([100.0, 120.0, 80.0, 110.0, 90.0])
sensor3 = np.array([98.1, 101.5, 99.0, 102.1, 99.5])

#Clasifica cada sensor como:Exacto/Inexacto (basado en la media vs valor real) Preciso/Impreciso (basado en la desviación estándar)

# sacar la media d cada sensor para ver si es exacto o inexacto
media_sensor1 = np.mean(sensor1)
media_sensor2 = np.mean(sensor2)
media_sensor3 = np.mean(sensor3)

print("\nMedia de cada sensor:")
print("Sensor 1:", media_sensor1)
print("Sensor 2:", media_sensor2)
print("Sensor 3:", media_sensor3)

# Desviacion estandar de los sensores esto checa si es preciso o no
desv_std_sensor1 = np.std(sensor1)
desv_std_sensor2 = np.std(sensor2)
desv_std_sensor3 = np.std(sensor3)

print("\nDesviación estándar de cada sensor:")
print("Sensor 1:", desv_std_sensor1)
print("Sensor 2:", desv_std_sensor2)
print("Sensor 3:", desv_std_sensor3)



#Revisar la clasificacion de cada sensorr
def clasificar_sensor(media, desviacion_std, valor_real, umbral_precision=2.0): # umbral de precision es el valor maximo de desviacion estandar para que un sensor sea considerado preciso
    if abs(media - valor_real) < 0.5:  # checar que la media quepa dentro de un rango de 0.5 
        exactitud = "Exacto"
    else:
        exactitud = "Inexacto"
    
    if desviacion_std < umbral_precision:  # checar que la descviacion sea menor que el umbral de precision
        precision = "Preciso"
    else:
        precision = "Impreciso"
    
    return exactitud, precision

print ("\nClasificación de los sensores:")
print ("Sensor 1:",clasificar_sensor(media_sensor1, desv_std_sensor1))
print ("Sensor 2:",clasificar_sensor(media_sensor2, desv_std_sensor2))
print ("Sensor 3:",clasificar_sensor(media_sensor3, desv_std_sensor3))  

