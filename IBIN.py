j = 0

inputstring = input("Enter a string to encode/decode with IBIN (Inverted-BINary): ")

MAX = 1114111
 
def encrypt(string: str) -> str:
     max_char_code = MAX
     return ' '.join([format(ord(char) ^ max_char_code, 'b')
                      for char in string])
 
def decrypt(string: str) -> str:
     max_char_code = MAX
     return ''.join([chr(int(char, 2) ^ max_char_code)
                     for char in string.split(' ')])
 
bstr = encrypt(inputstring)

i = len(bstr)

def binary_to_dec(bin: str) -> int:
    return int(bin, 2)

def convert_binary_to_char(bin: str) -> str:
    return chr(binary_to_dec(bin))

def convert_binary_with_space_to_string(bin: str) -> str:
    convert = bin.split(' ')
    result = []

    for c in convert:
        result.append(convert_binary_to_char(c))
    return ''.join(result)

festr = convert_binary_with_space_to_string(bstr)

print("Your encoded/decoded string = " + festr + " (don't worry if the characters are not recognized).")