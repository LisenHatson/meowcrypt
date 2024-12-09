def meowovert(char):
    meowpping = {
        'a': 'MAUWW ',
        'b': 'MeOw ',
        'c': 'hSSSh ',
        'd': 'mauw ',
        'e': 'meow ',
        'f': 'MEOw ',
        'g': 'mrruhh ',
        'h': 'nyua ',
        'i': 'mouw ',
        'j': 'MeOW ',
        'k': 'mrruww ',
        'l': 'miii ',
        'm': 'meee ',
        'n': 'meOw ',
        'o': 'nyawww ',
        'p': 'ngauu ',
        'q': 'mawww ',
        'r': 'meoW ',
        's': 'mrrr ',
        't': 'hisss ',
        'u': 'nyaauu ',
        'v': 'mEOW ',
        'w': 'MEow ',
        'x': 'ssshaa ',
        'y': 'mawmaw ',
        'z': 'Meow ',

        '0': 'purr ',
        '1': 'ngauung ',
        '2': 'HSSSS ',
        '3': 'rrrrr ',
        '4': 'RRrRR ',
        '5': 'nyAAA ',
        '6': 'meW ',
        '7': 'MEW ',
        '8': 'hssSSS ',
        '9': 'rrrrurrr ',

        '.': 'nyaOO ',
        '!': 'rraurr ',
        '?': 'nyaa ',
        ' ': ' '
    }

    if char.lower() in meowpping:
        return meowpping[char.lower()]

    return ''

def convMeow(input):
    return ''.join(meowovert(char) for char in input)

def convOrig(meow_input):
    meowpping = {
        'MAUWW': 'a',
        'MeOw': 'b',
        'hSSSh': 'c',
        'mauw': 'd',
        'meow': 'e',
        'MEOw': 'f',
        'mrruhh': 'g',
        'nyua': 'h',
        'mouw': 'i',
        'MeOW': 'j',
        'mrruww': 'k',
        'miii': 'l',
        'meee': 'm',
        'meOw': 'n',
        'nyawww': 'o',
        'ngauu': 'p',
        'mawww': 'q',
        'meoW': 'r',
        'mrrr': 's',
        'hisss': 't',
        'nyaauu': 'u',
        'mEOW': 'v',
        'MEow': 'w',
        'ssshaa': 'x',
        'mawmaw': 'y',
        'Meow': 'z',

        'purr': '0',
        'ngauung': '1',
        'HSSSS': '2',
        'rrrrr': '3',
        'RRrRR': '4',
        'nyAAA': '5',
        'meW': '6',
        'MEW': '7',
        'hssSSS': '8',
        'rrrrurrr': '9',

        'nyaOO': '.',
        'rraurr': '!',
        'nyaa': '?',
        ' ': ' '
    }

   # Split the meow input by spaces and convert back to original characters
    original_chars = []
    meow_chars = meow_input.split(' ')  # Split on single spaces to preserve spaces

    for meow_char in meow_chars:
        if meow_char in meowpping:
            original_chars.append(meowpping[meow_char])
        else:
            original_chars.append(' ')  # If not found, append a placeholder

    return ''.join(original_chars)


input_string = "abcdefghijklmnopqrstuvwxyz1234567890"
encrypted_string = convMeow(input_string)
decrypted_string = convOrig(encrypted_string.strip())

print(f"Input: {input_string}")
print(f"Encrypted: {encrypted_string}")
print(f"Decrypted: {decrypted_string}")
