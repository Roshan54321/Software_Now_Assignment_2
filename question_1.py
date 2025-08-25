# --- Encryption/Decryption that NEVER crosses halves (mod 13) ---

def encrypt_letter(letter, shift1, shift2):
    # lowercase
    if 'a' <= letter <= 'z':
        if letter <= 'm':  # a-m : forward by shift1*shift2 within a-m
            return chr(ord('a') + ((ord(letter) - ord('a') + (shift1 * shift2)) % 13))
        else:              # n-z : backward by shift1+shift2 within n-z
            return chr(ord('n') + ((ord(letter) - ord('n') - (shift1 + shift2)) % 13))
    # uppercase
    elif 'A' <= letter <= 'Z':
        if letter <= 'M':  # A-M : backward by shift1 within A-M
            return chr(ord('A') + ((ord(letter) - ord('A') - shift1) % 13))
        else:              # N-Z : forward by shift2^2 within N-Z
            return chr(ord('N') + ((ord(letter) - ord('N') + (shift2 ** 2)) % 13))
    else:
        return letter  # spaces, tabs, newlines, digits, symbols unchanged


def decrypt_letter(letter, shift1, shift2):
    # exact inverse of above (same halves, opposite directions)
    if 'a' <= letter <= 'z':
        if letter <= 'm':  # a-m : backward by shift1*shift2 within a-m
            return chr(ord('a') + ((ord(letter) - ord('a') - (shift1 * shift2)) % 13))
        else:              # n-z : forward by shift1+shift2 within n-z
            return chr(ord('n') + ((ord(letter) - ord('n') + (shift1 + shift2)) % 13))
    elif 'A' <= letter <= 'Z':
        if letter <= 'M':  # A-M : forward by shift1 within A-M
            return chr(ord('A') + ((ord(letter) - ord('A') + shift1) % 13))
        else:              # N-Z : backward by shift2^2 within N-Z
            return chr(ord('N') + ((ord(letter) - ord('N') - (shift2 ** 2)) % 13))
    else:
        return letter


def encryption(shift1, shift2):
    with open("resources/raw_text.txt", "r", encoding="utf-8") as file:
        text = file.read()
    encrypted_text = ''.join(encrypt_letter(c, shift1, shift2) for c in text)
    with open("resources/encrypted_text.txt", "w", encoding="utf-8") as file:
        file.write(encrypted_text)


def decryption(shift1, shift2):
    with open("resources/encrypted_text.txt", "r", encoding="utf-8") as file:
        text = file.read()
    decrypted_text = ''.join(decrypt_letter(c, shift1, shift2) for c in text)
    with open("resources/decrypted_text.txt", "w", encoding="utf-8") as file:
        file.write(decrypted_text)


def verification(debug=False):
    with open("resources/raw_text.txt", "r", encoding="utf-8") as file:
        raw_text = file.read()
    with open("resources/decrypted_text.txt", "r", encoding="utf-8") as file:
        decrypted_text = file.read()

    if raw_text == decrypted_text:
        print("Encryption and decryption are consistent.")
    else:
        print("Mismatch found between original and decrypted texts.")
        if debug:
            # help you see where it breaks
            for i, (a, b) in enumerate(zip(raw_text, decrypted_text)):
                if a != b:
                    print(f"First mismatch at pos {i}: '{a}' -> '{b}'")
                    break


def main():
    try:
        shift1, shift2 = map(int, input("Provide two shift values separated by space: ").split())
        encryption(shift1, shift2)
        decryption(shift1, shift2)
        verification(debug=True)
    except ValueError:
        print("Invalid input. Enter two integers separated by a space.")
    except FileNotFoundError:
        print("File not found. Make sure raw_text.txt exists in resources folder.")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
