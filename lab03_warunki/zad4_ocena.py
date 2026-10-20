# Lab 03 – Zadanie 4 (★): Ocena z przedmiotu
#
# Program wczytuje liczbę punktów (0–100) i wypisuje ocenę według progów
# z sylabusa naszego przedmiotu:
#     > 91        -> 5
#     > 83 – 91   -> 4.5
#     > 75 – 83   -> 4
#     > 67 – 75   -> 3.5
#     > 60 – 67   -> 3
#     <= 60       -> 2
#
# Przykład:  Ocena: 4.5
# Uwaga: w zachęcie input() nie wypisuj liczb (np. „0-100”) – testy szukają liczb w wyjściu.

# TODO: Twój kod poniżej
liczba_punktów = float(input("Podaj liczbę punktów: "))
if liczba_punktów > 91:
    ocena = 5
elif liczba_punktów > 83:
    ocena = 4.5
elif liczba_punktów > 75:
    ocena = 4
elif liczba_punktów > 67:
    ocena = 3.5 
elif liczba_punktów > 60: 
    ocena = 3
else:
    ocena = 2
print(f"Ocena: {ocena}")
