prix_du_cafe=0.60
montant_paye=0
"sert a distribuer la boisson en demandant le valeur de la piece et dit si la piece est prise en compte"
while montant_paye<0.60:
    transaction=float(input("saisir le montant de votre piece:"))
    if transaction==2 or transaction==1 or transaction==0.50 or transaction==0.20 or transaction==0.10 or transaction==0.05:
        montant_paye+=transaction
        print("vous avez payer:",montant_paye,"sur 0.60€")
    else :print("la piece n'est pas prise en compte veuillez recomenser")
"sert a definir les piece que la machine va distribuer"
if montant_paye > 0.6 :
    monnaie_brute = montant_paye - 0.6
    monnaie  = round(monnaie_brute, 2)
    print("Voici votre monnaie :",monnaie)
    while monnaie > 0.05 :
        if monnaie >= 2 :
            print("Une piece de deux euros")
            monnaie -= 2
        while monnaie >= 1 :
            print("Une piece de un euro")
            monnaie -= 1
        while monnaie >= 0.5 :
            print("Une piece de cinquantes centimes")
            monnaie -= 0.5
        while monnaie >= 0.2 :
            print("Une piece de vingts centimes")
            monnaie -= 0.2
        while monnaie >= 0.1 :
            print("Une piece de dix centimes")
            monnaie -= 0.1
        while monnaie >= 0.05 :
            print("Une piece de cinq centimes")
            monnaie -= 0.05
else :
    print("Pas de monnaie à rendre")
print("Fin de la transaction")