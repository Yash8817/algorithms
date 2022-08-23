n = int(input("how many values you want:"))
lst = [ int(input("enter value:")) for i in range(n) ]

for i in range(len(lst)-1):
    for j in range(len(lst)-1-i):
        if lst[j] > lst[j+1]:
            lst[j] , lst[j+1] =lst[j+1],lst[j]
print(lst)
