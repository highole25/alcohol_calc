
con = "y"

def alkrechner():
    getraenke = int(input("How many beverages does your mixed drink have? "))

    ml = {}
    prozente = {}

    for i in range(getraenke):
        while True:
            try:                       
                print(f"\Drink #{i+1}")
                ml[i] = int(input("How much of this drink are you going to add?(ml) "))
                prozente[i] = float(input("How much alcohol does your drink have?(%) "))
                print("")
            except:
                print("\nNo Input...")

    MlAlkPaare = []

    for i in range(getraenke):
        MlAlkPaare.append(ml[i] * prozente[i])

    gesamtMl = sum(ml.values())

    gesamtMlAlk = sum(MlAlkPaare)

    gesamtAlk = gesamtMlAlk / gesamtMl
    gesamtAlk = round(gesamtAlk, 1)

    print(f"\nYour mixed drink has {gesamtAlk}%")

while con == "y":
    print("")
    print("Alcohol-content Calc")
    print("--------------------")
    print("(decimals have to be seperated by periods)\n")
    alkrechner()
    con = input("use calc again?(y/n) ").lower()
