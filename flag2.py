import base64

def secret(s):
    return ''.join('\\u{:04x}'.format(ord(c)) for c in s)

def obfuscate_input(user_input):

    un_escd = secret(user_input)

    encoded = base64.b32encode(un_escd.encode()).decode()

    return encoded

def main():
    print("====================================")
    user_input = input("Enter text to encrypt: ")

    obf = obfuscate_input(user_input)

    print("\nencrypted output:")
    print(obf)

if __name__ == "__main__":
    main()
