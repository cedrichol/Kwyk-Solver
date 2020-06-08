from fractions import Fraction
from functions import int_input, fraction_input


def solve():
    x = fraction_input("Entrez le nombre auquel X est comparé : ")
    p = fraction_input("Entrez la valeur de la probabilité P : ")
    print("La question est :")
    print("\t1. P(X <= a)")
    print("\t2. P(X >= a)")
    choix = 0
    while not choix in [1, 2]:
        choix = int_input("1 ou 2 ? ")

    if choix == 1:
        result = f"ln({- p + 1})/({- x})"
    else:
        result = f"ln({p})/({- x})"
    print(f"La paramètre λ est égal à {result}")

