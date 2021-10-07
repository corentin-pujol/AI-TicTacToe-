# -*- coding: utf-8 -*-
"""
Created on Fri May 14 18:57:16 2021

@author: alice
"""
import random as rd
import time

class Action: #On définit une action par son motif (X ou O) et ses coordonnées dans la grille 12x12
    def __init__(self,motif,coordonnees):
        self.motif = motif
        self.coordonnees = coordonnees
    def __str__(self):
        return f"({self.motif}, {self.coordonnees})"
    def __eq__(self, autreaction): #permet le testd'égalité de deux sepales
        result = False
        if((self.motif==autreaction.motif) and (self.coordonnees==autreaction.coordonnees)):
            result = True
        return result
    def __contains__(self,x):
        return True
    def __hash__(self):
        return hash((self.motif, self.coordonnees))


def Grille12x12(): #On définit la grille initiale par une matrice 4x4 définit par des points, un point caractérisant une possibilité de jeu
    l=[['.','.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.','.','.','.']] 
    return l


def AffichageGrille(grille):
    res = "   0   1   2   3   4   5   6   7   8   9   10  11\n0  "
    for i in range(len(grille)):
        for j in range(len(grille)-1):
            res += str(grille[i][j]) + ' | '
        res += str(grille[i][len(grille)-1])
        print(res)
        if(len(str(i+1))==2):
            res= str(i+1) + ' '
        else:
            res= str(i+1) + "  "

def Actions(s): #Nous parcourons la grille, et si une case est vide, alors nous pouvons y jouer un coup et nous sauvegardons les coordonnées sous la forme d'un tuple à deux éléments stocké dans la liste de l'ensemble des actions possibles
    liste_actions=[]
    for i in range(len(s)):
        for j in range(len(s)):
            if(s[i][j]=='.'):
                action = tuple([i,j])
                liste_actions.append(action)
    return liste_actions

def ActionsProches(s):
    liste_actions_proches=[]
    for i in range(len(s)):
        for j in range(len(s)):
            if(s[i][j]=='X' or s[i][j]=='O'):
                if( i < 11 and j>=1 and s[i+1][j-1]=='.'): 
                    liste_actions_proches.append(tuple([i+1,j-1]))
                if(i<11 and s[i+1][j]=='.'): 
                    liste_actions_proches.append(tuple([i+1,j]))
                if(i < 11 and j < 11 and s[i+1][j+1]=='.'): 
                        liste_actions_proches.append(tuple([i+1,j+1]))
                if( i >=1 and s[i-1][j]=='.') :
                    liste_actions_proches.append(tuple([i-1,j]))
                if( i >=1 and j <11 and s[i-1][j+1]=='.'): 
                    liste_actions_proches.append(tuple([i-1,j+1]))
                if(i >=1 and j >=1 and s[i-1][j-1]=='.') :
                    liste_actions_proches.append(tuple([i-1,j-1]))
                if(j<11 and s[i][j+1]=='.') :
                    liste_actions_proches.append(tuple([i,j+1]))
                if(j>=1 and s[i][j-1]=='.' ) :
                    liste_actions_proches.append(tuple([i,j-1]))
    return liste_actions_proches

#grille=Grille12x12()

def Result(s,a): #On applique l'action a (soit mettre un X ou un O aux coordonnées demandées) dans la grille
    l=Actions(s)
    if(a.coordonnees in l):
        s[a.coordonnees[0]][a.coordonnees[1]]=a.motif
    else:
        print("L'action souhaité n'est pas possible")
        return -1
    return s

#grille = Result(grille,Action('X',(5,4)))
#grille = Result(grille,Action('X',(5,5)))
#grille = Result(grille,Action('X',(5,6)))
#grille = Result(grille,Action('X',(5,7)))

#grille = Result(grille,Action('X',(4,4)))
#grille = Result(grille,Action('X',(6,4)))
#grille = Result(grille,Action('X',(7,4)))

#grille = Result(grille,Action('X',(4,5)))
#grille = Result(grille,Action('X',(3,6)))
#grille = Result(grille,Action('X',(2,7)))

#AffichageGrille(grille)

def CheckLine(s,motif,i,j):
    nb=1
    #Vérification à droite
    cpt=1
    if(j+3<=len(s)-1):
        while(s[i][j+cpt]==motif):
            if(nb==3):
                return True #Les 3 motifs à la droite du motif sont identiques, c'est terminé
            else:
                cpt += 1
                nb += 1
    #Vérification à gauche
    cpt=1
    if(j-3>=0):
        while(s[i][j-cpt]==motif):
            if(nb==3):
                return True #Les 3 motifs à la gauche du motif sont identiques, c'est terminé
            else:
                cpt += 1
                nb += 1
    
    return False #Si l'on sort des deux boucles while, cela signifie qu'il n'y a pas 4 motifs identiques alignés
  
#print(CheckLine(grille,'X',5,4))
#print(CheckLine(grille,'X',5,6))
   
