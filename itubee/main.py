from .const import *


class ITUBEE:
    def l(self, a):
        x = [(a[4] ^ a[0]) ^ a[1],
             (a[0] ^ a[1]) ^ a[2],
             (a[1] ^ a[2]) ^ a[3],
             (a[2] ^ a[3]) ^ a[4],
             (a[3] ^ a[4]) ^ a[0]]
        return x

    def f(self, a):
        temp_x = self.l(list(map(lambda x: SBOX[x & 255], a)))

        return list(map(lambda x: SBOX[x & 255], temp_x))

    def encrypt(self, message, key):
        h_message = generate_hexadecimal_array(message)
        h_key = generate_hexadecimal_array(key)

        half = len(h_message) // 2
        pl, pr, kl, kr = h_message[:half], h_message[-half:], h_key[:half], h_key[-half:]

        x = [xor(pr, kr),
             xor(pl, kl)]

        for i in range(1, 21):
            rk = []

            if i % 2 == 0:
                rk = kl
            else:
                rk = kr

            rc = generate_rc(i - 1)
            x += [xor(x[i - 1], self.f(self.l(xor(xor(rk, rc), self.f(x[i])))))]

        cl = xor(x[20], kr)
        cr = xor(x[21], kl)

        return "".join(map(lambda el: '{0:02X}'.format(el), cl + cr))

    def decrypt(self, enc_message, key):
        h_message = generate_hexadecimal_array(enc_message)
        h_key = generate_hexadecimal_array(key)

        half = len(h_message) // 2
        pl, pr, kl, kr = h_message[:half], h_message[-half:], h_key[:half], h_key[-half:]
        x = [xor(pr, kl),
             xor(pl, kr)]

        for i in range(1, 21):
            rk = []

            if i % 2 == 0:
                rk = kr
            else:
                rk = kl

            rc = generate_rc(-i)
            x += [xor(x[i - 1], self.f(self.l(xor(xor(rk, rc), self.f(x[i])))))]

        cl = xor(x[20], kl)
        cr = xor(x[21], kr)

        return "".join(map(lambda el: '{0:02X}'.format(el), cl + cr))


# для обработки текстов
class ITUBEETEXTS(ITUBEE):

    def encrypt_text(self, text, key):
        plain_text2_hex = "".join("{:02x}".format(ord(c)) for c in text)

        encrypted_texts = []
        for x in range(0, len(plain_text2_hex), 20):
            final_index = len(plain_text2_hex) if x + 20 > len(plain_text2_hex) else x + 20
            current_text = "{0:0<20}".format(plain_text2_hex[x:final_index])
            encrypted_texts += [self.encrypt(current_text, key)]

        return encrypted_texts

    def decrypt_text(self, encrypted_texts, key):
        decrypted_plain_text = ''
        for enc2 in encrypted_texts:
            decrypted_plain_text += self.decrypt(enc2, key)

        return bytearray.fromhex(decrypted_plain_text).decode().rstrip(' \t\r\n\0')
