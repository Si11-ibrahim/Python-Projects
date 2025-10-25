alph = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
    , 'w', 'x', 'y', 'z']


def encryption(val, shift):
    enc_str = ""
    for i in val:
        pos = alph.index(i)
        new_pos = (pos + shift) % 26
        enc_str += alph[new_pos]
    print(f"Encrypted String is: {enc_str}")


def decryption(val, shift):
    dec_str = ""
    for i in val:
        pos = alph.index(i)
        new_pos = (pos - shift) % 26
        dec_str += alph[new_pos]
    print(f"Decrypted String: {dec_str}")


while True:
    opt = input("e for Encryption or d Decryption: or 0 to exit\n Enter here: ").lower()
    if opt == "e":
        string = input("Enter a string: ").lower()
        shift = int(input("Enter a shift value: "))
        encryption(string, shift)
    elif opt == "d":
        string = input("Enter a string: ").lower()
        shift = int(input("Enter a shift value: "))
        decryption(string, shift)
    elif (opt == "exit") or (opt == "0"):
        break
