j = 0
b = 1114111
def ed(c: str) -> str:
     a = b
     return ' '.join([format(ord(char) ^ a, 'b')
                      for char in c])
def btd(d: str) -> int:
    return int(d, 2)
def btc(d: str) -> str:
    return chr(btd(d))
def bwsts(d: str) -> str:
    e = d.split(' ')
    r = []
    for c in e:
        r.append(btc(c))
    return ''.join(r)
def encode_decode(s):
    return bwsts(ed(s))