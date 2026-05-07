hp1=100
hp2=100
turno=1
while hp1 >= 2 and 2 <= hp2:
    if turno == 1:
        print("Jugador 1 ataca")
        hp2-= 3
        turno=2
    else:
        print("Jugador 2 ataca")
        hp2-= 3
        turno=2