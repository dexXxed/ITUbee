from itubee.main import ITUBEETEXTS
import time

start = time.time()
itubee = ITUBEETEXTS()

key2 = '00000000000000000080'
plain_text2 = 'Andrey Rocks'

enc2 = itubee.encrypt_text(plain_text2, key2)
dec2 = itubee.decrypt_text(enc2, key2)
print(enc2)
print(dec2)
print(dec2 == plain_text2)

end = time.time()
print(end - start)
