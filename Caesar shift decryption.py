SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('CAESAR SHIFT DECRYTION')

print('ENTER THE CODE YOU WANT TO DECRYPT, (USE CAPITAL LETERS)')

code = input('>')

for key in range(1,26):
    translated = ''

    for letter in code:
        if letter in SYMBOLS:
            num=SYMBOLS.find(letter)
            num = num-key
        if num<0:
            num = num+26

        translated = translated + SYMBOLS[num]

    print(key, translated)