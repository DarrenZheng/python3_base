import sys

def readfile(fileName):
    f = open(fileName,'r')
    while True:
        line = f.readline()
        if len(line) ==0:
            break
        print(line, end='')
    f.close()


if len(sys.argv) < 2:
    print('no file')
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if option == 'version':
        print('v1.2')
    elif option == 'help':
        print('no help message')
else:
    for filename in sys.argv[1:]:
        readfile(filename)