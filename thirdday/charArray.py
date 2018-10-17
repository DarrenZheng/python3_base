name = 'darren'

if name.startswith('da'):
    print('it is my name')

if 'd' in name:
    print('这是继承了D的意志')

if name.find('ren') != -1:
    print('yes, 是个人')

delimiter = '__*__'
mylist = ['darren', 'love', 'zhang']
print(delimiter.join(mylist))