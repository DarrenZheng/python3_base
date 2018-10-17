shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist

del mylist[0]
print('shoplist is', shoplist)

mylist = shoplist[:]
del mylist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
