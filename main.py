from evidence import Evidence

evidence = Evidence()
pojistenci = []

pokracovat = True
while pokracovat:
    print("--------------------------------\nEVIDENCE POJIŠTĚNÝCH\n--------------------------------")
    print("Vyberte si akci a stisněte enter : ")
    print("1 - Přidat nového pojištěnce\n")
    print("2 - Vypsat všechny pojištěné\n")
    print("3 - Vyhledat pojistěného\n")
    print("4 - Konec\n")

    volba = int(input())
    if volba == 1:
        novy_pojistenec = evidence.pridat()
        pojistenci.append(novy_pojistenec)
        print("Pojištěnec byl uložen do databáze. Pokračujte stisknutím klávesy enter...")
        input()
    elif volba == 2:
        evidence.vypsat(pojistenci)
        print("Pro návrat do menu stiskněte enter...")
        input()
    elif volba == 3:
        evidence.vyhledat(pojistenci)
        print("Pro návrat do menu stiskněte enter...")
        input()
    elif volba == 4:
        pokracovat = False
        print("Děkujeme a nashledanou :-)")
    else:
        print("Nesprávná volba")
        pokracovat = False





