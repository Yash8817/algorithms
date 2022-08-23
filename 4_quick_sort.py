def pivot_position(lst,first,last):
    pivot = lst[first]
    left = first +1
    right = last
    while True:
        while left <= right and lst[left] <= right:
            left += 1
        while left <= right and lst[right] >= pivot:
            right =right -1
        if right<left:
            break
        else:
            lst[left],lst[right] = lst[right],lst[left]
    lst[first],lst[right] = lst[right],lst[first]
    return right

def quicksort(lst,first,last):
    if first < last:
        p = pivot_position(lst,first,last)
        quicksort(lst,first,p-1)
        quicksort(lst,p+1,last)
    

lst = [2,45,78,21,45,87,98,10,4,0]
n = len(lst)
quicksort(lst,0,n-1)
print(lst)
