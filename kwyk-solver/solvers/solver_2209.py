from fractions import Fraction
from functions import int_input, fraction_input


def solve():
    p = fraction_input("Entrez le paramètre de la loi exponentielle : ")
    x = fraction_input("Entrez le nombre auquel X est comparé : ")
    print("La question est :")
    print("\t1. P(X <= a)")
    print("\t2. P(X >= a)")
    choix = 0
    while not choix in [1, 2]:
        choix = int_input("1 ou 2 ? ")

    exponent = Fraction(- p * x).limit_denominator()
    if choix == 1:
        result = f"1 - e^({exponent})"   
    else:
        result = f"e^({exponent})"
    print(f"La probabilité P est de {result}")

