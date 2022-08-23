def binarysearch(my_list,key):
    low = 0
    high = len(my_list)-1
    found = False
    while low<=high and not found:
        mid = (low+high)//2
        
        if key == my_list[mid]:
            found = True
        elif key > my_list[mid]:
            low = mid+1
        else:
            high = mid-1
    if found == True:
        print("key found")
    else:
        print("key not found")

    
lst=[23,1,2,3,5,6]
lst.sort()
print(lst)
key =int(input("enter key:"))
binarysearch(lst,key)
