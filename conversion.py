def main():
    print('** Converter App **\n')
    print('Reading file...\n')
    print('')

    file = open('numeros.txt', 'r')

    for line in file:
        base, number = line.split(';')
        number = number.replace('\n', '')
        if base == '10':
            if not '.' in number:
                n = decimal_e_binary(number)
                print(binary_to_IEEE754(n))
            elif '.' in number:
                whole, dec = number.split('.')
                whole = decimal_e_binary(whole)
                dec = decimal_f_binary(number)
                n = f'{whole}.{dec}'
                print(binary_to_IEEE754(n))
        elif base == '2':
            print(binary_to_IEEE754(number))
        elif base == '16':
            n = hexadecimal_binary(number)
            print(binary_to_IEEE754(n))
        elif base == '8':
            n = octal_binary(number)
            print(binary_to_IEEE754(n))

    print('\nClosing file...')
    file.close()


# Decimal numbers

def decimal_e_binary(decimal_number):  # To entire part 
    rest_list = []
    # remove sign - if exist
    sign = '-' if '-' in decimal_number else ''
    decimal_number = int(decimal_number.replace('-', ''))

    while decimal_number >= 2:
        rest_list.append(decimal_number % 2)
        decimal_number = int(decimal_number / 2)
    rest_list.append(decimal_number % 2)
    return f'{sign}{"".join(str(d) for d in rest_list[::-1])}'

def decimal_f_binary(decimal_number):  # To fractionary part
    result_list = []

    for i in range(0, 4): # only take 4 places
        decimal_number = float(f'0.{str(decimal_number).split(".")[1]}') * 2
        result_list.append(str(decimal_number)[:1])
    return ''.join(str(d) for d in result_list)

# Octal numbers

def octal_binary(octal_number):
    octal_number = octal_number
    octal_binary_table = {
        '0': '000',
        '1': '001',
        '2': '010',
        '3': '011',
        '4': '100',
        '5': '101',
        '6': '110',
        '7': '111',
        '.': '.',
        '-': '-',
    }
    return ''.join(octal_binary_table[n] for n in octal_number)

# Hexadecimal numbers

def hexadecimal_binary(hexadecimal_number):
    hexadecimal_number = hexadecimal_number.upper()
    hexadecimal_binary_table = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
        '.': '.',
        '-': '-',
    }
    return ''.join(hexadecimal_binary_table[n] for n in hexadecimal_number)


# To IEEE 754

def binary_to_IEEE754(number:str):  # Convert binary to IEEE754 number format of 32 bits
    # Format of IEEE754
    # |1 bit| 8 bits   | 23 bits  |
    # |sign | exponent | mantissa |

    sign = '1' if '-' in number else '0'  # Sign
    number = number.replace('-', '')
    before_comma, after_comma = number.split('.')  # separate the number
    to_exponent = len(before_comma) - 1  # get exponent
    standard = 127 + to_exponent  # calculate the E decimal
    exponent_binary = decimal_e_binary(str(standard))  # E to binary
    mantissa_incomplete = f'{before_comma[1:]}{after_comma}'  # mantissa incomplete
    mantisa_rest = ''.join('0' for n in range(0, (23-len(mantissa_incomplete)))) # rest of mantissa with 0
    result = f'{sign}{exponent_binary}{mantissa_incomplete}{mantisa_rest}'  # final format of IEEE754 format
    return result

if __name__ == "__main__":
    main()