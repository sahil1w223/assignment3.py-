list1 = [1 ,2 ,3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
for i in range (len(list1)//2):
    list2.append(list1[i])


list3 = []
for j in range (len(list2)):
    num = 0
    num = num + list2[len(list2)-1-j]
    list3.append(num)
print(list3)
