def selection_sort(list_to_order):
    list_size = len(list_to_order)
    for i in range(list_size-1):
        min_index = i
        for j in range(i, list_size):
            if list_to_order[j] < list_to_order[min_index]:
                min_index = j
        if list_to_order[i] > list_to_order[min_index]:
            list_to_order[i], list_to_order[min_index] = list_to_order[min_index], list_to_order[i]
    print(list_to_order)

list_to_order = [1,15,35,23,7,7,21,3,9]
selection_sort(list_to_order)

