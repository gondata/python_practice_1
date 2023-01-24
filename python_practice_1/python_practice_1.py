# Python puede funcionar como una calculadora

3+6
3+63-2
3/2
2*5
2**5
3%2
c=23
m=99
m-c

# Cadenas de texto

'Hola'
"Hola"
"'Hola'"
c = "Hola"
print("Hola\nNueva parte")
print("Hola\tTabulacion")
print(r"C:\nombre\skadjas")

# Listas

datos = ["Hola", -5, 6, 3.1, 'Python3']
datos[0]
datos[-1]
datos[-5]
datos[1:]

# Sentencias condicionadas e iterativas
# 1

for number in range(-5, 100):
    if (number % 2 == 0):
        print(number)

# 2

n=0
while n < 100:
    if (n % 2 == 0):
        print(n, "es par")
    else:
        print(n, "es impar")
    n = n+1

#Si quisieramos mas condicionantes, pondriamos "elif" y al final de todo un "else"