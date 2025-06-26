def decimal_to_binary(n):
    return bin(n)[2:]

def binary_to_decimal(b):
    return int(b,2)

def main():
    print("choisir 1 ou 2")
    choix=input("choisir")
    if choix=="1" :
        n =int(input("entree un nombre decimal"))
        print(f"binaire: {decimal_to_binary(n)}")
    elif choix=="2" :
        b=input("entree le nombre binaire:").replace(" ","")
        print(f"decimal :{binary_to_decimal(b)}")
    else: print("choix invalide")

if __name__=="__main__":
    main()