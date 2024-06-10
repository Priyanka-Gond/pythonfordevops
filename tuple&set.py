tupleitems=("first","second","third","fourth")
listitems=["first","second","third","fourth"]
#==tuple is immutable throws error__TypeError: 'tuple' object does not support item assignment
#tupleitems[1]="one"
listitems[1]="one"

#setdoesn't allow duplicates and sorts the elements
setele={'b','b','b',1,1,1,3,3,33,"priya"}
setele1={2,2,2,'b','b','b',33}
print(setele.intersection(setele1))
print(setele.union(setele1))

#set can be used to remoe the repeat elemts and print the unique elements
listele=["test","prod","stg","stg","qa","qa","prod"]
print(list(set(listele)))

