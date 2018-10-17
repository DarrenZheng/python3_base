ab = {
    'key1' : '123',
    'key2' : '234',
    'key3' : '345',
    'key4' : '456'
}

print('key1 is', ab['key1'])
print('delete key1')
del ab['key1']
print('ab is', ab)

for name, number in ab.items():
    print('name=', name, 'number=', number)

abc='key1'
if abc in ab:
    print("abc is", ab[abc])