elegir_enemigo = input("Elige un pokemon enemigo (ARCANINE / ZAPDOS / MUK): ").upper()

vida_pikachu = 100
vida_enemigo = 0

if elegir_enemigo == "ARCANINE":
    vida_enemigo = 85
if elegir_enemigo == "ZAPDOS":
    vida_enemigo = 100
if elegir_enemigo == "MUK":
    vida_enemigo = 90

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("Selecciona tu ataque (RAYO / TRUENO): ").upper()

    if ataque_elegido == "RAYO":
        print("Pikachu hace 15 de daño")
        vida_enemigo -= 15
    if ataque_elegido == "TRUENO":
        print("Pikachu hace 25 de daño")
        vida_enemigo -= 25
    print("La vida del enemigo es {}".format(vida_enemigo))

    if elegir_enemigo == "ARCANINE":
        print("Arcanine te hace 10 de daño")
        vida_pikachu -= 10
    if elegir_enemigo == "ZAPDOS":
        print("Zapdos te hace 10 de daño")
        vida_pikachu -= 10
    if elegir_enemigo == "MUK":
        print("Muk te hace 10 de daño")
        vida_pikachu -= 10
    print("La vida de Pikachu es {}".format(vida_pikachu))

if vida_pikachu <= 0:
    print("Has perdido")
if vida_enemigo <= 0:
    print("Has ganado")

print("El combate ha terminado")