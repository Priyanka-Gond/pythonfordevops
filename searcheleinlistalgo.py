listitem=["stg","prd","test","uat"]
key=input("enter a env ")
isfound=False
for i in listitem:
    if i==key:
        isfound=True
if isfound==True:
    print("found")
else:
    print("not found")