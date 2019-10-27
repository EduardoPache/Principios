KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'Q',
    'C': '4',
    'D': ',',
    'E': '!',
    'F': '?',
    'G': '&',
    'H': '|',
    'I': '#',
    'J': 'x',
    'K': 'P',
    'L': '6',
    'M': 'z',
    'O': 's',
    'P': 'l',
    'Q': 'h',
    'R': '0',
    'S': '2',
    'T': '7',
    'U': 'F',
    'V': '+',
    'W': 'M',
    'X': 'O',
    'Y': '?',
    'Z': 'E',
}
def cypher(message):
    words = message.split(' ')
    cypher_message = []

    for word in words:
        cypher_word = ''
        for letter in word:
            cypher_word += KEYS[letter]
            

        cypher_message.append(cypher_word)
    return ' '.join(cypher_message)


def decipher(message):
    words = message.split(' ')
    decipher_message = []

    for word in words:
        decipher_word = ''
        
        for letter in word:
            for key, value in KEYS.items():
                if value == letter:
                    decipher_word += key

        decipher_message.append(decipher_word)
    return ' '.join(decipher_message)
def run():
    
    while True:

        command = str(input('''--- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografia. ¿Que deseas hacer?

            [C]ifrar mensaje
            [D]ecrifar mensaje
            [S]alir
        '''))

        if command == 'c':
            message = str(input('Cual seria tu mensaje: '))
            cypher_message = cypher(message)
            print(cypher_message)

        elif command == 'd':
            message = str(input('Cual seria tu mensaje: '))
            decipher_message = decipher(message)
            print(decipher_message)
        elif command == 's':
            print('Salir')
        else:
            print('¡Comando no encontrado!')

    print('MENSAJES CIFRADOS')
run()
