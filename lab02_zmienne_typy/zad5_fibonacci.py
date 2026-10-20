# Lab 02 – Zadanie 5 (☆, dodatkowe): Ciąg Fibonacciego
#
# Program wczytuje n i wypisuje n pierwszych wyrazów ciągu Fibonacciego
# oddzielonych spacjami, np. dla n = 10:
#     0 1 1 2 3 5 8 13 21 34
#
# Każdy kolejny wyraz to suma dwóch poprzednich.
# Potrzebna będzie pętla for (lab 04) – zajrzyj do slajdów i spróbuj!
# Wskazówka: a, b = b, a + b

# TODO: Twój kod poniżej
n = int(input("Podaj liczbę wyrazów ciągu Fibonacciego: "))
a, b = 0, 1 
print(a, end=" ")
for _ in range(n - 1):
    print(b, end=" ")
    a, b = b, a + b


