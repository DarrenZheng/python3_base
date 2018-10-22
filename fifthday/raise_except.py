class ShortException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length=length
        self.atleast=atleast

    def __str__(self):
        return "是什么"

try:
    s = input("enter something:")
    if len(s) < 3:
        raise ShortException(len(s), 3)

except EOFError:
    print('why did you do an EOF to me?')

except ShortException as x :
    print('ShortException', 'the input was', x.length)
    print(x)