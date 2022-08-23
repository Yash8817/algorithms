def mergesort(lst):
    if len(lst)>1:
        mid = len(lst)//2
        left_list = lst[:mid]
        right_list = lst[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i=0
        j=0
        k=0
        while i<len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                lst[k] = left_list[i]
                i += 1
                k += 1
            else:
                lst[k] = right_list[j]
                j += 1
                k += 1
        while i < len(left_list):
            lst[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            lst[k] = right_list[j]
            j += 1
            k += 1

n = int(input("Enter number of element:"))
lst = [int(input()) for x in range(n)]
mergesort(lst)
print(lst)
