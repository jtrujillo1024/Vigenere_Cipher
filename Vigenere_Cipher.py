
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def translate_message(key, message, mode):
    new_message = []
    keyIndex = 0
    key = key.upper()

    for symbol in message: #iterate over each character
        num = LETTERS.find(symbol.upper())
        if num != -1: #num = -1 means symbol is not in LETTERS
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])
            
            num %= len(LETTERS) #Handle wrap arounds

            if symbol.isupper():
                new_message.append(LETTERS[num])
            elif symbol.islower():
                new_message.append(LETTERS[num].lower())
            
            keyIndex += 1 #iterates over key characters
            if keyIndex == len(key):
                keyIndex = 0
            
        else:
            new_message.append(symbol) #append special characters
        
    return ''.join(new_message)
    

def encrypt(key, message):
    return translate_message(key, message, 'encrypt')

def decrypt(key, message):
    return translate_message(key, message, 'decrypt')

def check_key(key):
    for symbol in key:
        num = LETTERS.find(symbol.upper())
        if num == -1:
            return False
    return True

def main():
    while True:
        print('------------------------------\n')
        print('Vigenere Cipher Translator\n')
        print('------------------------------\n\n')

        
        print('Encrypt or decrypt?')
        mode = input().lower()
        
        if mode.startswith('e'): #handles spelling errors
            mode = 'Encrypt'
        elif mode.startswith('d'):
            mode = 'Decrypt'
        
        else:
            print('\n[!] Invalid input [!]\n')
            continue


        print('\nEnter the key:')
        key = input()
        
        if check_key(key) == False: #check key validity
            print('[!] No special characters in the key [!]')
            continue
        

        print('\nEnter the text to be {}ed:'.format(mode.lower()))
        message = input()


        if mode == 'Encrypt': #encrypt
            new_message = encrypt(key, message)

        elif mode == 'Decrypt': #decrypt
            new_message = decrypt(key, message)
        
        print('\nSuccess!\n{0}ed message:\n{1}\n'.format(mode, new_message))

        print('continue? y/n\n') #determines loop termination
        sentinel = input().lower()
        if sentinel.startswith('n'):
            break

if __name__ == '__main__':
    main()