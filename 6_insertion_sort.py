def insertionsort(my_list):
    for index in range(1,len(my_list)):
        curr_element = my_list[index]
        pos = index
        while curr_element < my_list[pos-1] and pos >0:
            my_list[pos] = my_list[pos-1]
            pos -= 1

            my_list[pos] = curr_element
    



lst = [1,12,45,87,878,20,1,4]
insertionsort(lst)
print(lst)
