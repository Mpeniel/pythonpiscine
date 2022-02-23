import datetime
import math

# fonction qui demande le nom
def ask_name():
    name  = input("Entrer votre nom :")
    print("votre nom est : {}".format(name))

# demande l'age et affiche l'année ou il auront 100 ans
def age():
    age = int(input("Entrer votre age: "))
    ago = 100 - age
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    print("Vous aurez 100 en : {}".format(int(date.strftime("%Y")) + ago))

# Calcule le volume
def volume(rayon, hauteur):
    volume = (math.pi * rayon**2 * hauteur) / 3
    return volume

# impair ou pair
def odd_or_even(number):
    if number % 2 == 0:
        print("c'est un nombre pair")
    else:
        print("C'est un nombre impair")

# la suite de fibonnaci
def fibo(n):
    if(n <= 1):
        return n
    else:
        return (fibo(n-1) + fibo(n-2))

# fibo final
def fibonnaci(n):
    for i in range(n):
        print(fibo(i))

# ppcm
def ppcm(a,b):
    p=a*b
    while(a!=b):
        if (a<b): b-=a
        else: a-=b
    return p/a

#pgcd
def pgcd(a,b):
    return math.gcd(a,b)

# ppcm et pgcd
def ppcm_pgcd(a,b):
    print("ppcm : "+ppcm(a,b))
    print("pgcd : "+ pgcd(a,b))

#Element commun
def common(a:list, b:list):
    a_set = set(a) 
    b_set = set(b) 
  
    if (a_set & b_set): 
        print(a_set & b_set) 
    else: 
        print("No common elements") 

#palyndrome
def palyndrome(chaine):
    if str(chaine) == str(chaine)[::-1] :
        print("Palindrome")
    else:
        print("Not Palindrome")

# doublon
def doublon(a:list):
    a_set = set(a)
    print(a_set)
#valide adresse ip
def is_valid_ip(ip):
    pass

# transcrire
def transcrire(a):
    if isinstance(a, (int, float)):
        print(bin(a))
    else:
        print("entrer un nombre")

#hexa
def hexadecimal(a):
    if isinstance(a, (int, float)):
        print(hex(a))
    else:
        print("entrer un nombre")
#carré
def carre(n):
    print(("*"*n+"\n")*n )