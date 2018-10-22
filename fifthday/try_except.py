import sys

try:
    s = input("enter something:")
except EOFError:
    print('why did you do an EOF to me?')
    sys.exit()
except:
    print('other error')

print('Done')