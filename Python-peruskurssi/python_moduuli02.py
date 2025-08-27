import math

#tehtävä 1
name = input("Kerro nimesi: ")
print(f"Terve, {name}!")

#tehtävä 2
r = float(input("Anna ympyrän säde: "))
A = math.pi * r ** 2 #matemaattinen kaava pinta-alan ympyrän pinta-alan laskemiselle A=πr2
print(f"Ympyrän pinta-ala on {A: .2f}")

#tehtävä 3
kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))
A = kanta * korkeus #pinta-ala
P = (kanta * 2) + (korkeus * 2) # piiri
print(f"Suorakulmion pinta-ala on {A:.2f} ja piiri {P:.2f}")

#tehtävä 4
luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = (luku1 + luku2 + luku3) / 3
print(f"Lukujen summa on {summa}, tulo on {tulo}, ja keskiarvo on {keskiarvo:.2f}.")





