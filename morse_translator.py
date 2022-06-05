# translate morse messages
# dot (.), dash(-), letter separator ( ), word separator (/)

morseKey = {
    'a':'.-',
    'b':'-...',
    'c':'-.-.',
    'd':'-..',
    'e':'.',
    'f':'..-.',
    'g':'--.',
    'h':'....',
    'i':'..',
    'j':'.---',
    'k':'-.-',
    'l':'.-..',
    'm':'--',
    'n':'-.',
    'o':'---',
    'p':'.--.',
    'q':'--.-',
    'r':'.-.',
    's':'...',
    't':'-',
    'u':'..-',
    'v':'...-',
    'w':'.--',
    'x':'-..-',
    'y':'-.--',
    'z':'--..',
    '0':'-----',
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    ' ':'/',
    '.':'.-.-.-',
    ',':'--..--',
    '?':'..--..',
    "'":'.----.',
    '!':'-.-.--',
    '/':'-..-.',
    '\\':'-.-.-',
    '(':'-.--.',
    ')':'-.--.-',
    '[':'.--..',
    ']':'.--..-',
    '{':'.--.-',
    '}':'.--.--',
    '&':'.-...',
    ':':'---...',
    ';':'-.-.-.',
    '=':'-...-',
    '+':'.-.-.',
    '-':'-....-',
    '_':'..--.-',
    '"':'.-..-.',
    '@':'.--.-.',
    '#':'--.-.',
    '$':'...-..',
    '%':'---.-',
    '*':'...-.',
    '<':'-.---',
    '>':'-.----',
    '^':'......',
    '`':'-..-.-',
    '~':'.---..',
    '|':'--.-.-'
}

def morseToChar(text):
    """Takes a string (or list of strings) of morse characters and returns a string of regular characters."""
    if type(text) is list:
        nList = []
        for item in text:
            nList.append(morseToChar(item))
        return nList
    else:
        nText = ''
        text = str(text).lower()
        textList = text.split()
        for item in textList:
            for key, val in morseKey.items():
                if item == val:
                    nText += key
                    break
            else:
                nText += item
        return nText

def charToMorse(text):
    """Takes a string (or list of strings) of regular characters and returns a string of morse characters."""
    # nString = None
    if type(text) is list:
        nList = []
        for item in text:
            nList.append(charToMorse(item))
        return nList
    elif type(text) is str or type(text) is int or type(text) is float:
        nText = ''
        text = str(text).lower()
        for l in text:
            nText += morseKey.get(l, l) + ' '
        nText = nText[:-1]
        return nText

def prompt():
    """Prompt the user on what they would like to do."""
    res = input('Would you like to \n(A) translate morse code into regular characters, \n(B) translate regular charaters into morse code, or \n(C) view the translation key?').lower()
    if res == 'a':
        print(morseToChar(input('What text would you like to translate?')))
    elif res == 'b':
        print(charToMorse(input('What text would you like to translate?')))
    elif res == 'c':
        print(morseKey)
    else:
        print('Invalid Response')
    if input('Would you like to continue?').lower() in ['yes', 'y']:
        prompt()

if __name__ == "__main__":
    prompt()