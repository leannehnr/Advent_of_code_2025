'''
Advent of code day 3
'''

lignes = []

def data_sort(file):
    global lignes
    with open(file, "r", encoding="utf-8") as f:
        for ligne in f:
            lignes.append(ligne)
    for i in range (0, len(lignes)):
        lignes[i]=lignes[i].strip()
    return lignes

def maxi(a, b, c): 
    if(a>=b and a>=c): 
        return a
    elif(b>=a and b>=c): 
        return b
    else: 
        return c

def part1():
    global lignes
    scores = 0

    for ligne in lignes: 
        score = []

        for i in ligne : 
            if len(score) < 2: 
                score.append(i)
            else : 
                tmp1, tmp2 = [], []
                tmp1.append(score[0])
                tmp1.append(i)
                tmp2.append(score[1])
                tmp2.append(i)
                tmp1_int, tmp2_int, score_int = int(tmp1[0])*10+int(tmp1[1]), int(tmp2[0])*10+int(tmp2[1]), int(score[0])*10+int(score[1])
                score_int = maxi(tmp1_int, tmp2_int, score_int)
                score = [str(int(score_int/10)), str(int(score_int%10))]
        scores += score_int
        print(scores)

def best12(s):
    remove = len(s) - 12
    stack = []

    for c in s:
        while remove > 0 and stack and stack[-1] < c:
            stack.pop()
            remove -= 1
        stack.append(c)

    # si on n’a pas retiré assez
    return "".join(stack[:12])


def part2():
    total = 0
    for ligne in lignes:
        best = int(best12(ligne.strip()))
        total += best
    print(total)


data_sort('input_day3.txt')
print(lignes)
part1()
part2()
# test : 3121910778619
# to low : 166345822896393
