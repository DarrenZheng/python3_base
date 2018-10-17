shoplist = ['apple', 'mango', 'carrno']
print("i have", len(shoplist), 'items to purchase.')
print("these item are"),
for item in shoplist:
    print(item, end=' ')

print('\nIalso havve buy rice')
shoplist.append('rice')

print("now list is",shoplist)

shoplist.sort()
print('after sort, list is',shoplist)

print('the first item i want to buy is', shoplist[0])
#del shoplist[0]

shoplist.__delitem__(-1)

print('my shopping list now is: ', shoplist)