def bubble_sort(list_to_order):
    for i in range(len(list_to_order) - 1):
        for j in range(len(list_to_order) - i - 1):
            if list_to_order[j] > list_to_order[j+1]:
                list_to_order[j], list_to_order[j+1] = list_to_order[j+1], list_to_order[j]
    print(list_to_order)

list_to_order = [1,15,35,23,7,7,21,3,9]
bubble_sort(list_to_order)