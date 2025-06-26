def repeat_key(key,lenght):
    #copie la cle sur la longueur du message chifree
    return (key*((lenght//len(key))+1))[:lenght]
def vigenere_decrypt(cyphertexte,key):
    plaintext=""
    key=key.upper()
    key_index = 0 #position dans la cle repetee
    for char in cyphertexte:
        if char.isalpha():
            # permet de convertire une lettre en indice entre 0 et 25
            is_upper = char.isupper()
            offset = ord('A') if is_upper else ord('a')
            # lettre cle actuelle (toujours en majuscule)
            k = ord(key[key_index % len(key)]) - ord('A')
            c = ord(char) - offset
            # Dechiffrement
            p = (c - k + 26) % 26
            decrypted_char = chr(p + offset)
            plaintext += decrypted_char
            key_index += 1  # on n'avance que si l'on a traite une lettre
        else:
            plaintext += char
    return plaintext


def main():
    cyphertexte = """Gqfltwj emgj clgfv ! Aqltj rjqhjsksg ekxuaqs, ua xtwk
    n'feuguvwb gkwp xwj, ujts f'npxkqvjgw nw tjuwcz
    ugwygjtfkf qz uw efezg sqk gspwonu. Jgsfwb-aqmu f
    Pspygk nj 29 cntnn hqzt dg igtwy fw xtvjg rkkunqf."""
    key = "FCSC"
    decrypted = vigenere_decrypt(cyphertexte, key)
    print("=== Message dechiffre ===")
    print(decrypted)

if __name__ == "__main__":
    main()
