# -*- coding: utf-8 -*-

"""

TP2 - Le paradoxe du chevalier de Méré
Auteur : Gotchu

"""

import math;
import random;


#cette fonction retourne vrai si le 6 est apparu au moins une fois en 4 lancés
def lanceDe4():
    for i in range(4):
        if(random.randint(1,6)==6):
            return True
    return False


#cette fonction prend en parametre le vecteur taille (le vecteur taille est le nombre de fois que vous voulez répéter l'opération, plus il est grand plus la probabilité sera précise)
# et elle retourne la probabilité que le 6 apparaisse 
def theorieChev4(nbTimes):
    c = 0
    for i in range(nbTimes):
        if(lanceDe4()==True):
            c = c+1;
    
    return c/nbTimes


print("4 fois")
print(theorieChev4(10))
print(theorieChev4(100))
print(theorieChev4(1000))
print(theorieChev4(10000))
print(theorieChev4(100000))
#on peut remarquer que plus le vecteur taille est grand plus on a un resultat précis
            

#cette fonction retourne vrai si un double 6 est apparu au moins une fois en 24 lancés
def lanceDoubleDe24():
    c = 0
    for i in range(24):
        if(random.randint(1,6)==6):
            if(random.randint(1,6)==6):
                return True
    return False
 

#cette fonction prend en parametre le vecteur taille (le vecteur taille est le nombre de fois que vous voulez répéter l'opération, plus il est grand plus la probabilité sera précise)
# et elle retourne la probabilité que le double 6 apparaisse 
def theorieChev24(nbTimes):
    c = 0
    for i in range(nbTimes):
        if(lanceDoubleDe24()==True):
            c = c+1;
    
    return c/nbTimes




print()
print("24 fois")
print(theorieChev24(10))
print(theorieChev24(100))
print(theorieChev24(1000))
print(theorieChev24(10000))
print(theorieChev24(100000))
