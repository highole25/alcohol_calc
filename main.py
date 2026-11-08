
con = "y"

lang = ""

#language dics
titles = {
        "de" : " Alkoholgehalt-Rechner",
        "en" : " Alcohol-content Calc"
    }

decimal_titles = {
        "de" : "(dezimalzahlen müssen mit punkten getrennt werden)",
        "en" : "(decimals have to be seperated by periods)"
    }

use_again_title = {
        "de" : "Rechner erneut nutzen?(y/n)",
        "en" : "use calc again?(y/n)"
    }

drink_count_title = {
        "de" : "Wie viele Getraenke hat deine Mische? ",
        "en" : "how many drinks does your mixed beverage contain? "
    }

drink_titles = {
        "de" : "Getraenk",
        "en" : "drink"
    }

ml_titles = {
        "de" : "wie viel von diesem Getraenk?(ml) ",
        "en" : "how much of this drink?(ml) "
    }

percent_titles = {
        "de" : "Wie viel % hat dein Getraenk? ",
        "en" : "how much alk does your drink have?(%) "
    }

error_titles = {
        "de" : "Keine eingabe vorhanden",
        "en" : "no input available"
    }

end_titles = {
        "de" : "Deine Mische hat",
        "en" : "your drink has"
    }

def alkrechner():
    
    getraenke = int(input(drink_count_title[lang]))

    ml = {}
    prozente = {}

    for i in range(getraenke):
        while True:       
            try:                
                print(f"\n{drink_titles[lang]} #{i+1}")
                ml[i] = int(input(ml_titles[lang]))
                prozente[i] = float(input(percent_titles[lang]))
                print("")
                break
            
            except:              
                print(f"\n{error_titles[lang]}")

    MlAlkPaare = []

    for i in range(getraenke):
        MlAlkPaare.append(ml[i] * prozente[i])

    gesamtMl = sum(ml.values())

    gesamtMlAlk = sum(MlAlkPaare)

    gesamtAlk = gesamtMlAlk / gesamtMl
    gesamtAlk = round(gesamtAlk, 1)
    
    print(f"\n{end_titles[lang]} {gesamtAlk}%")

while con == "y":
    print("")

    while lang not in ("de", "en"):
        try:
            lang = input("choose language(de/en) ")
        except:
            print("please choose available language")
    
    print(titles[lang])
    print(f"{decimal_titles[lang]}\n")
    alkrechner()    
    con = input(use_again_title[lang]).lower()
