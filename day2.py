'''
Docstring pour day1
'''

id1, id2 = [], []

def data_sort(file):
    global id1, id2
    with open(file, "r", encoding="utf-8") as f:
        for ligne in f:
            inter = []
            inter = ligne.split(',')
    z=[]
    for i in inter:
        z = i.split('-')
        id1.append(z[0])
        id2.append(z[1])
    print(inter)
    return id1, id2

def split_in_n_parts(s, n):
    L = len(s)
    if L % n != 0:
        raise ValueError("La chaîne ne peut pas être divisée en n parties égales")
    
    size = L // n
    return [s[i:i+size] for i in range(0, L, size)]

def part1(): 
    ## C'est une erreur si : 
    ## l'id est un nombre qui se repete (ex :11, 123123)
    ## l'id a un 0 en premier caractère 
    ## On peut soustraire une quantité à un id et l'ajouter à l'autre et donc obtenir deux fois le même id 
    global id1, id2
    wrong_id=0
    if(len(id1)==len(id2)):
        for start, stop in zip(id1, id2):
            if start[0]=='0' or stop[0]=='0':
                if start[0]=='0':
                    wrong_id+=int(start)
                    print(start)
                if stop[0]=='0':
                    wrong_id+=int(stop)
                    print(stop)

            for i in range (int(start), int(stop)+1):
                i = str(i)
                for n in range (1, len(i)+1) : 
                    if len(i) % n == 0:
                        sub_i = split_in_n_parts(i, n)
                        #print(n, sub_i)

                        cmp = 0
                        for k in range (0, len(sub_i)-1) :
                            if(sub_i[k]==sub_i[k+1]):
                                cmp+=1
                            else : 
                                cmp=0
                                break
                        if cmp > 0:
                            wrong_id+=int(i)
                            print(i)
                            break

    else:
        print("Erreur longueur des données")
    print(wrong_id)

# test value : 4174379265

def main():
    global id1, id2
    data_sort('input_day2.txt')
    part1()

main()


# mon res (faux) : 7575957658
