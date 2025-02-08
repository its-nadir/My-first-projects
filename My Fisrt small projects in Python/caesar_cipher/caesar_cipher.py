from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            index = alphabet.index(char)
            encrypted_text += alphabet[index + shift]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            index = alphabet.index(char)
            decrypted_text += alphabet[index - shift]
        else:
            decrypted_text += char
    return decrypted_text
choose=""
while  choose!="no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode':
        encrypted_text = encrypt(text, shift)
        print("Here is the encoded result:", encrypted_text)
    elif direction == 'decode':
        decrypted_text = decrypt(text, shift)
        print("Here is the decoded result:", decrypted_text)
    choose=input("Type 'yes' if you want to go again. otherwise, type 'no': ").lower()
print("Goodbye!")
