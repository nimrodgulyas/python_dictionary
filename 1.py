"""
1. Feladat
Írj egy programot, amely a felhasználótól bekéri egy kutya nevét, életkorát, fajtáját, és azt hogy rendelkezik-e érvényes oltással veszettség ellen!
Az adatokat tárolja a program szótárban, és írja ki a képernyőre az adatszerkezetet!

"""



nev = input("Kérem add meg a kutya nevét!: ")
kor = input("Kérem add meg a kutya életkorát!: ")
fajta = input("Kérem add meg a kutya fajtáját!: ")
oltas_valasz = input("A kutya rendelkezik-e érvényes oltással?(i/n): ")
oltas = oltas_valasz == "i" or oltas_valasz == "igen"


kutya = {
    "nev": nev,
    "kor": kor,
    "fajta": fajta,
    "oltas": oltas

}

for kulcs, ertek in kutya.items():
    print(f"{kulcs}: {ertek}")