def CheckColumn(s,motif,i,j):
    nb=1
    #Vérification en dessous
    cpt=1
    if(i+3<=len(s)-1):
        while(s[i+cpt][j]==motif):
            if(nb==3):
                return True #Les 3 motifs en dessous du motif sont identiques, c'est terminé
            else:
                cpt += 1
                nb += 1
    #Vérification au dessus
    cpt=1
    if(i-3>=0):
        while(s[i-cpt][j]==motif):
            if(nb==3):
                return True #Les 3 motifs au dessus du motif sont identiques, c'est terminé
            else:
                cpt += 1
                nb += 1
    
    return False #Si l'on sort des deux boucles while, cela signifie qu'il n'y a pas 4 motifs identiques alignés

#print(CheckColumn(grille,'X',6,4))

def CheckDiags(s,motif,i,j):
    nb_1=1
    #Vérification en diagonal bas/droite
    cpt=1
    if((i+3<=len(s)-1) and (j+3<=len(s)-1)):
        while(s[i+cpt][j+cpt]==motif):
            if(nb_1==3):
                return True #Les 3 motifs en diagonal bas/droite du motif sont identiques, c'est terminé
            else:
                cpt += 1
                nb_1 += 1
    nb_2=1
    #Vérification en diagonal bas/gauche
    cpt=1
    if((i+3<=len(s)-1) and (j-3>=0)):
        while(s[i+cpt][j-cpt]==motif):
            if(nb_2==3):
                return True #Les 3 motifs en diagonal bas/gauche du motif sont identiques, c'est terminé
            else:
                cpt += 1
                nb_2 += 1
    #Vérification en diagonal haut/gauche
    cpt=1
    if((i-3>=0) and (j-3>=0)):
        while(s[i-cpt][j-cpt]==motif):
            if(nb_1==3):
                return True #Les 3 motifs en diagonal haut/gauche du motif sont identiques, c'est terminé
            else:
                cpt += 1
                nb_1 += 1
    #Vérification en diagonal haut/droite
    cpt=1
    if((i-3>=0) and (j+3<=len(s)-1)):
        while(s[i-cpt][j+cpt]==motif):
            if(nb_2==3):
                return True #Les 3 motifs en diagonal haut/droite du motif sont identiques, c'est terminé
            else:
                cpt += 1
                nb_2 += 1
    
    
    return False #Si l'on sort des quatres boucles while, cela signifie qu'il n'y a pas 4 motifs identiques alignés

