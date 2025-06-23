prix_du_cafe=0.60
montant_paye=0
while montant_paye<0.60:
    transaction=float(input("saisir le montant de votre piece:"))
    if transaction==2 or transaction==1 or transaction==0.50 or transaction==0.20 or transaction==0.10 or transaction==0.05:
        montant_paye+=transaction
        print("vous avez payer:",montant_paye,"sur 0.60€")
    else :print("la piece n'est pas prise en compte veuillez recomenser")
print("voici votre cafe et voici votre monnaie:",montant_paye-prix_du_cafe)