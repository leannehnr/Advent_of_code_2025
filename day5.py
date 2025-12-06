'''
Advent of code day 5
'''

range_data, food = [], []

def data_sort(file):
    global range_data, food
    with open(file, "r", encoding="utf-8") as f:
        for ligne in f:
            interval = []
            ligne = ligne.strip("\n")
            if(ligne.__contains__('-')):
                interval = ligne.split('-')
                range_data.append(interval)
            else : 
                food.append(ligne)
    food.remove(food[0])
    return range_data, food

def part1(): 
    global range_data, food
    cmp = 0
    for data in food : 
        for interval in range_data : 
            data_int = int(data)
            mini = int(interval[0])
            maxi = int(interval[1])
            if data_int >= mini and data_int<=maxi : 
                cmp+=1
                break
    print(cmp)

def part2():
    global range_data
    intervals = sorted((int(mini), int(maxi)) for mini, maxi in range_data)

    merged = []
    cur_start, cur_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= cur_end + 1:  
            cur_end = max(cur_end, end)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end
    merged.append((cur_start, cur_end))

    total = sum(maxi - mini + 1 for mini, maxi in merged)
    print(total)


data_sort("input_day5.txt")
print(range_data)
print(food)
#part1()
part2()
