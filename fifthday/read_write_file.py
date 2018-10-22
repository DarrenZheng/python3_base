

poem = '''\
当你说这句话的时候
请仔细想象
是否是
偏离了你的意图
'''

f = open('/tmp/poem.txt','w')

f.write(poem)

f.close()

f = open('/tmp/poem.txt')
while True:
    line = f.readline();
    if len(line) == 0:
        break
    print(line)
f.close()