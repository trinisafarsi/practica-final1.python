# Paso 1: Definir el valor actual del Euro y Dolar con respecto al peso mexicano
Tipo_cambio_eur_a_mxn = 23.70 # En un caso mas realista habria que consumir informacion actualizada de una base de datos o API

Tipo_cambio_usd_a_mxn = 20.75 # En un caso mas realista habria que consumir informacion actualizada de una base de datos o API

 # Paso 2: Solicitar al usuario el tipo de conversion(euro a mex o usd a mex)

tipo_conversion = str(input("Ingrese la moneda origen para la conversion(EUR o USD)")) #tener cuidado que aqui esta todo en mayuscula

# Paso 3: Solicitar al usuario monto a convertir

monto_a_convertir = float(input("Ingrese el monto a convertir")) 

# Paso 4: Realizar la conversion utilizando el tipo de cambio correspondiente

if tipo_conversion.upper() == "EUR":


   resultado =  monto_a_convertir * Tipo_cambio_eur_a_mxn
   print("El resultado de la conversion EUR a MXN es:", resultado)
elif tipo_conversion.upper() == "USD": 
    resultado = monto_a_convertir * Tipo_cambio_usd_a_mxn
    print("El resultado de la conversion USD a MXN es:", resultado)
else: 
    print("No esta disponible este tipo de conversion actualmente")

