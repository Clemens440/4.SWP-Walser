import random


def lottoziehung():
    zahlen = []
    for i in range(1, 46):
        zahlen.append(i)

    gezogen = []
    for i in range(6):
        position = random.randint(0, len(zahlen) - 1)
        zahl = zahlen.pop(position)
        gezogen.append(zahl)

    return gezogen


def statistik(zaehler, gezogen):
    for zahl in gezogen:
        zaehler[zahl] = zaehler[zahl] + 1


def lotto_statistik(anzahl):
    zaehler = {}
    for i in range(1, 46):
        zaehler[i] = 0

    for i in range(anzahl):
        gezogen = lottoziehung()
        statistik(zaehler, gezogen)

    print("Statistik fuer", anzahl, "Ziehungen:")
    for zahl in zaehler:
        print(zahl, ":", zaehler[zahl])
    print()


# Hauptprogramm
print("Die Lottozahlen sind:", lottoziehung())
print()

lotto_statistik(1000)
lotto_statistik(10000)
lotto_statistik(100000)