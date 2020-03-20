print('Ingrese la palabra a encontrar')
texto = input()
count=0
while(count < 50):
    print('--------------------------------------------------')
    count=count+1
print(' ')

cant_letras = len(texto)
vidas = 6
aux = 0
cadena_usuario=[]
for i in range(len(texto)):
    cadena_usuario.append(' ')
encontre=False
print('La palabra posee ',len(texto), ' letras')
while cant_letras != 0 and vidas > 0:                                          #COMIENZO WHILE PRINCIPAL
    print('Ingrese una letra')
    letra = input()
    encontre=False
    indice=0
    while (encontre == False) and (indice < len(texto)):       #MIENTRAS NO ENCONTRE LA LETRA EN EL TEXTO Y NO LLEGUE AL FIN DE LA PALABRA
        if (letra==texto[indice]):                                              #SI LA LETRA COINCIDE CON ALGUNA DEL TEXTO
            encontre=True
            for i in range(len(texto)):                                         #LLENO ESPACIOS QUE EXISTE LA LETRA
                if(letra == texto[i]):
                    cadena_usuario[i] = letra
                    cant_letras=cant_letras-1
        else:
            encontre=False
            indice=indice+1


    if(encontre==True):                                                         #SI COINCIDIO, MUESTRO RESULTADOS
        print('Encontraste la letra ', letra ,' - La palabra quedo asi: ')
        for x in range(len(texto)):
            if cadena_usuario[x] != ' ':
                print(cadena_usuario[x])
            else:
                    print('_')
    else:                                                                       #SINO, RESTO VIDA Y MUESTRO COMO QUEDO LA PALABRA
        vidas = vidas - 1
        print('La letra ', letra ,' no esta en la palabra. Segui intentando')
        print ('La palabra quedo asi: ')
        for x in range(len(texto)):
            if cadena_usuario[x] != ' ':
                print(cadena_usuario[x])
            else:
                print('_')
    print('VIDAS: ', vidas)
                                                                                #FIN WHILE PRINCIPAL
if (vidas==0):
    print('Perdiste el juego :(')
else:
    print ('Ganaste!')
