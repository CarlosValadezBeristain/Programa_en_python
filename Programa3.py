numeros = []
contador = 1
# Mientras no se hayan leído 5 números...
while len(numeros) < 5:
    # Hacemos un ciclo infinito que se romperá solo cuando estén los tres números ingresados correctamente:
    numero_como_cadena = input("Ingrese el número " + str(contador) + ": ")
    # Intentamos "parsear" el número
    try:
        numero = int(numero_como_cadena)
        # Si pasamos lo de arriba, hacemos otra comprobación: buscamos si el número existe
        if numero in numeros:
            print("El número ya existe")
        else:
            # Si todo es correcto, agregamos el número al arreglo
            numeros.append(numero)
            # Y aumentamos el contador
            contador = contador + 1
    except:
        print("Número no válido")

# Ahora ya tenemos los 5 números, vamos a ordenarlos con el método de la burbuja

for i in numeros:
    for j in range(len(numeros) - 1):
        if numeros[j] > numeros[j+1]:
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
# Ya están ordenados. Los imprimimos
for numero in numeros:
    print(numero)