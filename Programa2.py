frase=input("Ingrese la frase:")
vocales="aeiouAEIOU"
cantidad=0
for c in frase:
    if c in vocales:
        cantidad=cantidad+1
print("Vocales que hay en la frase:", cantidad)