import string
import time

#takes in text and key. goes through each character turns them into unicode
#once it has the final unicode index for the decrypted character, it turns the
#found unicode and turn it back into a character. (97 is the unicode index for
# when lower case letters start)
def possible_decryption(text, key):
    possible_decrypted = ''
    for i in range(0, len(text)):
        m = ord(text[i]) - 97
        k = ord(key[i % len(key)]) - 97
        possible_decrypted = possible_decrypted + chr(((m - k) % 26) + 97)
    return possible_decrypted.upper()

def password_cracker(cipher, key_length, first_word_length):
    #starts the timer
    start_time = time.time()
    poss_keys = dict.fromkeys(string.ascii_uppercase, 1)
    poss_first_words = {}
    first_time = True
    #this gets the cipher's first word based on the given length
    cipher_first_word = cipher[:int(first_word_length)]
    dict_file = open('dict.txt', 'r')
    #this gets all the words from dict.txt that are the given length
    for i in dict_file:
        if len(i.rstrip()) == first_word_length:
            poss_first_words[i.rstrip()] = 1
    #finding all possible key of the given lengths
    for i in range(key_length):
        possible_keys = {}
        temp = {}
        #puts the amount of letters from the possible first words into a hash table
        for current_word in poss_first_words:
            possible_keys[current_word[:i+1]] = 1
        if first_time == True:
            #at this point we basically have the whole alphabet as possible keys
            #in the has table
            for j in poss_keys.keys():
                #this will try to see if any of the length 1 keys will decrypt the
                #the message by comparing the result of the first word decryption
                #to the possible first words from the dict.txt. any word that start
                #with the key letter is added to a hash table
                if possible_decryption(cipher_first_word[i], j) in possible_keys:
                    temp[j] = 1
            first_time = False
        else:
            #this will try all the possible keys of different legths. once all the
            #posabilities are found for the keys. it will try them to see if any
            #combination would make a match to the list of possible first words
            #and add them to a hash table
            for j in poss_keys.keys():
                for z in string.ascii_uppercase:
                    if possible_decryption(cipher_first_word[:i+1], j + z) in possible_keys:
                        temp[j + z] = 1
        #updates the hash table for the next step
        poss_keys = temp
    for i in poss_keys.keys():
        #once here, this means that all the possible keys were found for the assign length
        plaintext = possible_decryption(cipher_first_word, i)
        #this will try all the keys found until the outcome matches one of the
        #possibe first words from dict.txt
        if plaintext in poss_first_words:
            #getting in here means the first word has been found and will decrypt
            #the whole message and it will stop the timer, and print everything out
            end_time = time.time()
            print("Key: " + i)
            print("Decrypted Text: " + possible_decryption(cipher, i))
            print("Time: " + str(end_time - start_time) + " sec")
def main():
    print("Key length: 2")
    password_cracker("MSOKKJCOSXOEEKDTOSLGFWCMCHSUSGX", 2, 6)
    print("")
    print("Key length: 3")
    password_cracker("OOPCULNWFRCFQAQJGPNARMEYUODYOUNRGWORQEPVARCEPBBSCEQYEARAJUYGWWYACYWBPRNEJBMDTEAEYCCFJNENSGWAQRTSJTGXNRQRM", 3, 7)
    print("")
    print("Key length: 4")
    password_cracker("MTZHZEOQKASVBDOWMWMKMNYIIHVWPEXJA", 4, 10)
    print("")
    print("Key length: 5")
    password_cracker("HUETNMIXVTMQWZTQMMZUNZXNSSBLNSJVSJQDLKR", 5, 11)
    print("")
    print("Key length: 6")
    password_cracker("LDWMEKPOPSWNOAVBIDHIPCEWAETYRVOAUPSINOVDIEDHCDSELHCCPVHRPOHZUSERSFS", 6, 9)
    print("")
    print("Key length: 7")
    password_cracker("VVVLZWWPBWHZDKBTXLDCGOTGTGRWAQWZSDHEMXLBELUMO", 7, 13)
    print("")
#checks if the source file is being run as the main program
if __name__ == '__main__':
    main()
