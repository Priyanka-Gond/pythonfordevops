#dictionary has key values
dict_items={"name":"priya","empid":899,"active":True}
dictitem2={"name":"mani","empid":90,"active":False}
mylst=[dict_items,dictitem2]
for i in mylst:
    for key,values in i.items():
        if key =="active" and values==True:
            print(i.values())

