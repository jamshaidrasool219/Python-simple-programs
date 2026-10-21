# Program: Caesar cipher (encrypt / decrypt)
def shift_text(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - base + key) % 26 + base)
        else:
            result += ch
    return result


text = input("Text likhein: ")
key = int(input("Key (number) likhein: "))

encrypted = shift_text(text, key)
print("Encrypted:", encrypted)
print("Decrypted:", shift_text(encrypted, -key))
