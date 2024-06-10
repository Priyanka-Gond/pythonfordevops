inputlist=list(input("enter a list"))
print(inputlist)
l=len(inputlist)
for i in range(l):
    for j in range(l):
        if inputlist[i] < inputlist[j]:
            temp=inputlist[i]
            inputlist[i]=inputlist[j]
            inputlist[j]=temp
print(inputlist)

print(inputlist[0])
print(inputlist[1])