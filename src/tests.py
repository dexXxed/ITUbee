from itubee.main import ITUBEE
from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f'func:{f.__name__} args:[{args}, {kw}] Выполнялась: {te - ts} sec')
        return result
    return wrap


@timing
def itubee_logic(itubee, plain_text, key):
    enc = itubee.encrypt(plain_text, key)
    print(enc)

    dec = itubee.decrypt(enc, key)
    print(dec)


if __name__ == '__main__':
    itubee = ITUBEE()

    itubee_logic(itubee, '01000000000000000000', '00000000000000000080')

    itubee_logic(itubee, '00000000000000000000', '00000000000000000000')

    itubee_logic(itubee, '6925278951fbf3b25ccc', 'c538bd9289822be43363')
