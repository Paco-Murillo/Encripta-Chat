# encoding = UTF-8

def encode(string,ip,n):
    dic = {'☺': 0, '☻': 1, '♥': 2, '♦': 3, '♣': 4, '♠': 5, '•': 176, '◘': 7, '○': 8, '◙': 9, '♂': 10, '♀': 11, '♪': 12,
           '♫': 13, '☼': 14, '►': 15, '◄': 16, '↕': 17, '‼': 18, '¶': 233, '§': 234, '▬': 21, '↨': 22, '↑': 23, '↓': 24,
           '→': 25, '←': 26, '∟': 27, '↔': 28, '▲': 29, '▼': 30, ' ': 31, '!': 32, '"': 33, '#': 34, '$': 35, '%': 36,
           '&': 37, "'": 38, '(': 39, ')': 40, '*': 41, '+': 42, ',': 43, '-': 44, '.': 45, '/': 46, '0': 47, '1': 48,
           '2': 49, '3': 50, '4': 51, '5': 52, '6': 53, '7': 54, '8': 55, '9': 56, ':': 57, ';': 58, '<': 59, '=': 60,
           '>': 61, '?': 62, '@': 63, 'A': 64, 'B': 65, 'C': 66, 'D': 67, 'E': 68, 'F': 69, 'G': 70, 'H': 71, 'I': 72,
           'J': 73, 'K': 74, 'L': 75, 'M': 76, 'N': 77, 'O': 78, 'P': 79, 'Q': 80, 'R': 81, 'S': 82, 'T': 83, 'U': 84,
           'V': 85, 'W': 86, 'X': 87, 'Y': 88, 'Z': 89, '[': 90, '\\': 91, ']': 92, '^': 93, '_': 94, '`': 95, 'a': 96,
           'b': 97, 'c': 98, 'd': 99, 'e': 100, 'f': 101, 'g': 102, 'h': 103, 'i': 104, 'j': 105, 'k': 106, 'l': 107,
           'm': 108, 'n': 109, 'o': 110, 'p': 111, 'q': 112, 'r': 113, 's': 114, 't': 115, 'u': 116, 'v': 117, 'w': 118,
           'x': 119, 'y': 120, 'z': 121, '{': 122, '|': 123, '}': 124, '~': 125, '⌂': 126, 'Ç': 127, 'ü': 128, 'é': 129,
           'â': 130, 'ä': 131, 'à': 132, 'å': 133, 'ç': 134, 'ê': 135, 'ë': 136, 'è': 137, 'ï': 138, 'î': 139, 'ì': 140,
           'Ä': 141, 'Å': 142, 'É': 143, 'ø': 144, '£': 145, '×': 147, 'ƒ': 148, 'á': 149, 'í': 150, 'ó': 151, 'ú': 152,
           'ñ': 153, 'Ñ': 154, 'ª': 155, 'º': 156, '¿': 157, '®': 158, '¬': 159, '½': 160, '¼': 161, '¡': 162, '«': 163,
           '»': 164, '░': 165, '▒': 166, '▓': 167, '│': 168, '┤': 169, 'Á': 170, 'Â': 171, 'À': 172, '©': 173, '╣': 174,
           '║': 175, '╝': 177, '¢': 178, '¥': 179, '┐': 180, '└': 181, '┴': 182, '┬': 183, '├': 184, '─': 185, '┼': 186,
           'ã': 187, 'Ã': 188, '╚': 189, '╔': 190, '╩': 191, '╦': 192, '╠': 193, '═': 194, '╬': 195, '¤': 196, 'ð': 197,
           'Ð': 198, 'Ê': 199, 'Ë': 200, 'È': 201, 'ı': 202, 'Í': 203, 'Î': 204, 'Ï': 205, '┘': 206, '┌': 207, '█': 208,
           '▄': 209, '¦': 210, 'Ì': 211, '▀': 212, 'Ó': 213, 'ß': 214, 'Ô': 215, 'Ò': 216, 'õ': 217, 'Õ': 218, 'µ': 219,
           'þ': 220, 'Þ': 221, 'Ú': 222, 'Û': 223, 'Ù': 224, 'ý': 225, 'Ý': 226, '¯': 227, '´': 228, '■': 229, '±': 230,
           '‗': 231, '¾': 232, '÷': 235, '¸': 236, '°': 237, '¨': 238, '·': 239, '¹': 240, '³': 241, '²': 242}
    id = int(ip[n%3])%3
    passw = ip.split(".")
    arr = ""
    if(id == 0):
        for i in range(0,len(string)):
            pas = int(passw[i%3])
            if pas == 0:
                pas = 72
            arr += getchar((dic[string[i]] + pas) % 242)
    if (id == 1):
        for i in range(0, len(string)):
            pas = int(passw[i % 3])
            if pas == 0:
                pas = 72
            arr += getchar((dic[string[i]] - pas) % 242)
    if (id == 2):
        for i in range(0, len(string)):
            pas = int(passw[i % 3])
            if pas == 0:
                pas = 72
            arr += getchar((dic[string[i]] ^ pas) % 242)
    return(arr)

