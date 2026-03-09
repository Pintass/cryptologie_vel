from utils import utils as c

def RSA(M:int, n:int, p:int, e:int):
    """ Permet de calculer le RSA via tous les "exos" d'avant.
    params: 
        n un entier naturel permettant de déterminer N et phi(N).
        p un entier naturel permettant de déterminer N et phi(N).
        M étant la valeur du message en clair.
        e étant un entier naturel permettant de définir, plus tard, d.
    Questions associées:
        a) Calculer N = np, puis Phi(N) où N est l'indicateur d'Euler et vérifier : M XOR N = 1 (XOR DANS LES JUSTIFICATIONS DU TP NOTé)
        b) Déterminer le reste M`de M^e modulo N
        c) Déterminer l'entier naturel d<Phi(N) tel que ed≡ 1[Phi(N)]
        d) Déterminer le reste M`` de (M`)^d modulo N
    Démarche: 
        Fonctions pour chaque question : 
            a) trouver_indicateur_euler(n:int, p:int, M:int) --> N et le résultat, si 1 ==> premiers entre eux sinon "pas premier"
            b) exponentiation_modulaire(M_prime:int, e:int, N:int) --> M` étant le reste 
            c) inverse_modulaire_bezout(phi_n:int, e:int): --> donnant le PGCD et les coefficients de bezout (u, v)
            d) exponentiation_modulaire(M_prime:int, d:int, N:int) --> M`` étant le reste 
            e) A la fin M`` == M si tout s'est bien produit.
    """
    N = n*p
    phi_n, est_premier = c.trouver_indicateur_euler(n, p, M)
    if not est_premier:
        print("Impossible d'effectuer RSA si N n'est pas premier avec M")
        return False
    
    M_prime = c.exponentiation_modulaire(M, e, N)
    pgcd, coefs = c.inverse_modulaire_bezout(N, e)
    d = e*coefs[1]
    M_prime_prime = c.exponentiation_modulaire(M_prime, d, N)
    if M == M_prime_prime:
        print("RSA executé", M, M_prime_prime)
        return True
    else:
        print("RSA failed", M, M_prime_prime)
        return False

RSA(823, 523, 211, 641)

    


