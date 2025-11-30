# Script que imprime los números del 1 al 10 en bucle con una pausa (SMP)

import time

def contar_hasta_diez():
    for i in range(1, 11):
        print(i)

if __name__ == "__main__":
    while True:
        contar_hasta_diez()
        # Incorporo pausa de 60 segundos antes de repetir
        time.sleep(60)

