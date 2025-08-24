def encryption(shift1, shift2):
    with open("resources/raw_text.txt", "r") as file:
        text = file.read()

        encrypted_text = ''
        for letter in text:
            # for lowercase letters
            if 'a' <= letter <= 'z':
                if letter <= 'm':
                    # to make sure the shift is between a-m in a round fashion
                    encrypted_text += chr(ord('a') + (ord(letter) - ord('a') + (shift1 * shift2)) % 13)
                else:
                    encrypted_text += chr(ord('n') + (ord(letter) - ord('n') - (shift1 + shift2)) % 13)
            # for uppercase letters
            elif 'A' <= letter <= 'Z':
                if letter <= 'M':
                    encrypted_text += chr(ord('A') + (ord(letter) - ord('A') - shift1) % 13)
                else:
                    encrypted_text += chr(ord('N') + (ord(letter) - ord('N') + (shift2 ** 2)) % 13)
            else:
                encrypted_text += letter

    with open("resources/encrypted_text.txt", "w") as file:
        file.write(encrypted_text)

def decryption(shift1, shift2):
    with open("resources/encrypted_text.txt", "r") as file:
        encrypted_text = file.read()

        decrypted_text = ''
        for letter in encrypted_text:
            # lowercase letters
            if 'a' <= letter <= 'z':
                if letter <= 'm':  
                    decrypted_text += chr(ord('a') + (ord(letter) - ord('a') - (shift1 * shift2)) % 13)
                else: 
                    decrypted_text += chr(ord('n') + (ord(letter) - ord('n') + (shift1 + shift2)) % 13)
            # uppercase letters
            elif 'A' <= letter <= 'Z':
                if letter <= 'M': 
                    decrypted_text += chr(ord('A') + (ord(letter) - ord('A') + shift1) % 13)
                else:
                    decrypted_text += chr(ord('N') + (ord(letter) - ord('N') - (shift2 ** 2)) % 13)
            else:
                decrypted_text += letter

    with open("resources/decrypted_text.txt", "w") as file:
        file.write(decrypted_text)

def verification():
    with open("resources/raw_text.txt", "r") as file:
        raw_text = file.read()    
    with open("resources/decrypted_text.txt", "r") as file:
        decrypted_text = file.read()
    if raw_text == decrypted_text:
        print("Encryption and decryption are consistent.")
    else:
        print("Mismatch found between original and decrypted texts.")

def main():
    try:
        print("Provide two shift values separated by a space:")
        shift1, shift2 = map(int, input().split())

        encryption(shift1, shift2)
        decryption(shift1, shift2)
        verification()
        
    except ValueError:
        print("Invalid input. Please enter two integers separated by a space.")

    except Exception as e:
        print("Please try again.")

if __name__ == "__main__":
    main()