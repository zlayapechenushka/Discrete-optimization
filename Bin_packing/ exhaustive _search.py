import sys

def total_low_bound(items, total_knapsack_volume, number_of_items):
    bound = 0
    for i in range(number_of_items):
        if total_knapsack_volume - items[i][0] >= 0:
            total_knapsack_volume -= items[i][0]
            bound += items[i][1]
    return bound

def local_up_bound(items, n, current_volume, value, total_knapsack_volume):
    return value + (total_knapsack_volume - current_volume) * items[n][1]/items[n][0]

def enumeration(items, current_volume, total_volume, n = 0 , value = 0):
    global answer
    if current_volume > total_volume:
        return
    if value > answer:
        answer = value
    if n == len(items):
        return
    
    if local_up_bound(items, n, current_volume, value, total_volume) > answer:
        enumeration(items, current_volume, total_volume, n + 1, value)
        enumeration(items, current_volume + items[n][0], total_volume, n + 1, value + items[n][1])

if __name__ == '__main__':
    sys.setrecursionlimit(20000)

    total_knapsack_volume = int(input())
    number_of_items = int(input())
    items = tuple(list(map(int, input().split())) for i in range(number_of_items))
    items = sorted(items, key = lambda x: -x[1]/x[0])
    
    answer = total_low_bound(items, total_knapsack_volume, number_of_items)

    enumeration(items, 0, total_knapsack_volume)

    print(answer)