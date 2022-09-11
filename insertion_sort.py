from turtle import pos


def insertion_sort(list_to_order):
    for i in range(2, len(list_to_order)):
        chave = list_to_order[i]
        j = i - 1
        while j > 0 and list_to_order[j] > chave:
            list_to_order[j + 1] = list_to_order[j]
            j = j - 1
        list_to_order[j + 1] = chave
    print(list_to_order)
    
list_to_order = [1,15,35,23,7,7,21,3,9]
insertion_sort(list_to_order)
            