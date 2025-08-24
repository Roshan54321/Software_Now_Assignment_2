#Encrypt and decrypt a single letter
def encrypt_letter(letter, shift1, shift2):
    if 'a' <= letter <= 'z':
        if 'a' <= letter <= 'm':
            new_ord = ord(letter) + (shift1 * shift2)
            if new_ord > ord('z'):
                new_ord = ord('a') + (new_ord - ord('z') - 1)
            return chr(new_ord)
        else:
            new_ord = ord(letter) - (shift1 + shift2)
            if new_ord < ord('a'):
                new_ord = ord('z') - (ord('a') - new_ord - 1)
            return chr(new_ord)
    elif 'A' <= letter <= 'Z':
        if 'A' <= letter <= 'M':
            new_ord = ord(letter) - shift1
            if new_ord < ord('A'):
                new_ord = ord('Z') - (ord('A') - new_ord - 1)
            return chr(new_ord)
        else:
            new_ord = ord(letter) + (shift2 ** 2)
            if new_ord > ord('Z'):
                new_ord = ord('A') + (new_ord - ord('Z') - 1)
            return chr(new_ord)
    else:
        return letter


def decryption_letter(letter, shift1, shift2):
    if 'a' <= letter <= 'z':
        if 'a' <= letter <= 'm':
            new_ord = ord(letter) - (shift1 * shift2)
            if new_ord < ord('a'):
                new_ord = ord('z') - (ord('a') - new_ord - 1)
            return chr(new_ord)
        else:
            new_ord = ord(letter) + (shift1 + shift2)
            if new_ord > ord('z'):
                new_ord = ord('a') + (new_ord - ord('z') - 1)
            return chr(new_ord)
    elif 'A' <= letter <= 'Z':
        if 'A' <= letter <= 'M':
            new_ord = ord(letter) + shift1
            if new_ord > ord('Z'):
                new_ord = ord('A') + (new_ord - ord('Z') - 1)
            return chr(new_ord)
        else:
            new_ord = ord(letter) - (shift2 ** 2)
            if new_ord < ord('A'):
                new_ord = ord('Z') - (ord('A') - new_ord - 1)
            return chr(new_ord)
    else:
        return letter
