import math
import random

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
A = kanta * korkeus #pinta-alan kaava
P = (kanta * 2) + (korkeus * 2) #piirin kaava
print(f"Suorakulmion pinta-ala on {A:.2f} ja piiri {P:.2f}")

#tehtävä 4
luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = (luku1 + luku2 + luku3) / 3 #keskiarvon laskeminen
print(f"Lukujen summa on {summa}, tulo on {tulo}, ja keskiarvo on {keskiarvo:.2f}.")

#tehtävä 5
leiviska = int(input("Anna leiviskät: "))
naula = int(input("Anna naulat: "))
luoti = int(input("Anna luodit: "))
luodit_yht = (leiviska * 20 * 32) + (naula * 32) + luoti #koska luodit tiedetään grammoina niin muunnetaan kaikki luodeiksi
grammat_yht = luodit_yht * 13.3 #muutetaan luodit grammoiksi
kilot = int(grammat_yht // 1000)
grammat = grammat_yht % 1000
print(f"Massa on {kilot} kilogrammaa ja {grammat:.2f} grammaa")

#tehtävä 6
for i in range (3): #muodostetaan loop, koodi sisällä suoritetaan 3 kertaa
    print(random.randint(0, 9), end = " ") #silmukan sisällä tapahtuva koodi, tulostaa 3 kertaa luvun 1 ja 9 välillä
print() #seuraava loop alkaa uudelta riviltä
for i in range (4):
    print(random.randint(1, 6), end = " ")