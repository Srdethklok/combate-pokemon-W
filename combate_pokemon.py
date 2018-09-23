pokemon_elegido = input("¿Que pokemon quieres elegir? (RATATA / MEW / CHARMANDER): ").upper()

vida_pikachu = 100
vida_enemigo = 0

if pokemon_elegido == "RATATA":
    vida_enemigo = 80

if pokemon_elegido == "MEW":
    vida_enemigo = 70

if pokemon_elegido == "CHARMANDER":
    vida_enemigo = 100

while vida_pikachu > 0 and vida_enemigo > 0:

    ataque_elegido = input("¿que ataque quieres elegir? (CHISPAZO / BOLA VOLTIO): ").upper()

    if ataque_elegido == "CHISPAZO":
        vida_enemigo -= 10

    if ataque_elegido == "BOLA VOLTIO":
        vida_enemigo -= 13

    print("la vida del enemigo es de {}".format(vida_enemigo))

    if pokemon_elegido == "RATATA":
        print("Ratata te hace un ataque de 5 de daño!")
        vida_pikachu -= 5

    if pokemon_elegido == "MEW":
        print("Mew te hace un ataque de 10 de daño!")
        vida_pikachu -= 10

    if pokemon_elegido == "CHARMANDER":
        print("Charmander te hace un ataque de 20 de daño!")
        vida_pikachu -= 20

    print("La vida de pikachu es de {}".format(vida_pikachu))

if vida_enemigo <= 0:
    print("has ganado")

if vida_pikachu <= 0:
    print("has perdido")


print("el combate a termionado")
