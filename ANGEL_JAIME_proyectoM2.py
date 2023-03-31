# Programa 1

# El siguiente programa tiene las siguientes propiedades

print("El primer progama solicita una palabra con logitud minima de 4 letras y maxima de 4.")

while True:
    palabra = input("Introduce una palabra con minimo 4 letras y máximo 8 : ") # 1.- Identifica la longitud de una palabra solicitada # 2.- Aplica restricción de longitud minima de 4 letras y maxima de 8.
    if len(palabra) < 4:
        print("La palabra tiene menos de 4 letras y cuenta con", len(palabra), "letras")# 4.- Si la palabra tiene menos de 4 letras debe indicar un mensaje que diga: Hacen falta letras. Solo tiene N letras (siendo N el número de letras dela palabra)                                                                                     
    elif len(palabra) > 8 :
        print("La palabra tiene mas de 8 letras y cuenta con", len(palabra), "letras") # 5.-Si la palabra tiene más de 8 letras debe indicar un mensaje que diga: Sobran letras. Tiene N letras ((siendo N el número de letras de la palabra))
    else: 
        print("la palabra esta aprobada") # 3.- Si la palabra se encuentra entre el rango previamente establecido debe mostra un mensaje de aprobatorio
        break


# Programa 2


print("El siguiente programa indica en que sector se encuentran el punto conformado por las siguientes coordenadas")

# Crear un programa que en base a 2 números de entrada, coordenadas,
x = float(input("Ingresa la coordenada X: "))
y = float(input("Ingresa la coordenada Y: "))

# Identifique en cuál de los 4 cuadrantes se encuentra el punto.
while x != 0 and y != 0 :
    if x >= 1 and y  >= 1:
        print("El punto se ubican en el primer sector")
        break
    if x >= 1 and y  <= -1:
        print("El punto se ubican en el segundo sector")
        break
    if x <= -1 and y  <= -1:
        print("El punto se ubican en el tercer sector")
        break
    if x <= -1 and y  >= 1:
        print("El punto se ubican en el cuarto sector")
        break
    
# El programa debe verificar que ninguna coordenada sea 0. 
else:
    print("Las coordenadas deben ser mayores a 0 para ubicarse en algún sector\
        de otra forma permancen en el origen o en los ejes.")