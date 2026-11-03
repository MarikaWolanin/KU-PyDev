# Lab 04 – Zadanie 5 (☆, dodatkowe): Mini-crawler
#
# Crawler (robot sieciowy) przegląda strony i zbiera z nich linki.
# Przeczytaj plik dane/strona.html i:
#   1. policz wszystkie linki – wystąpienia tekstu  href="
#   2. wypisz domeny linków bez powtórzeń, np. docs.python.org
#
# Wynik:
#     Liczba linków: 5
#     www.python.org
#     docs.python.org
#     ...
#
# Wskazówki:
#   - text.find('href="', start) zwraca pozycję albo -1 – szukaj w pętli while
#   - adres kończy się na kolejnym znaku "
#   - domena to fragment między "://" a pierwszym "/" po nim
#   - (dla chętnych) urllib.request.urlopen pobierze prawdziwą stronę

from pathlib import Path

sciezka = Path(__file__).parent / "dane" / "strona.html"

with open(sciezka, encoding="utf-8") as f:
    html = f.read()

# TODO: Twój kod poniżej
linki = []
start = 0

while True:
    pozycja = html.find('href="', start)
    if pozycja == -1:
        break
    start = pozycja + 6
    koniec = html.find('"', start)
    link = html[start:koniec]
    start = koniec + 1
    linki.append(link)

domeny = set()
for link in linki:
    if "://" in link:
        domena = link.split("://")[1].split("/")[0]
        domeny.add(domena)

print(f"Liczba linków: {len(linki)}")
for domena in sorted(domeny):
    print(domena)

