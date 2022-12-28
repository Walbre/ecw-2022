
def c1(bit0, bit1, bit2, bit3, bit4, bit5, bit6, bit7):
    return bit0^bit1^bit3|bit2|bit5&bit7

def c2(bit0, bit1, bit2, bit3, bit4, bit5, bit6, bit7):
    return bit0^bit1^bit3^bit4^bit6^bit7

def c3(bit0, bit1, bit2, bit3, bit4, bit5, bit6, bit7):
    return bit2|bit3^bit4|bit5&bit7|bit6

def c4(bit0, bit1, bit2, bit3, bit4, bit5, bit6, bit7):
    return bit0|bit1&bit3&bit5^bit7|bit6

def c5(bit0, bit1, bit2, bit3, bit4, bit5, bit6, bit7):
    return bit3^bit0|bit1&bit5^bit2|bit4

def c6(bit0, bit1, bit2, bit3, bit4, bit5, bit6, bit7):
    return bit7&bit2&bit1^bit3&bit5&bit6

def c7(bit0, bit1, bit2, bit3, bit4, bit5, bit6, bit7):
    return bit0^bit1|bit3^bit4&bit7|bit5

def c8(bit0, bit1, bit2, bit3, bit4, bit5, bit6, bit7):
    return bit2^bit0|bit1^bit4|bit3^bit6

def create_bit(b0, b1, b2, b3, b4, b5, b6, b7):
    b0 = int(b0)
    b1 = int(b1)
    b2 = int(b2)
    b3 = int(b3)
    b4 = int(b4)
    b5 = int(b5)
    b6 = int(b6)
    b7 = int(b7)

    r1 = c1(b0, b1, b2, b3, b4, b5, b6, b7)
    r2 = c2(b0, b1, b2, b3, b4, b5, b6, b7)
    r3 = c3(b0, b1, b2, b3, b4, b5, b6, b7)
    r4 = c4(b0, b1, b2, b3, b4, b5, b6, b7)
    r5 = c5(b0, b1, b2, b3, b4, b5, b6, b7)
    r6 = c6(b0, b1, b2, b3, b4, b5, b6, b7)
    r7 = c7(b0, b1, b2, b3, b4, b5, b6, b7)
    r8 = c8(b0, b1, b2, b3, b4, b5, b6, b7)
    return f"{r1}{r2}{r3}{r4}{r5}{r6}{r7}{r8}"

def testing():
    tests = {
    "01101001" : "11111111",
    "11111001" : "11111101",
    "01001111" : "10111011",
    "01011001" : "00011011",
    "00111001" : "11111001",
    "11001010" : "00111001",
    "00000110" : "01110011",
    "01000011" : "11110011",
    "11110001" : "10111111",
    "00101110" : "10111011",
    "10011001" : "00011011",
    "11110111" : "11110011",
    "11001111" : "11111011",
    "01001101" : "11111010",
    "11100010" : "11111001",
    "10000100" : "11011011",
    "11111011" : "10111100",
    "00011110" : "11111111",
    "10101100" : "10111011",
    "11001001" : "00111011",
    "00110000" : "11101011",
    "00000100" : "00000010",
    "01000111" : "11111011",
    "01110001" : "11111111",
    "01110110" : "11111111",
    "10011000" : "01011011",
    "01011011" : "01111010",
    "00100010" : "11111001",
    "01100001" : "10111111",
    "10110000" : "10111011",
    "11110100" : "11110011",
    "10011110" : "00111111",
    "00011111" : "10111111",
    "10010101" : "11110011",
    "01011000" : "01001011",
    "11101001" : "10111110",
    "01111100" : "11111011",
    "01101100" : "10101011",
    "00001000" : "01101001",
    "11101011" : "11111111",
    "11100000" : "10111001",
    "10100101" : "10111010",
    "11011011" : "10111001",
    "00100001" : "11111001",
    "10011100" : "01011011",
    "01010100" : "00111011",
    "01010111" : "10111111",
    "00110001" : "10111011",
    "00001111" : "11111011",
    "10001110" : "11111011",
    "10111100" : "11111011",
    "10001001" : "11111011",
    "10101000" : "10111011",
    "11000100" : "00011011",
    "00111010" : "11111011",
    "11101110" : "10111011",
    "11001100" : "01111011",
    "01001011" : "10111011",
    "01011100" : "01011011",
    "11101101" : "10111110",
    "00110110" : "10111111",
    "00011100" : "10001011",
    "00010100" : "11101011",
    "11011010" : "11111011",
    "10111010" : "10111011",
    "10010000" : "00110011",
    "00001001" : "00111011",
    "11010011" : "11110011",
    "10001101" : "11111011",
    "00001011" : "01111011",
    "01000110" : "10111011",
    "11000010" : "01111001",
    "11111110" : "11111110",
    "00011010" : "11111011",
    "10010010" : "01110011",
    "11111010" : "11111010",
    "10011111" : "11111111",
    "00010000" : "11101011",
    "11101100" : "11111010",
    "11000000" : "00011001",
    "11100011" : "10111101",
    "00010010" : "10111010",
    "11010010" : "10110011",
    "01101000" : "10101011",
    "01100110" : "10110011",
    "10111011" : "11111011",
    "10101010" : "11111011",
    "10110001" : "11111011",
    "11000101" : "11111011",
    "00011101" : "11111011",
    "01001000" : "10101010",
    "11100111" : "10111111",
    "10100100" : "11111010",
    "10101001" : "11111011",
    "11011001" : "11011001",
    "11011111" : "10111111",
    "10110101" : "11111011",
    "01110101" : "11101111",
    "10010111" : "10110111",
    "01011111" : "11111110",
    "01011110" : "00111110",
    "01100101" : "10110111"
    }

    for input, output in tests.items():
        val = create_bit(input[0], input[1], input[2],input[3], input[4], input[5], input[6], input[7])
        if output == val:
            print("ok", input)
        else:
            print('bad :', output, "=>", val)

    print("data : ")
    for i in range(0x100):
        nb_bin = "0" * (10 - len(bin(i))) + bin(i).replace("0b", "")

        if not nb_bin in tests.keys():
            val = create_bit(nb_bin[0], nb_bin[1], nb_bin[2], nb_bin[3], nb_bin[4], nb_bin[5], nb_bin[6], nb_bin[7])
            print(f"{nb_bin} : {val}")


testing()

