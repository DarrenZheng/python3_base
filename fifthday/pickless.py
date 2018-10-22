import pickle as p

shoplistFile = '/tmp/list'

shoplist = ['apple','mango','banana']
str = '字符串'
num = 123

f = open(shoplistFile,'wb')

p.dump(shoplist,f)
p.dump(str, f)
p.dump(num, f)

f.close()

f = open(shoplistFile, "rb")

data = p.load(f)
print(data)

data = p.load(f)
print(data)

data = p.load(f)
print(data)
