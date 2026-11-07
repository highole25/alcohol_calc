
con = "y"

def alkrechner():
    getraenke = int(input("Wie viele Getraenke hat deine Mische? "))

    ml = {}
    prozente = {}

    for i in range(getraenke):
        while True:       
            try:
                print(f"\nGetraenk #{i+1}")
                ml[i] = int(input("Wie viel ml hat dein Getränk? "))
                prozente[i] = float(input("Wie viel % hat dein Getränk? "))
                print("")
                break
            except:
                print("\nKeine Eingabe vorhanden...")

    MlAlkPaare = []

    for i in range(getraenke):
        MlAlkPaare.append(ml[i] * prozente[i])

    gesamtMl = sum(ml.values())

    gesamtMlAlk = sum(MlAlkPaare)

    gesamtAlk = gesamtMlAlk / gesamtMl
    gesamtAlk = round(gesamtAlk, 1)

    print(f"\nDeine Mische hat {gesamtAlk}%")

while con == "y":
    print("")
    print("Alkoholgehalt-Rechner")
    print("---------------------")
    print("(dezimalzahlen müssen mit punkten getrennt werden)\n")
    alkrechner()
    con = input("Rechner erneut nutzen?(y/n) ").lower()
