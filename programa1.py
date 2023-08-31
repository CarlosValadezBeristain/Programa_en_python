while True:
    try:
        num = int(input("Ingrese un número del 1 al 12: "))
        if num < 1 or num > 12:
            raise ValueError
        break
    except ValueError:
        print("Ingrese un número válido del 1 al 12")

print(f"Tabla de multiplicar del {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}"