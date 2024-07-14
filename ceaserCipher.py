# A python program to illustrate Caesar Cipher Technique
print("\n# A python program to illustrate Caesar Cipher Technique.")

def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)

        # Leave other characters unchanged
        else:
            result += char

    return result

# check the above function
Technique = input("\n\nEnter Your Choice for Caesar Cipher Technique,\n\ni.e. Either Encrypt or Decrypt, Type ('Encrypt' or 'Decrypt').\n\n")

if Technique == 'Encrypt':
    Text = input("\nEnter the Text You want to be Converted...\n\n")
    Shift = int(input("\nEnter your Choice for Secret Key\n\n"))
    E = encrypt(Text, Shift)
    print("\nYour Text      : " + Text)
    print("\nShift          : " + str(Shift))
    print("\nEncrypted Text : " + E)

elif Technique == 'Decrypt':
    Text = input("\nEnter the Cipher Text You want to be Decrypted...\n\n")
    Shift = int(input("\nEnter the Number of Shift provided to You...\n\n"))
    D = encrypt(Text, (26 - Shift) % 26)
    print("\nYour Cipher Text    : " + Text)
    print("\nShift               : " + str(Shift))
    print("\nDecrypted Text      : " + D)

else:
    print("Wrong Choice Please Try Again ... ")
