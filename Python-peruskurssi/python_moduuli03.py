#tehtävä 1
kuhan_pituus = int(input("Anna kuhan pituus senttimetreinä: "))
if kuhan_pituus < 37:
    print("Laske kuha takaisin järveen.")
    print(f"Kuhan pituus {37 - kuhan_pituus} senttimetriä alle sallitun!23") #vähennetään annettu pituus alimmasta sallitusta

#tehtävä 2
hyttiluokka = input("Anna hyttiluokka (LUX, A, B tai C): ")
if hyttiluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")

#tehtävä 3
sukupuoli = input("Anna biologinen sukupuolesi: ")
hemoglobiini = int(input("Anna hemoglobiiniarvosi: "))
if sukupuoli == "Nainen":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemoglobiini > 175:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
if sukupuoli == "Mies":
    if hemoglobiini < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemoglobiini > 195:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")

#tehtävä 4
vuosi = int(input("Anna vuosiluku: "))
if vuosi % 4 == 0:  #onko jaollinen neljällä
    if vuosi % 100 == 0:  #jos jaollinen neljällä niin tarkastatetaan sadalla jaollisuus
        if vuosi % 400 == 0:  #jos jaollinen sadalla, tarkastetaan vielä erityisehto
            print(f"{vuosi} on karkausvuosi.") #jos jaollinen neljälläsadalla
        else:
            print(f"{vuosi} ei ole karkausvuosi.") #jos ei jaollinen neljälläsadalla
    else:
        print(f"{vuosi} on karkausvuosi.") #jos ei jaollinen sadalla
else:
    print(f"{vuosi} ei ole karkausvuosi.") #jos ei jaollinen neljällä