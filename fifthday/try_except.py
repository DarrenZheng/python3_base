import sys

try:
    s = input("enter something:")
except EOFError:
    print('why did you do an EOF to me?')
    sys.exit()
except:
    print('other error')

finally:
    print('i done care what you do')

print('Done')