ures_szotar = {}

szemely = {

    "nev": "Kis Ferenc",
    "kor": "25",
    "varos": "Budapest"
    }

print(szemely["nev"])
print(szemely["kor"])


#   print(szemely.get("kor"))

#   print(szemely["telefon"])

print(szemely.get("telefon","Nincs találat"))



#modositas
szemely["kor"] = 26
print(szemely["kor"])



#kulcs-érték pár hozzáadása

szemely["neme"] = "Férfi"
print(szemely["neme"])



#kulcs-érték pár törlése:
print(szemely["varos"])
del szemely["varos"]
print(szemely.get("varos", "Nincs találat"))


#in operátor

if "nev" in szemely:
    print("A keresett kulcs megtalálható a szótárban")
if "bankszamla" not in szemely:
    print("A keresett kulcs nem található meg a szótárban")


#kulcs-érték párok elérése
for kulcs, ertek in szemely.items():
    print(f"{kulcs} {ertek}")