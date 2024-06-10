items=[90,5,89,-2,8,4,1,0]
length=len(items)
for i in range(length):
    for j in range(length):
        if items[i] < items[j]:
            temp=items[i]
            items[i]=items[j]
            items[j]=temp
print(items)