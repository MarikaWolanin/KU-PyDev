# Lab 03 – Zadanie 2 (★): Kalkulator z wyborem działania
#
# Program wczytuje kolejno: liczbę, operator (+, -, *, /) i drugą liczbę,
# a potem wypisuje wynik, np.:  8.0 * 2.0 = 16.0
#
# Obsłuż przypadki szczególne instrukcją if:
#   - dzielenie przez zero  -> "Nie można dzielić przez zero"
#   - inny operator         -> "Nieznany operator"

# TODO: Twój kod poniżej
liczbaA = float(input("Podaj pierwszą liczbę: "))
operator = input("Podaj operator (+, -, *, /): ").strip()

if operator not in ("+", "-", "*", "/"):
    print("Nieznany operator")
else:
    liczbaB = float(input("Podaj drugą liczbę: "))
    
    if operator == "+":
        wynik = liczbaA + liczbaB
        print(f"{liczbaA} + {liczbaB} = {wynik}")
    elif operator == "-":
        wynik = liczbaA - liczbaB
        print(f"{liczbaA} - {liczbaB} = {wynik}")
    elif operator == "*":
        wynik = liczbaA * liczbaB
        print(f"{liczbaA} * {liczbaB} = {wynik}")
    elif operator == "/":
        if liczbaB == 0:
            print("Nie można dzielić przez zero")
        else:
            wynik = liczbaA / liczbaB
            print(f"{liczbaA} / {liczbaB} = {wynik}")
