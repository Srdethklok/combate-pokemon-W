pokemon_elegido = input("¿Que pokemon quieres elegir? (RATATA / MEW / CHARMANDER): ").upper()

vida_pikachu = 100
vida_enemigo = 0

if pokemon_elegido == "RATATA":
     vida_enemigo = 80
     dano_enemigo = 9
     nombre_enemigo = "ratata"

elif pokemon_elegido == "MEW":
     vida_enemigo = 70
     dano_enemigo = 14
     nombre_enemigo = "mew"

elif pokemon_elegido == "CHARMANDER":
     vida_enemigo = 100
     dano_enemigo = 20
     nombre_enemigo = "charmander"

while vida_pikachu > 0 and vida_enemigo > 0:

    ataque_elegido = input("¿que ataque quieres elegir? (CHISPAZO / BOLA VOLTIO): ").upper()

    if ataque_elegido == "CHISPAZO":
        print("Pikachu usa ataque chspazo y te hace un daño de 16")
        vida_enemigo -= 16

    elif ataque_elegido == "BOLA VOLTIO":
        print("Pikachu usa ataque bola voltio y te hace un daño de 24")
        vida_enemigo -= 24

    print("la vida de {} es de {}".format(nombre_enemigo, vida_enemigo))
    print("{} te hace un ataque {} de daño".format(nombre_enemigo, dano_enemigo))
    vida_pikachu -= dano_enemigo
    print("la vida de pikachu es de {}".format(vida_pikachu))


if vida_enemigo <= 0:
    print("has ganado")
    resultado = print("el combate a finalizado")
    input(resultado), input(exit())

if vida_pikachu <= 0:
    print("has perdido")



