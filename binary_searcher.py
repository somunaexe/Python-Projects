# def myFunc(e):
#   return e['year']

def binarySearch(list, element):
    list.sort()
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start <= end):
        print("Step", steps, ":", str(list[start:end+1]))

        steps = steps + 1
        middle = (start + end) // 2

        if element == list[middle]:
           return middle
        if element < list[middle]:
           end = middle - 1
        else:
           start = middle + 1

    return -1

my_list = [3, 2, 4, 7, 6, 5, 8, 9, 1, 10]
binarySearch(my_list, 9)