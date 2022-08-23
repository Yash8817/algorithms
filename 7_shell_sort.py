def shellsort(my_list):
    gap = len(my_list) // 2
    while gap >0:
        for index in range(gap,len(my_list)):
            current_ele = my_list[index]
            pos = index
            while pos >= gap and current_ele <my_list[pos-gap]:
                my_list[pos]=my_list[pos-gap]
                pos -= gap
            my_list[pos] =current_ele
        gap =gap//2

n = int(input("how many element you want"))
lst = [int(input()) for x in range(n)]
shellsort(lst)
print(lst)
