def map_braille():
    ABC = "the quick brown fox jumps over the lazy dog"
    BRAILLE_ABC = "011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
    
    braille_abc_map = dict()
    braille_abc = BRAILLE_ABC
    for letter in ABC:
        braille_letter = braille_abc[:6]
        braille_abc = braille_abc[6:]
        braille_abc_map[letter] = braille_letter
    return braille_abc_map

def solution(s):
    ABC = "the quick brown fox jumps over the lazy dog"
    BRAILLE_ABC = "011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
    BRAILLE_CAP = "000001"
    result = []
    abc_map = map_braille()
    for letter in s:
        if letter.isupper():
            result.append(BRAILLE_CAP)
            letter = letter.lower()
        result.append(abc_map.get(letter))
    
    return "".join(result)