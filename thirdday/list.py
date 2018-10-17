shoplist = ['apple', 'mango', 'carrno']
print("i have", len(shoplist), 'items to purchase.')
print("these item are"),
for item in shoplist:
    print(item, end=' ')

print('\nIalso havve buy rice')
shoplist.append('rice')

print("now list is",shoplist)
