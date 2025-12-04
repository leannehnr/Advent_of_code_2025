'''
Docstring pour day1
'''

sens, nombre = [], []

def data_sort(file):
    global sens, nombre
    with open(file, "r", encoding="utf-8") as f:
        for ligne in f:
            inter = []
            for char in ligne:
                if char.isalpha():
                    sens.append(char)
                elif char.isdigit():
                    inter.append(char)
            if(len(inter)==1):
                nombre.append(int(inter[0]))
            elif(len(inter)==2):
                nombre.append(int(inter[0])*10+int(inter[1]))
            elif(len(inter)==3):
                nombre.append(int(inter[0])*100 +int(inter[1])*10+int(inter[2]))
    return sens, nombre

def main():
    global sens, nombre
    file = "input_test.txt"
    sens, nombre = data_sort(file)
    res = 50
    cmp = 0
    if(len(sens)==len(nombre)):
        for i, j in zip(sens, nombre):
            if(i=='R'):
                while j!=0:
                    res = (res + 1)%100
                    if (res ==0):
                        cmp+=1
                    j-=1
            elif(i=='L'):
                while j!=0:
                    res = (res - 1)%100
                    if (res ==0):
                        cmp+=1
                    j-=1
            
            #if res == 0:
            #    cmp+=1

    else :
        print("Erreur data size")
        print(len(sens), len(nombre))
    
    print(cmp)
    

main()