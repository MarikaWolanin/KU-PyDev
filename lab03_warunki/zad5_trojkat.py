# Lab 03 – Zadanie 5 (☆, dodatkowe): Jaki to trójkąt?
#
# Program wczytuje trzy długości boków (float) i wypisuje:
#   - "Nie da się zbudować trójkąta", jeśli nie spełniają nierówności trójkąta
#     (każdy bok musi być krótszy od sumy dwóch pozostałych),
#   - w przeciwnym razie rodzaj: "równoboczny", "równoramienny" albo "różnoboczny",
#   - dodatkowo "prostokątny", jeśli a² + b² = c² dla najdłuższego boku c
#     (porównuj z tolerancją: abs(x - y) < 1e-9).

# TODO: Twój kod poniżej
bok1 = float(input("Podaj długość pierwszego boku: "))
bok2 = float(input("Podaj długość drugiego boku:"))
bok3 = float(input("Podaj długość trzeciego boku: "))
if bok1 + bok2 <= bok3 or bok1 + bok3 <= bok2 or bok2 + bok3 <= bok1:
    print("Nie da się zbudować trójkąta")
else:
    if bok1 == bok2 == bok3:
        print("Trójkąt jest równoboczny ")
    elif bok1 == bok2 or bok1 == bok3 or bok2 == bok3 :
        print("Trójkąt jest równoramienny ")
    else:
        print("Trójkąt jest różnoboczny ")

    a, b, c = sorted([bok1, bok2, bok3])
    if abs(a**2 + b**2 - c**2) < 1e-9:
        print("Trójkąt jest prostokątny")



