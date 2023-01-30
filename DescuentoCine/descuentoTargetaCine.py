
# El valor de las entradas de una sala de CineMark es de 20.000 pesos y los días jueves se aplica un decuento
# del 50%, adicional para usuarios que tengan la targeta CineMark se les aplica un descuento adicionel del 10%.
# Elabore un algoritmo que pregunte al usuario el día de la pelicula y si cuenta con la targeta CineMark;
# y con base a los anterior informe el precio final que debe pagar.


canboleta = int(input("Por favor digite el número de entradas que quiere: "))
dia = str(input("Digite que día es: \n Lunes = 1 \n Martes = 2 \n Miércoles = 3 \n Jueves = 4 \n Viernes = 5 \n Sábado = 6 \n Domingo = 7 \n"))
if dia == 4:
    descuentoJueves = ((canboleta*20000)*50)/100
    tarjeta = str(print("Si tiene la tarjeta CineMark digite S o N: "))
    if tarjeta == "s":
        descuentoTargenta = descuentoJueves * 10
        total = descuentoJueves - descuentoTargenta
        print("EL valor final con descuento jueves y descuento tarjeta es :", total)
    else:
        print("El valor total con el descuento de jueves es: " + descuentoJueves)

else:
    total = canboleta * 20000
    print("El valor tota es: ", total)
