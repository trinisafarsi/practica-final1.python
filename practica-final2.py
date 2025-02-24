 


# Paso 1: Solicitar al usuario las medidas de la pieza del mueble en cms
medida_en_cm = float(input("Porfavor, ingresar las medidas de la pieza del mueble (en cm): "))


# Paso 2: Convertir las medidas de centimetros a pulgadas
medidas_en_pulgadas = medida_en_cm/ 2.54

# Paso 3: Mostrar las medidas convertidas en pulgadas al usuario
print(" Las medidas de la pieza ingresada son:", medidas_en_pulgadas, " pulgadas")
