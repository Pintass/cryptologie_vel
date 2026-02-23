def init_nb_premiers(maxi:int):
    nb_premiers = []

    for i in range(2, maxi+1): #+1 pour faire apparaître maxi s'il est premier.
        est_premier = True
        for k in nb_premiers:
            if i % k == 0:
                est_premier = False
                break
        
        if est_premier:
            nb_premiers.append(i)
    return nb_premiers


def decomposition_primaire(nombre:int):
    """
        Démarche: 
            On prends d'abord tous les nb premiers jusqu'à 'nombre'
            si 'nombre' est premier et donc dans la liste des premiers, sa décomposition est : nombre^1

            Sinon, on prend le plus grand nombre premier de la liste et on appplique : nombre % nombrePremier, s'il est égal à 0, son exposant prends +1, équivalent au nombre de fois que l'on utilise nombrePremier
            Si l'exposant n'est pas 0, on l'ajoute au résultat final.
            A la fin du parcourt de la liste des nbPremiers, on aura un reste = 0

    """
    nb_premiers = init_nb_premiers(nombre)
    resultat = [] # format : li = [[coef, exposant]]
    nb_final = nombre
    compteur = 0 # équivaut à l'exposant

    if nombre in nb_premiers:
        resultat.append([nombre, 1])
        print(f"nombre de départ : {nombre}, décomposition : {resultat}")
        return resultat

    for premier in reversed(nb_premiers):
        while nb_final % premier == 0: # tant que l'on peut, on garde ce nombre premier
            nb_final = nb_final // premier
            compteur += 1
        if compteur != 0: # si on a fait au moins 1 tour dans la boucle, on l'ajoute au résultat
            resultat.append([premier, compteur])
            compteur = 0 
        # si compteur = 0 car aucun tour dans le while => on ne l'affiche pas.

    print(f"nombre de départ : {nombre}, décomposition : {resultat}")
    return resultat
    
def bezout(a:int, b:int):
    """
        Démarche: 
            Ligne1 = A un entier naturel ainsi que 1*A  et 0*B
            Ligne2 = B un entier naturel ainsi que 0*A et 1*B

            pour passer à la ligne suivante, on fait le quotient : A // B
            ainsi, on saura passer à la prochaine ligne.
            Le quotient est équivalent à la question : Combien de fois j'ai B dans A?
            Le for in range(0,3) permet de le faire sur tous les éléments de la ligne.

            On prend l'avant dernière ligne, soit le résultat de Ligne1 puisque Ligne2 aura un résultat = 0, le PGCD doi être non nul, donc seul la ligne antérieur nous intéresse.

    """
    Ligne1 = [a, 1, 0]
    Ligne2 = [b, 0, 1]
    while Ligne2[0] != 0:
        quotient = Ligne1[0] // Ligne2[0]
        LigneTmp = Ligne2.copy()
        for i in range(0,3):
            Ligne2[i] = Ligne1[i]-quotient*Ligne2[i]
        Ligne1 = LigneTmp
    print(f"PGCD : {Ligne1[0]} | u= {Ligne1[1]} et  v= {Ligne1[2]}")
    return Ligne1[0], (Ligne1[1], Ligne1[2]) # équivaut au PGCD & u, v
    

def exponentiation_modulaire(M:int, e:int, N:int):
    """
        exemple:
            result = 5^^45 % 17 soit 5^^45≡result[17] en écriture mathématique
        params: 
            M: un entier naturel étant 5 dans l'exemple.
            e: un exposant entier naturel, étant 45 dans l'exemple.
            N: un modulo entier naturel, étant 17 dans l'exemple.
        result: étant le reste du calcul.
    """
    exposants = []
    restes = []
    e_base2 = format(e, '08b') #l'exposant (45 dans l'exemple) en base 2
    for position, i in enumerate(e_base2):
        if i == '1':
            exposants.append(2 ** (7 - position)) # permet d'avoir la décomposition : 45 = 2^^0 + 2^^2 + 2^^3 + 2^^5

    # passons aux restes pour chaque exposant
    for expoz in exposants:
        restes.append(M**expoz % N)

    Me_final = 1
    for x in restes: # on multiplie tous les restes ensembles
        Me_final *= x
    
    print(f"Le reste est : {Me_final % N}\nJustification: 0<= ``{Me_final % N}`` <{N}") # on applique le modulo N (17 dans l'exemple) afin que le reste soit bien >= 0 et < à N | Dans l'exemple : reste = 3 et 0 <= 3 < 17
    return Me_final % N




exponentiation_modulaire(5,45,17)

        




    

        
        

        
        