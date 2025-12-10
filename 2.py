"""

2. Feladat
Írj egy programot, amely szótárban tárolja egy macska nevét, korát. A felhasználónak legyen lehetősége megváltoztatni az egyik tárolt adatot.
A program írja ki a felhasználó választása alapján az egyik adatot, kérdezze meg, mire módosítsa, végül írja ki a képernyőre a frissített
adatszerkezetet!
"""

macska_nev = input("Add meg a macskád nevét!: ")
macska_kora = input("Add meg a macskád korát!: ")

macska = {
    "nev": macska_nev,
    "kor": macska_kora
}

print(macska_nev["nev"])
print(macska_kora["kor"])



valtoztatas = input("Melyik adatot akarod változtatni?(nev/kor): ")
if "kor" in input:
    macska["kor"] = int(input("Add meg a macskád megváltozott korát!: "))
elif "nev" in input:
    macska["nev"] = input("Add meg a macska megváltozott nevét!: ")






