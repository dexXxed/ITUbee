from itubee.main import ITUBEETEXTS
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
def itubee_logic_text(itubee, plain_text, key):
    enc = itubee.encrypt_text(plain_text, key)
    dec = itubee.decrypt_text(enc, key)
    print("".join(enc))
    print(dec)
    print(dec == plain_text)


if __name__ == '__main__':
    itubee_text = ITUBEETEXTS()

    itubee_logic_text(itubee_text, 'dexxxed', '00000000000000000080')
