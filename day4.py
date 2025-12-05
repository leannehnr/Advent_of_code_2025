'''
Advent of code day 4
'''

import copy


tableau = []

def data_sort(file):
    global tableau

    with open(file, "r", encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.strip("\n")     # retire uniquement le saut de ligne
            tableau.append(list(ligne))    # transforme la ligne en liste de caractères
    return tableau


def part1(): 
    global tableau
    res = 2
    cmp_res = 0
    while res!=0:
        res = 0
        tab_copy = copy.deepcopy(tableau)    
        for i in range (0, len(tableau)): 
            for j in range (0, len(tableau[0])): 
                if (i==0 and j==0) or (i==0 and j==len(tableau[0])-1) or (i==len(tableau)-1 and j==0) or (i==len(tableau)-1 and j==len(tableau[0])-1) : 
                    if tableau[i][j]=='@' : tab_copy[i][j]='x'
                elif(i==len(tableau)-1): 
                    cmp=-1
                    current_line = [tableau[i-1][j-1], tableau[i-1][j], tableau[i-1][j+1], tableau[i][j-1], tableau[i][j], tableau[i][j+1]]
                    if (tableau[i][j]=='@'):
                        for k in current_line: 
                            if k=='@' : cmp+=1
                        if cmp<4 : tab_copy[i][j]='x'
                elif(j==len(tableau[0])-1):
                    cmp=-1
                    current_line = [tableau[i-1][j-1], tableau[i-1][j], tableau[i][j-1], tableau[i][j], tableau[i+1][j-1], tableau[i+1][j]]
                    if (tableau[i][j]=='@'):
                        for k in current_line: 
                            if k=='@' : cmp+=1
                        if cmp<4 : tab_copy[i][j]='x'
                elif (i==0): 
                    cmp=-1
                    current_line = [tableau[i][j-1], tableau[i][j], tableau[i][j+1], tableau[i+1][j-1], tableau[i+1][j], tableau[i+1][j+1]]
                    if (tableau[i][j]=='@'):
                        for k in current_line: 
                            if k=='@' : cmp+=1
                        if cmp<4 : tab_copy[i][j]='x'
                elif(j==0):
                    cmp=-1
                    current_line = [tableau[i-1][j], tableau[i-1][j+1], tableau[i][j], tableau[i][j+1], tableau[i+1][j], tableau[i+1][j+1]]
                    if (tableau[i][j]=='@'):
                        for k in current_line: 
                            if k=='@' : cmp+=1
                        if cmp<4 : tab_copy[i][j]='x'
                else : 
                    cmp=-1
                    current_line = [tableau[i-1][j-1], tableau[i-1][j], tableau[i-1][j+1], tableau[i][j-1], tableau[i][j], tableau[i][j+1], tableau[i+1][j-1], tableau[i+1][j], tableau[i+1][j+1]]
                    if (tableau[i][j]=='@'):
                        for k in current_line: 
                            if k=='@' : cmp+=1
                        if cmp<4 : tab_copy[i][j]='x'
        
        for i in range (0, len(tab_copy)): 
            for j in range (0, len(tab_copy[0])): 
                if tab_copy[i][j]=='x' : res +=1
        tableau = tab_copy
        for i in range (0, len(tab_copy)): 
            for j in range (0, len(tab_copy[0])): 
                if(tableau[i][j]=='x') : tableau[i][j]='.'
        print(res)
        cmp_res+=res
    print(cmp_res)
    
data_sort("input_day4.txt")
part1()
#print(tableau)
