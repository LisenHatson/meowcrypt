def meowovert(char):
    meowpping = {
        'a': 'mEoW ',
        'b': 'MeOw ',
        'c': 'MEow ',
        'd': 'meOW ',
        'e': 'mEoW ',
        'f': 'MeOw ',
        'g': 'MEow ',
        'h': 'meOW ',
        'i': 'mEoW ',
        'j': 'MeOw ',
        'k': 'MEow ',
        'l': 'meOW ',
        'm': 'mEoW ',
        'n': 'MeOw ',
        'o': 'MEow ',
        'p': 'meOW ',
        'q': 'mEoW ',
        'r': 'MeOw ',
        's': 'MEow ',
        't': 'meOW ',
        'u': 'mEoW ',
        'v': 'MeOw ',
        'w': 'MEow ',
        'x': 'meOW ',
        'y': 'mEoW ',
        'z': 'MeOw ',

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
        'mEoW': 'a',
        'MeOw': 'b',
        'MEow': 'c',
        'meOW': 'd',
        'mEoW': 'e',
        'MeOw': 'f',
        'MEow': 'g',
        'meOW': 'h',
        'mEoW': 'i',
        'MeOw': 'j',
        'MEow': 'k',
        'meOW': 'l',
        'mEoW': 'm',
        'MeOw': 'n',
        'MEow': 'o',
        'meOW': 'p',
        'mEoW': 'q',
        'MeOw': 'r',
        'MEow': 's',
        'meOW': 't',
        'mEoW': 'u',
        'MeOw': 'v',
        'MEow': 'w',
        'meOW': 'x',
        'mEoW': 'y',
        'MeOw': 'z',

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


# input_string = "1 1213 !! 1??...?"
# encrypted_string = convMeow(input_string)
# decrypted_string = convOrig(encrypted_string.strip())

# print(f"Input: {input_string}")
# print(f"Encrypted: {encrypted_string}")
# print(f"Decrypted: {decrypted_string}")
