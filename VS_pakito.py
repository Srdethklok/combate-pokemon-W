elegir_enemigo = input("Elige un pokemon enemigo (ARCANINE / ZAPDOS / MUK): ").upper()

vida_pikachu = 100
vida_enemigo = 0
ataque_enemigo = 0

if elegir_enemigo == "ARCANINE":
    vida_enemigo = 85
    nombre_enemigo = "ARCANINE"
    ataque_enemigo = 9
elif elegir_enemigo == "ZAPDOS":
    vida_enemigo = 100
    nombre_enemigo = "ZAPDOS"
    ataque_enemigo = 10
elif elegir_enemigo == "MUK":
    vida_enemigo = 90
    nombre_enemigo = "MUK"
    ataque_enemigo = 8

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("Selecciona tu ataque (RAYO / TRUENO): ").upper()

    if ataque_elegido == "RAYO":
        vida_enemigo -= 15
        print("Pikachu usa ataque rayo y hace 15 de daño")
    elif ataque_elegido == "TRUENO":
        vida_enemigo -= 25
        print("Pikachu usa ataque trueno y hace 25 de daño")

    print("La vida de {} ahora es {}".format(nombre_enemigo, vida_enemigo))
    print("{} te hace un ataque de {} de daño".format(nombre_enemigo, ataque_enemigo))
    vida_pikachu -= ataque_enemigo
    print("La vida de Pikachu es {}".format(vida_pikachu))

if vida_pikachu <= 0:
    print("Has perdido")
if vida_enemigo <= 0:
    print("Has ganado")

print("El combate ha terminado")