#print(CheckDiags(grille,'X',2,7))
#print(CheckDiags(grille,'X',6,4))

  
def TerminalTest(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if(s[i][j]!='.'):
                #On doit vérifier autour du motif si il y a 3 motifs qui s'alignent avec lui sur la ligne, sur la colonne et dans les diagonales
                if(CheckLine(s,s[i][j],i,j)==True):
                    return s[i][j]
                if(CheckColumn(s,s[i][j],i,j)==True):
                    return s[i][j]
                if(CheckDiags(s,s[i][j],i,j)==True):
                    return s[i][j]
    return '.'

#print(TerminalTest(grille))
    
def MyHeuristique(grille):
   
    #alignement deux pions : +10 / -10
    #alignement trois pions : +30 / -30
    #alignement trois pions avec case vide au milieu : +30 / -30
    #alignmenet trois pions sans voisin des deux côtés : +100 / -100
   
    scoreX=0 #Score pour l'IA 'X'
    scoreO=0 #Score pour l'IA 'O'
   
#count ligne, colonne
    for i in range(len(grille)):
        for j in range(len(grille)):
            
            
            if(grille[i][j]=='X'):
                
                    
                if(j+3 < len(grille) and grille[i][j+1] == 'X' and grille[i][j+2] == '.' and grille[i][j+3] == 'X'): #XX.X 
                    scoreX+=30
                if(j+3 < len(grille) and grille[i][j+1] == '.' and grille[i][j+2] == 'X' and grille[i][j+3] == 'X'): #X.XX
                    scoreX+=30
                    
                if(j+3<len(grille) and j-1 >=0 and grille[i][j+1] == 'X' and grille[i][j+2]== 'X' and grille[i][j+3]=='.' and grille[i][j-1]=='.'): #.XXX.
                    scoreX+=100
                    
                if(j+3<len(grille) and j-1 >=0 and grille[i][j+1] == 'X' and grille[i][j+2]== 'X' and grille[i][j-1]=='.' and grille[i][j+3]!='.'): #.XXX
                    scoreX+=30
                if(j+3<len(grille) and j-1 >=0 and grille[i][j+1] == 'X' and grille[i][j+2]== 'X' and grille[i][j+3]=='.' and grille[i][j-1]!='.'): #XXX.
                    scoreX+=30

                if(j+2 < len(grille) and j-1 >= 0 and grille[i][j+1] == 'X' and grille[i][j+2] == '.' and grille[i][j-1] == '.'): #.XX.
                    scoreX+=10
                
                #if(j+3 < len(grille) and grille[i][j+1] == 'X' and grille[i][j+2] == 'X' and grille[i][j+3] == 'X'): #XXXX 
                    #scoreX+=1000
                               
                #Colonne X
                
                if(j+3 < len(grille) and grille[j+1][i] == 'X' and grille[j+2][i] == '.' and grille[j+3][i] == 'X'): #XX.X 
                    scoreX+=30
                if(j+3 < len(grille) and grille[j+1][i] == '.' and grille[j+2][i] == 'X' and grille[j+3][i] == 'X'): #X.XX
                    scoreX+=30
                    
                if(j+3<len(grille) and j-1 >=0 and grille[j+1][i] == 'X' and grille[j+2][i]== 'X' and grille[j+3][i]=='.' and grille[j-1][i]=='.'): #.XXX.
                    scoreX+=100
                    
                if(j+3<len(grille) and j-1 >=0 and grille[j+1][i] == 'X' and grille[j+2][i]== 'X' and grille[j+3][i]!='.' and grille[j-1][i]=='.'): #.XXX
                    scoreX+=30
                if(j+3<len(grille) and j-1 >=0 and grille[j+1][i] == 'X' and grille[j+2][i]== 'X' and grille[j+3][i]=='.' and grille[j-1][i]!='.'): #XXX.
                    scoreX+=30

                if(j+2 < len(grille) and j-1 >= 0 and grille[j+1][i] == 'X' and grille[j+2][i] == '.' and grille[j-1][i] == '.'): #.XX.
                    scoreX+=10
                
                #if(j+3 < len(grille) and grille[j+1][i] == 'X' and grille[j+2][i] == 'X' and grille[j+3][i] == 'X'): #XXXX 
                    #scoreX+=1000
                    
                #On regarde chaque case
                #Diagonale Descandante Droites
            if(i+j<len(grille) and grille[j][i+j]=='X'):
                
                #if(i+j+3<len(grille) and grille[j+1][i+j+1]=='X' and grille[j+2][i+j+2]=='X' and grille[j+3][i+j+3]=='X'): #XXXX
                    #scoreX+=1000
                
                if(i+j+3<len(grille) and grille[j+1][i+j+1]=='.' and grille[j+2][i+j+2]=='X' and grille[j+3][i+j+3]=='X'): #X.XX
                    scoreX+=30
                if(i+j+3<len(grille) and grille[j+1][i+j+1]=='X' and grille[j+2][i+j+2]=='.' and grille[j+3][i+j+3]=='X'): #XX.X
                    scoreX+=30
                    
                if(i+j+3<len(grille) and j-1>=0 and grille[j+1][i+j+1]=='X' and grille[j+2][i+j+2]=='X' and grille[j+3][i+j+3]=='.' and grille[j-1][i+j-1]=='.'): #.XXX.
                    scoreX+=100
                    
                if(i+j+3<len(grille) and j-1>=0 and grille[j+1][i+j+1]=='X' and grille[j+2][i+j+2]=='X' and grille[j+3][i+j+3]!='.' and grille[j-1][i+j-1]=='.'): #.XXX
                    scoreX+=30
                if(i+j+3<len(grille) and j-1>=0 and grille[j+1][i+j+1]=='X' and grille[j+2][i+j+2]=='X' and grille[j+3][i+j+3]=='.' and grille[j-1][i+j-1]!='.'): #XXX.
                    scoreX+=30
                    
                if(i+j+2<len(grille) and j-1>=0 and grille[j+1][i+j+1]=='X' and grille[j+2][i+j+2]=='.' and grille[j-1][i+j-1]=='.'): #.XX.
                    scoreX+=10
                    
                    
            if(j-i>=0 and j!=j-i and j+3<len(grille) and grille[j][j-i]=='X'):
                
                #if(grille[j+1][j-i+1]=='X' and grille[j+2][j-i+2]=='X' and grille[j+3][j-i+3]=='X'): #XXXX
                    #scoreX+=1000
                
                if(grille[j+1][j-i+1]=='.' and grille[j+2][j-i+2]=='X' and grille[j+3][j-i+3]=='X'): #X.XX
                    scoreX+=30
                if(grille[j+1][j-i+1]=='X' and grille[j+2][j-i+2]=='.' and grille[j+3][j-i+3]=='X'): #XX.X
                    scoreX+=30
                    
                if(j-i-1>=0 and grille[j+1][j-i+1]=='X' and grille[j+2][j-i+2]=='X' and grille[j+3][j-i+3]=='.' and grille[j-1][j-i-1]=='.'): #.XXX.
                    scoreX+=100
                    
                if(j-i-1>=0 and grille[j+1][j-i+1]=='X' and grille[j+2][j-i+2]=='X' and grille[j+3][j-i+3]!='.' and grille[j-1][j-i-1]=='.'): #.XXX
                    scoreX+=30
                if(j-i-1>=0 and grille[j+1][j-i+1]=='X' and grille[j+2][j-i+2]=='X' and grille[j+3][j-i+3]=='.' and grille[j-1][j-i-1]!='.'): #XXX.
                    scoreX+=30
                    
                if(j-i-1>=0 and grille[j+1][j-i+1]=='X' and grille[j+2][j-i+2]=='.' and grille[j-1][j-i-1]=='.'): #.XX.
                    scoreX+=10
            
            if(i+j+3<len(grille) and grille[len(grille) - j - 1][i+j]=='X'):

                #if(grille[len(grille) - j - 1-1][i+j+1]=='X' and grille[len(grille) - j - 1-2][i+j+2]=='X' and grille[len(grille) - j - 1-3][i+j+3]=='X'): #XXXX
                    #scoreX+=1000
                
                if(grille[len(grille) - j - 1-1][i+j+1]=='.' and grille[len(grille) - j - 1-2][i+j+2]=='X' and grille[len(grille) - j - 1-3][i+j+3]=='X'): #X.XX
                    scoreX+=30
                if(grille[len(grille) - j - 1-1][i+j+1]=='X' and grille[len(grille) - j - 1-2][i+j+2]=='.' and grille[len(grille) - j - 1-3][i+j+3]=='X'): #XX.X
                    scoreX+=30
                    
                if(j>0 and i+j-1 >=0 and grille[len(grille) - j - 1-1][i+j+1]=='X' and grille[len(grille) - j - 1-2][i+j+2]=='X' and grille[len(grille) - j - 1-3][i+j+3]=='.' and grille[len(grille) - j -1+1][i+j-1]=='.'): #.XXX.
                    scoreX+=100
                    
                if(j>0 and i+j-1 >=0 and grille[len(grille) - j - 1-1][i+j+1]=='X' and grille[len(grille) - j - 1-2][i+j+2]=='X' and grille[len(grille) - j - 1-3][i+j+3]!='.' and grille[len(grille) - j -1+1][i+j-1]=='.'): #.XXX
                    scoreX+=30
                if(j>0 and i+j-1 >=0 and grille[len(grille) - j - 1-1][i+j+1]=='X' and grille[len(grille) - j - 1-2][i+j+2]=='X' and grille[len(grille) - j - 1-3][i+j+3]=='.' and grille[len(grille) - j -1+1][i+j-1]!='.'): #XXX.
                    scoreX+=30
                    
                if(i+j-1>=0 and j>0 and grille[len(grille) - j - 1-1][i+j+1]=='X' and grille[len(grille) - j - 1-2][i+j+2]=='.' and grille[len(grille) - j -1+1][i+j-1]=='.'): #.XX.
                    scoreX+=10
                    
            if(j-i>=0 and j!=j-i and len(grille)- j - 1 - 3>=0 and j-i + 3<len(grille) and grille[len(grille)- j - 1][j-i]=='X'):  

                #if(grille[len(grille)- j - 1 - 1][j-i + 1]=='X' and grille[len(grille)- j - 1 - 2][j-i + 2]=='X' and grille[len(grille)- j - 1 - 3][j-i + 3]=='X'): #XXXX
                    #scoreX+=1000
                
                if(grille[len(grille)- j - 1 - 1][j-i + 1]=='.' and grille[len(grille)- j - 1 - 2][j-i + 2]=='X' and grille[len(grille)- j - 1 - 3][j-i + 3]=='X'): #X.XX
                    scoreX+=30
                if(grille[len(grille)- j - 1 - 1][j-i + 1]=='X' and grille[len(grille)- j - 1 - 2][j-i + 2]=='.' and grille[len(grille)- j - 1 - 3][j-i + 3]=='X'): #XX.X
                    scoreX+=30
                    
                if(j-i - 1>=0 and grille[len(grille)- j - 1 - 1][j-i + 1]=='X' and grille[len(grille)- j - 1 - 2][j-i + 2]=='X' and grille[len(grille)- j - 1 - 3][j-i + 3]=='.' and grille[len(grille)- j - 1 + 1][j-i - 1]=='.'): #.XXX.
                    scoreX+=100
                    
                if(j-i - 1>=0 and grille[len(grille)- j - 1 - 1][j-i + 1]=='X' and grille[len(grille)- j - 1 - 2][j-i + 2]=='X' and grille[len(grille)- j - 1 - 3][j-i + 3]!='.' and grille[len(grille)- j - 1 + 1][j-i - 1]=='.'): #.XXX
                    scoreX+=30
                if(j-i - 1>=0 and grille[len(grille)- j - 1 - 1][j-i + 1]=='X' and grille[len(grille)- j - 1 - 2][j-i + 2]=='X' and grille[len(grille)- j - 1 - 3][j-i + 3]=='.' and grille[len(grille)- j - 1 + 1][j-i - 1]!='.'): #XXX.
                    scoreX+=30
                    
                if(j-i - 1>=0 and j>0 and grille[len(grille)- j - 1 - 1][j-i + 1]=='X' and grille[len(grille)- j - 1 - 2][j-i + 2]=='.' and grille[len(grille)- j - 1 + 1][j-i - 1]=='.'): #.XX.
                    scoreX+=10
                   
            if(grille[i][j]=='O'):
                
                    
                if(j+3 < len(grille) and grille[i][j+1] == 'O' and grille[i][j+2] == '.' and grille[i][j+3] == 'O'): #XX.X 
                    scoreO+=30
                if(j+3 < len(grille) and grille[i][j+1] == '.' and grille[i][j+2] == 'O' and grille[i][j+3] == 'O'): #X.XX
                    scoreO+=30
                    
                if(j+3<len(grille) and j-1 >=0 and grille[i][j+1] == 'O' and grille[i][j+2]== 'O' and grille[i][j+3]=='.' and grille[i][j-1]=='.'): #.XXX.
                    scoreO+=100
                    
                if(j+3<len(grille) and j-1 >=0 and grille[i][j+1] == 'O' and grille[i][j+2]== 'O' and grille[i][j-1]=='.' and grille[i][j+3]!='.'): #.XXX
                    scoreO+=30
                if(j+3<len(grille) and j-1 >=0 and grille[i][j+1] == 'O' and grille[i][j+2]== 'O' and grille[i][j+3]=='.' and grille[i][j-1]!='.'): #XXX.
                    scoreO+=30

                if(j+2 < len(grille) and j-1 >= 0 and grille[i][j+1] == 'O' and grille[i][j+2] == '.' and grille[i][j-1] == '.'): #.XX.
                    scoreO+=10
                
                #if(j+3 < len(grille) and grille[i][j+1] == 'O' and grille[i][j+2] == 'O' and grille[i][j+3] == 'O'): #XXXX 
                    #scoreO+=1000
                               
                #Colonne X
                
                if(j+3 < len(grille) and grille[j+1][i] == 'O' and grille[j+2][i] == '.' and grille[j+3][i] == 'O'): #XX.X 
                    scoreO+=30
                if(j+3 < len(grille) and grille[j+1][i] == '.' and grille[j+2][i] == 'O' and grille[j+3][i] == 'O'): #X.XX
                    scoreO+=30
                    
                if(j+3<len(grille) and j-1 >=0 and grille[j+1][i] == 'O' and grille[j+2][i]== 'O' and grille[j+3][i]=='.' and grille[j-1][i]=='.'): #.XXX.
                    scoreO+=100
                    
                if(j+3<len(grille) and j-1 >=0 and grille[j+1][i] == 'O' and grille[j+2][i]== 'O' and grille[j+3][i]!='.' and grille[j-1][i]=='.'): #.XXX
                    scoreO+=30
                if(j+3<len(grille) and j-1 >=0 and grille[j+1][i] == 'O' and grille[j+2][i]== 'O' and grille[j+3][i]=='.' and grille[j-1][i]!='.'): #XXX.
                    scoreO+=30

                if(j+2 < len(grille) and j-1 >= 0 and grille[j+1][i] == 'O' and grille[j+2][i] == '.' and grille[j-1][i] == '.'): #.XX.
                    scoreO+=10
                
                #if(j+3 < len(grille) and grille[j+1][i] == 'O' and grille[j+2][i] == 'O' and grille[j+3][i] == 'O'): #XXXX 
                    #scoreO+=1000
                    
                #On regarde chaque case
                #Diagonale Descandante Droites
            if(i+j<len(grille) and grille[j][i+j]=='O'):
                
                #if(i+j+3<len(grille) and grille[j+1][i+j+1]=='O' and grille[j+2][i+j+2]=='O' and grille[j+3][i+j+3]=='O'): #XXXX
                    #scoreO+=1000
                
                if(i+j+3<len(grille) and grille[j+1][i+j+1]=='.' and grille[j+2][i+j+2]=='O' and grille[j+3][i+j+3]=='O'): #X.XX
                    scoreO+=30
                if(i+j+3<len(grille) and grille[j+1][i+j+1]=='O' and grille[j+2][i+j+2]=='.' and grille[j+3][i+j+3]=='O'): #XX.X
                    scoreO+=30
                    
                if(i+j+3<len(grille) and j-1>=0 and grille[j+1][i+j+1]=='O' and grille[j+2][i+j+2]=='O' and grille[j+3][i+j+3]=='.' and grille[j-1][i+j-1]=='.'): #.XXX.
                    scoreO+=100
                    
                if(i+j+3<len(grille) and j-1>=0 and grille[j+1][i+j+1]=='O' and grille[j+2][i+j+2]=='O' and grille[j+3][i+j+3]!='.' and grille[j-1][i+j-1]=='.'): #.XXX
                    scoreO+=30
                if(i+j+3<len(grille) and j-1>=0 and grille[j+1][i+j+1]=='O' and grille[j+2][i+j+2]=='O' and grille[j+3][i+j+3]=='.' and grille[j-1][i+j-1]!='.'): #XXX.
                    scoreO+=30
                    
                if(i+j+2<len(grille) and j-1>=0 and grille[j+1][i+j+1]=='O' and grille[j+2][i+j+2]=='.' and grille[j-1][i+j-1]=='.'): #.XX.
                    scoreO+=10
                    
                    
            if(j-i>=0 and j!=j-i and j+3<len(grille) and grille[j][j-i]=='O'):
                
                #if(grille[j+1][j-i+1]=='O' and grille[j+2][j-i+2]=='O' and grille[j+3][j-i+3]=='O'): #XXXX
                    #scoreO+=1000
                
                if(grille[j+1][j-i+1]=='.' and grille[j+2][j-i+2]=='O' and grille[j+3][j-i+3]=='O'): #X.XX
                    scoreO+=30
                if(grille[j+1][j-i+1]=='O' and grille[j+2][j-i+2]=='.' and grille[j+3][j-i+3]=='O'): #XX.X
                    scoreO+=30
                    
                if(j-i-1>=0 and grille[j+1][j-i+1]=='O' and grille[j+2][j-i+2]=='O' and grille[j+3][j-i+3]=='.' and grille[j-1][j-i-1]=='.'): #.XXX.
                    scoreO+=100
                    
                if(j-i-1>=0 and grille[j+1][j-i+1]=='O' and grille[j+2][j-i+2]=='O' and grille[j+3][j-i+3]!='.' and grille[j-1][j-i-1]=='.'): #.XXX
                    scoreO+=30
                if(j-i-1>=0 and grille[j+1][j-i+1]=='O' and grille[j+2][j-i+2]=='O' and grille[j+3][j-i+3]=='.' and grille[j-1][j-i-1]!='.'): #XXX.
                    scoreO+=30
                    
                if(j-i-1>=0 and grille[j+1][j-i+1]=='O' and grille[j+2][j-i+2]=='.' and grille[j-1][j-i-1]=='.'): #.XX.
                    scoreO+=10
            
            if(i+j+3<len(grille) and grille[len(grille) - j - 1][i+j]=='O'):

                #if(grille[len(grille) - j - 1-1][i+j+1]=='O' and grille[len(grille) - j - 1-2][i+j+2]=='O' and grille[len(grille) - j - 1-3][i+j+3]=='O'): #XXXX
                    #scoreO+=1000
                
                if(grille[len(grille) - j - 1-1][i+j+1]=='.' and grille[len(grille) - j - 1-2][i+j+2]=='O' and grille[len(grille) - j - 1-3][i+j+3]=='O'): #X.XX
                    scoreO+=30
                if(grille[len(grille) - j - 1-1][i+j+1]=='O' and grille[len(grille) - j - 1-2][i+j+2]=='.' and grille[len(grille) - j - 1-3][i+j+3]=='O'): #XX.X
                    scoreO+=30
                    
                if(j>0 and i+j-1 >=0 and grille[len(grille) - j - 1-1][i+j+1]=='O' and grille[len(grille) - j - 1-2][i+j+2]=='O' and grille[len(grille) - j - 1-3][i+j+3]=='.' and grille[len(grille) - j -1+1][i+j-1]=='.'): #.XXX.
                    scoreO+=100
                    
                if(j>0 and i+j-1 >=0 and grille[len(grille) - j - 1-1][i+j+1]=='O' and grille[len(grille) - j - 1-2][i+j+2]=='O' and grille[len(grille) - j - 1-3][i+j+3]!='.' and grille[len(grille) - j -1+1][i+j-1]=='.'): #.XXX
                    scoreO+=30
                if(j>0 and i+j-1 >=0 and grille[len(grille) - j - 1-1][i+j+1]=='O' and grille[len(grille) - j - 1-2][i+j+2]=='O' and grille[len(grille) - j - 1-3][i+j+3]=='.' and grille[len(grille) - j -1+1][i+j-1]!='.'): #XXX.
                    scoreO+=30
                    
                if(i+j-1>=0 and j>0 and grille[len(grille) - j - 1-1][i+j+1]=='O' and grille[len(grille) - j - 1-2][i+j+2]=='.' and grille[len(grille) - j -1+1][i+j-1]=='.'): #.XX.
                    scoreO+=10
                    
            if(j-i>=0 and j!=j-i and len(grille)- j - 1 - 3>=0 and j-i + 3<len(grille) and grille[len(grille)- j - 1][j-i]=='O'):  

                #if(grille[len(grille)- j - 1 - 1][j-i + 1]=='O' and grille[len(grille)- j - 1 - 2][j-i + 2]=='O' and grille[len(grille)- j - 1 - 3][j-i + 3]=='O'): #XXXX
                    #scoreO+=1000
                
                if(grille[len(grille)- j - 1 - 1][j-i + 1]=='.' and grille[len(grille)- j - 1 - 2][j-i + 2]=='O' and grille[len(grille)- j - 1 - 3][j-i + 3]=='O'): #X.XX
                    scoreO+=30
                if(grille[len(grille)- j - 1 - 1][j-i + 1]=='O' and grille[len(grille)- j - 1 - 2][j-i + 2]=='.' and grille[len(grille)- j - 1 - 3][j-i + 3]=='O'): #XX.X
                    scoreO+=30
                    
                if(j-i - 1>=0 and grille[len(grille)- j - 1 - 1][j-i + 1]=='O' and grille[len(grille)- j - 1 - 2][j-i + 2]=='O' and grille[len(grille)- j - 1 - 3][j-i + 3]=='.' and grille[len(grille)- j - 1 + 1][j-i - 1]=='.'): #.XXX.
                    scoreO+=100
                    
                if(j-i - 1>=0 and grille[len(grille)- j - 1 - 1][j-i + 1]=='O' and grille[len(grille)- j - 1 - 2][j-i + 2]=='O' and grille[len(grille)- j - 1 - 3][j-i + 3]!='.' and grille[len(grille)- j - 1 + 1][j-i - 1]=='.'): #.XXX
                    scoreO+=30
                if(j-i - 1>=0 and grille[len(grille)- j - 1 - 1][j-i + 1]=='O' and grille[len(grille)- j - 1 - 2][j-i + 2]=='O' and grille[len(grille)- j - 1 - 3][j-i + 3]=='.' and grille[len(grille)- j - 1 + 1][j-i - 1]!='.'): #XXX.
                    scoreO+=30
                    
                if(j-i - 1>=0 and j>0 and grille[len(grille)- j - 1 - 1][j-i + 1]=='O' and grille[len(grille)- j - 1 - 2][j-i + 2]=='.' and grille[len(grille)- j - 1 + 1][j-i - 1]=='.'): #.XX.
                    scoreO+=10
                   
    return scoreX - scoreO
"""    
def Minimax(grille, depth, isMaximizingPlayer, alpha = -1000, beta = 1000, score=0):
    
    if(len(Actions(grille))==0):
        score = 0
        return score
    if(TerminalTest(grille) == 'X'):
        score = 1000
        return score
    if(TerminalTest(grille) == 'O'):
        score = -1000
        return score
    if(depth==1):
        return score
    
    actionsproches = ActionsProches(grille)
    
    if isMaximizingPlayer : #max pour le joueur IA
        bestScore = -1000
        
        
        for i,j in actionsproches:
            grille[i][j]='X'
            score += Minimax(grille, depth +1, False, alpha, beta)
            grille[i][j] = '.'
            #print(score)
            bestScore = max(score, bestScore)
            alpha = max(alpha, score)
            if alpha>= beta :
                break     
            
        return bestScore

    else : #min proba pour le joueur humain
        bestScore = 1000
        
        for i,j in actionsproches:
            grille[i][j] = 'O'
            score += Minimax(grille, depth+1, True, alpha, beta)
            grille[i][j] = '.'
            #print(score)
            bestScore = min(score, bestScore)
            beta = min(beta, score)
            if alpha >=beta:
                break                
                                    
        return bestScore

"""

def MinMax_Decision(s,depth, maximizingPlayer,alpha = -1000, beta = 1000): #Pour utiliser la fonction MinMax_Decision, on envoie un état futur à éventuellement choisir, puis on stock dans un dictionnaire la valeur de l'état

    l = ActionsProches(s)

    if(TerminalTest(s)!='.' or len(Actions(s))==0):
        if(TerminalTest(s) == 'X'):
            if(maximizingPlayer==True):
                score = 1000
            else:
                score = -1000
            return score
        else:
            if(TerminalTest(s) == 'X'):
                if(maximizingPlayer==False):
                    score = 1000
                else:
                    score = -1000
                return score
            else:
                return 0

    else:
        if(depth==0):
            if(maximizingPlayer==True):
                score = MyHeuristique(s)
            else:
                score = - MyHeuristique(s)
            return score                
        
        else:
            if(maximizingPlayer==True):
                maxEval=-10**6
                for i, j in l:
                    s[i][j]='X'
                    Eval = MinMax_Decision(s, depth -1, False, alpha, beta)
                    s[i][j]='.'
                    maxEval = max(maxEval,Eval)
                    alpha = max(alpha, Eval)
                    if alpha>= beta :
                        break
                    
                return maxEval
            else:
                minEval=10**6
                for i,j in l:
                    s[i][j]='O'
                    Eval = MinMax_Decision(s, depth -1, True, alpha, beta)
                    s[i][j]='.'
                    minEval = min(minEval, Eval)
                    beta = min(beta, Eval)
                    if alpha >=beta:
                        break
                    
                return minEval
#print(MinMax_Decision(grille, 1, True))

def Adversaire(s):
    l = Actions(s)
    i = int(input("Veuillez choisir une ligne entre 0 et 11 :"))
    j = int(input("Veuillez choisir une colonne entre 0 et 11 :"))
    a = tuple([i,j])
    action = Action('O',a)
    while(action.coordonnees not in l):
        i = int(input("Veuillez choisir une ligne entre 0 et 11 :"))
        j = int(input("Veuillez choisir une colonne entre 0 et 11 :"))
        a = tuple([i,j])
        action = Action('O',a)
    s = Result(s,action)
    return s
"""
grille = Grille12x12()
while(len(Actions(grille))!=0 and TerminalTest(grille)=='.'):
    AffichageGrille(grille)
    grille = Adversaire(grille)
    AffichageGrille(grille)
    print(MyHeuristique(grille))
    if(TerminalTest(grille)!='.'):
        print(MinMax_Decision(grille,1, False))
"""
def IA(grille):
    start = time.time()
    bestScore = -1000
    ligne,colonne =-1,-1
    grillevirtuelle = grille
    end = time.time()
    for i,j in ActionsProches(grillevirtuelle):
        end = time.time()
        if(end-start<=9.8):
            grillevirtuelle[i][j] = 'X'
            #print('--------------------------------------------------------------')
            score = MinMax_Decision(grillevirtuelle,2, True)
            #print(i,j)
            #print('SCORE : ', score)
            
            grillevirtuelle[i][j] = "."
            if score>bestScore :
                bestScore = score
                #print('best score', score, i, j)
                ligne,colonne = i,j
                if score == 1000 : break
        else:
            break
    #print("index", ligne, colonne)
    grille[ligne][colonne] = 'X'
    end = time.time()
    print(end-start)
    return grille
    
        
#AffichageGrille(IA(grille))


def New_game():
    nb_coup = 0
    grille = Grille12x12()
    print("Adversaire : Tapez 1\nIA : Tapez 2\n")
    joueur = input()
    while(joueur!="1" and joueur!="2"):
        print("Adversaire : Tapez 1\nIA : Tapez 2\n")
        joueur = input()
        
    if(joueur=="1"): #C'est l'adversaire qui commence  
        
        while(len(Actions(grille))!=0 and TerminalTest(grille)=='.'):
             AffichageGrille(grille)
             print("\nAdversaire, c'est ton tour !\n")
             grille = Adversaire(grille)
             AffichageGrille(grille)
             if(TerminalTest(grille)!='.'):
                 print("Fin de la partie")
             else:
                 print("\nC'est au tour de l'IA !\n")
                 grille = IA(grille)
             
        if(TerminalTest(grille)=='X'):
            print("\nVictoire de l'IA !")
        elif(len(Actions(grille))==0):
            #Egalité on renvoie 0
            print("\nMatch nul...")
        else:
            print("\nVictoire de l'adversaire")
        
    else: #C'est l'IA qui commence
        
        while(len(Actions(grille))!=0 and TerminalTest(grille)=='.'):
            AffichageGrille(grille)
            print("\nC'est au tour de l'IA !\n")
            if(nb_coup==0):
                i = rd.randint(2,9)
                j = rd.randint(2,9)
                grille=Result(grille,Action('X',(i,j)))
                AffichageGrille(grille)
                print("\nAdversaire, c'est ton tour !\n")
                grille = Adversaire(grille)
                nb_coup += 1
            else:   
                grille = IA(grille)
                AffichageGrille(grille)
                if(TerminalTest(grille)!='.'):
                    print("Fin de la partie")
                else:
                    print("\nAdversaire, c'est ton tour !\n")
                    grille = Adversaire(grille)
             
        if(TerminalTest(grille)=='X'):
            print("\nVictoire de l'IA !")
        elif(len(Actions(grille))==0):
            #Egalité on renvoie 0
            print("\nMatch nul...")
        else:
            print("\nVictoire de l'adversaire")
            
    print("Partie Terminée")
        
New_game()

"""
grille = Grille12x12()

def VerifDiag(s):
    for i in range(len(s)):
        for j in range(len(s)):
            print(i,j)
            if(i+j+3<len(s)):
                s[j][i+j]='X'
                s[j+1][i+j+1]='X'
                s[j+2][i+j+2]='X'
                s[j+3][i+j+3]='X'
            AffichageGrille(s)
            if(j-i>=0 and j!=j-i and j+3<len(s)):  
                s[j][j-i]='O'
                s[j+1][j-i+1]='O'
                s[j+2][j-i+2]='O'
                s[j+3][j-i+3]='O'
            AffichageGrille(s)

#VerifDiag(grille)    
        
def VerifDiag2(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if(i+j+3<len(s)):
                print(len(s) - j - 1+1,i+j+1)
                s[len(s) - j - 1][i+j]='X'
                s[len(s) - j - 1-1][i+j+1]='X'
                s[len(s) - j - 1-2][i+j+2]='X'
                s[len(s) - j - 1-3][i+j+3]='X'
            AffichageGrille(s)
            if(j-i>=0 and j!=j-i and len(s)- j - 1 - 3>=0 and j-i + 3<len(s)):  
                s[len(s)- j - 1][j-i]='O'
                s[len(s)- j - 1 - 1][j-i + 1]='O'
                s[len(s)- j - 1 - 2][j-i + 2]='O'
                s[len(s)- j - 1 - 3][j-i + 3]='O'

            AffichageGrille(s)

VerifDiag2(grille) 
"""