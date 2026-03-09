def chiffrer(mdp:str, cle_chiffrement:str):
    mdp_chiffre = []
    cle = (cle_chiffrement * len(mdp))[:len(mdp)] # afin d'avoir le meme nombre de caractères entre la clé et le mdp

    for mdp_caractere, cle_chiffrement_caractere in zip(mdp, cle):
        if mdp_caractere == cle_chiffrement_caractere:
            mdp_chiffre.append("0")
        else: 
            mdp_chiffre.append("1")

    return "".join(v for v in mdp_chiffre)

# chiffrer
print(chiffrer("11010001101", "110"))

#déchiffrer
print(chiffrer("00001010110", "110"))

# ============================================ ASCII
print("ADAPTATION ASCII")

def chiffrer_ascii(mdp:str, cle_chiffrement:str):
    mdp_chiffre = []
    mdp_initial = []
    for x in mdp:
        mdp_initial.append(format(ord(x), '08b'))
    mdp = "".join(v for v in mdp_initial) #on passe le mdp en binaire

    cle = (cle_chiffrement * len(mdp))[:len(mdp)] 
    for mdp_caractere, cle_chiffrement_caractere in zip(mdp, cle):
        if mdp_caractere == cle_chiffrement_caractere:
            mdp_chiffre.append("0")
        else: 
            mdp_chiffre.append("1")

    mdp_chiffre = "".join(v for v in mdp_chiffre)
    return ''.join(
        chr(int(mdp_chiffre[i:i+8], 2))
        for i in range(0, len(mdp_chiffre), 8)
    ) # on remet avec le bon format


mdp = chiffrer_ascii("salut à tous, c'est Danielou", "110")
print(f"Element chiffré : {mdp}")
print(f"Element déchiffré : {chiffrer_ascii(mdp, "110")}")