def decode(string,ip,n):
    dic = {'☺': 0, '☻': 1, '♥': 2, '♦': 3, '♣': 4, '♠': 5, '•': 176, '◘': 7, '○': 8, '◙': 9, '♂': 10, '♀': 11, '♪': 12,
           '♫': 13, '☼': 14, '►': 15, '◄': 16, '↕': 17, '‼': 18, '¶': 233, '§': 234, '▬': 21, '↨': 22, '↑': 23, '↓': 24,
           '→': 25, '←': 26, '∟': 27, '↔': 28, '▲': 29, '▼': 30, ' ': 31, '!': 32, '"': 33, '#': 34, '$': 35, '%': 36,
           '&': 37, "'": 38, '(': 39, ')': 40, '*': 41, '+': 42, ',': 43, '-': 44, '.': 45, '/': 46, '0': 47, '1': 48,
           '2': 49, '3': 50, '4': 51, '5': 52, '6': 53, '7': 54, '8': 55, '9': 56, ':': 57, ';': 58, '<': 59, '=': 60,
           '>': 61, '?': 62, '@': 63, 'A': 64, 'B': 65, 'C': 66, 'D': 67, 'E': 68, 'F': 69, 'G': 70, 'H': 71, 'I': 72,
           'J': 73, 'K': 74, 'L': 75, 'M': 76, 'N': 77, 'O': 78, 'P': 79, 'Q': 80, 'R': 81, 'S': 82, 'T': 83, 'U': 84,
           'V': 85, 'W': 86, 'X': 87, 'Y': 88, 'Z': 89, '[': 90, '\\': 91, ']': 92, '^': 93, '_': 94, '`': 95, 'a': 96,
           'b': 97, 'c': 98, 'd': 99, 'e': 100, 'f': 101, 'g': 102, 'h': 103, 'i': 104, 'j': 105, 'k': 106, 'l': 107,
           'm': 108, 'n': 109, 'o': 110, 'p': 111, 'q': 112, 'r': 113, 's': 114, 't': 115, 'u': 116, 'v': 117, 'w': 118,
           'x': 119, 'y': 120, 'z': 121, '{': 122, '|': 123, '}': 124, '~': 125, '⌂': 126, 'Ç': 127, 'ü': 128, 'é': 129,
           'â': 130, 'ä': 131, 'à': 132, 'å': 133, 'ç': 134, 'ê': 135, 'ë': 136, 'è': 137, 'ï': 138, 'î': 139, 'ì': 140,
           'Ä': 141, 'Å': 142, 'É': 143, 'ø': 144, '£': 145, '×': 147, 'ƒ': 148, 'á': 149, 'í': 150, 'ó': 151, 'ú': 152,
           'ñ': 153, 'Ñ': 154, 'ª': 155, 'º': 156, '¿': 157, '®': 158, '¬': 159, '½': 160, '¼': 161, '¡': 162, '«': 163,
           '»': 164, '░': 165, '▒': 166, '▓': 167, '│': 168, '┤': 169, 'Á': 170, 'Â': 171, 'À': 172, '©': 173, '╣': 174,
           '║': 175, '╝': 177, '¢': 178, '¥': 179, '┐': 180, '└': 181, '┴': 182, '┬': 183, '├': 184, '─': 185, '┼': 186,
           'ã': 187, 'Ã': 188, '╚': 189, '╔': 190, '╩': 191, '╦': 192, '╠': 193, '═': 194, '╬': 195, '¤': 196, 'ð': 197,
           'Ð': 198, 'Ê': 199, 'Ë': 200, 'È': 201, 'ı': 202, 'Í': 203, 'Î': 204, 'Ï': 205, '┘': 206, '┌': 207, '█': 208,
           '▄': 209, '¦': 210, 'Ì': 211, '▀': 212, 'Ó': 213, 'ß': 214, 'Ô': 215, 'Ò': 216, 'õ': 217, 'Õ': 218, 'µ': 219,
           'þ': 220, 'Þ': 221, 'Ú': 222, 'Û': 223, 'Ù': 224, 'ý': 225, 'Ý': 226, '¯': 227, '´': 228, '■': 229, '±': 230,
           '‗': 231, '¾': 232, '÷': 235, '¸': 236, '°': 237, '¨': 238, '·': 239, '¹': 240, '³': 241, '²': 242}
    id = int(ip[n%3])%3
    passw = ip.split(".")
    arr = ""
    if(id == 0):
        for i in range(0,len(string)):
            pas = int(passw[i%3])
            if pas == 0:
                pas = 72
            arr += getchar((dic[string[i]] - pas) % 242)
    if (id == 1):
        for i in range(0, len(string)):
            pas = int(passw[i % 3])
            if pas == 0:
                pas = 72
            arr += getchar((dic[string[i]] + pas) % 242)
    if (id == 2):
        for i in range(0, len(string)):
            pas = int(passw[i % 3])
            if pas == 0:
                pas = 72
            arr += getchar((dic[string[i]] ^ pas) % 242)
    return(arr)


