import string

def vignere_cipher(plain, key, encry):
    alphabet = {}
    #fills out the list with the number assign to each letter of the alphabet
    for i in range(0, len(string.ascii_uppercase)):
        alphabet[string.ascii_uppercase[i]] = i
    #based on the length of the message, decides how many keys we need
    repeated_key = key
    while(len(repeated_key) < len(plain)):
        repeated_key = repeated_key + key
    #basically turns the encrypted message or plaintext into their assign letters
    secret_message = ''
    for i in range(0, len(plain)):
        if(encry == True):
            #Ek(m) = m + K mod 26
            new_letter_index = alphabet[plain[i]] + (alphabet[repeated_key[i]] % 26)
            if new_letter_index > 25:
                new_letter_index = new_letter_index - 26
        else:
            #Ek(m) = m - K mod 26
            new_letter_index = alphabet[plain[i]] - (alphabet[repeated_key[i]] % 26)
            if new_letter_index < 0:
                new_letter_index = new_letter_index - 26
        secret_message += string.ascii_uppercase[new_letter_index]
    print(secret_message)
#if this file is ran as the main program, anything under the if will run
if __name__ == "__main__":
    #choose between encryption or decryption
    encrypt = input("Would you like encrypt plaintext? (Y or N): ").upper()
    if encrypt == 'Y':
        encrypt = True
        #will take out all the spaces and make it all uppercase
        plaintext = ''.join(input("Enter plaintext: ").split()).upper()
        key = input("Enter encryption key: ").upper()
        vignere_cipher(plaintext, key, encrypt)
    else:
        encrypt = False
        encrypted_msg = ''.join(input("Enter plaintext: ").split()).upper()
        key = input("Enter encryption key: ").upper()
        vignere_cipher(encrypted_msg, key, encrypt)
