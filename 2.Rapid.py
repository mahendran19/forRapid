li=[1, 2, 3, 5, 8,1,0,2,3, 4,15,12,7,0,0,7,8, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1]
s=set(li)


for i in s:
    li.count(i)
    print(str(i)+"-- counting of Results:",li.count(i))

