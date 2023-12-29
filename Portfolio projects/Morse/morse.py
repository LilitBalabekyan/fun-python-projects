letters = {'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


is_on = True
while is_on:
    print('Hi, Welcome to MORSE TRABSLATOR! If you want to turn your phrase into a morse code!')

    def to_morse():

        word = input('Enter yourt word: ')
        word = word.lower()
        print(f"Morse code for {word.title()}")
        wordmorse = ' '
        for l in word:
            if l != ' ':
                wordmorse += letters[l] + ' '
            else:
                wordmorse += ' '
        print(wordmorse)
    to_morse()