def getchar(int):
    dic = {'☺': 0, '☻': 1, '♥': 2, '♦': 3, '♣': 4, '♠': 5, '•': 176, '◘': 7, '○': 8, '◙': 9, '♂': 10, '♀': 11, '♪': 12,
           '♫': 13, '☼': 14, '►': 15, '◄': 16, '↕': 17, '‼': 18, '¶': 233, '§': 234, '▬': 21, '↨': 22, '↑': 23, '↓': 24,
           '→': 25, '←': 26, '∟': 27, '↔': 28, '▲': 29, '▼': 30, ' ': 31, '!': 32, '"': 33, '#': 34, '$': 35, '%': 36,
           '&': 37, "'": 38, '(': 39, ')': 40, '*': 41, '+': 42, ',': 43, '-': 44, '.': 45, '/': 46, '0': 47, '1': 48,
           '2': 49, '3': 50, '4': 51, '5': 52, '6': 53, '7': 54, '8': 55, '9': 56, ':': 57, ';': 58, '<': 59, '=': 60,
           '>': 61, '?': 62, '@': 63, 'A': 64, 'B': 65, 'C': 66, 'D': 67, 'E': 68, 'F': 69, 'G': 70, 'H': 71, 'I': 72,
           'J': 73, 'K': 74, 'L': 75, 'M': 76, 'N': 77, 'O': 78, 'P': 79, 'Q': 80, 'R': 81, 'S': 82, 'T': 83, 'U': 84,
           'V': 85, 'W': 86, 'X': 87, 'Y': 88, 'Z': 89, '[': 90, '²': 91, ']': 92, '^': 93, '_': 94, '`': 95, 'a': 96,
           'b': 97, 'c': 98, 'd': 99, 'e': 100, 'f': 101, 'g': 102, 'h': 103, 'i': 104, 'j': 105, 'k': 106, 'l': 107,
           'm': 108, 'n': 109, 'o': 110, 'p': 111, 'q': 112, 'r': 113, 's': 114, 't': 115, 'u': 116, 'v': 117, 'w': 118,
           'x': 119, 'y': 120, 'z': 121, '{': 122, '|': 123, '}': 124, '~': 125, '⌂': 126, 'Ç': 127, 'ü': 128, 'é': 129,
           'â': 130, 'ä': 131, 'à': 132, 'å': 133, 'ç': 134, 'ê': 135, 'ë': 136, 'è': 137, 'ï': 138, 'î': 139, 'ì': 140,
           'Ä': 141, 'Å': 142, 'É': 143, 'ø': 144, '£': 145, '×': 147, 'ƒ': 148, 'á': 149, 'í': 150, 'ó': 151, 'ú': 152,
           'ñ': 153, 'Ñ': 154, 'ª': 155, 'º': 156, '¿': 157, '®': 158, '¬': 159, '½': 160, '¼': 161, '¡': 162, '«': 163,
           '»': 164, '░': 165, '▒': 166, '▓': 167, '│': 168, '┤': 169, 'Á': 170, 'Â': 171, 'À': 172, '©': 173, '╣': 174,
           '║': 175, '╝': 177, '¢': 178, '¥': 179, '┐': 180, '└': 181, '┴': 182, '┬': 183, '├': 184, '─': 185, '┼': 186,
           'ã': 187, 'Ã': 188, '╚': 189, '╔': 190, '╩': 191, '╦': 192, '╠': 193, '═': 194, '╬': 195, '¤': 196, 'ð': 197,
           'Ð': 198, 'Ê': 199, 'Ë': 200, 'È': 201, 'ı': 202, 'Í': 203, 'Î': 204, 'Ï': 205, '┘': 206, '┌': 207, '█': 208,
           '▄': 209, '¦': 210, 'Ì': 211, '▀': 212, 'Ó': 213, 'ß': 214, 'Ô': 215, 'Ò': 216, 'õ': 217, 'Õ': 218, 'µ': 219,
           'þ': 220, 'Þ': 221, 'Ú': 222, 'Û': 223, 'Ù': 224, 'ý': 225, 'Ý': 226, '¯': 227, '´': 228, '■': 229, '±': 230,
           '‗': 231, '¾': 232, '÷': 235, '¸': 236, '°': 237, '¨': 238, '·': 239, '¹': 240, '³': 241}
    for key, value in dic.items():
        if(value == int):
            return key
    return "NULL"

# print(encode("Hola como estas","192.56.72",45678))
# print(decode(encode("Hola como estas","192.56.72",45678),"192.56.72",45678))