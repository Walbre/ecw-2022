

def circuit1(bit0, bit1, bit2, bit3):
    return bit0^bit1^bit2^bit3

def circuit2(bit0, bit1, bit2, bit3):
    return bit2&bit0|bit1|bit3

def circuit3(bit0, bit1, bit2, bit3):
    return bit2|bit0^bit1^bit3

def circuit4(bit0, bit1, bit2, bit3):
    return bit0 | bit1 | bit2 | bit3


def test():
    data = {
    "0101" : "0101",
    "0111" : "1111",
    "0110" : "0111",
    "0011" : "0111",
    "1001" : "0101",
    "1110" : "1111",
    "1011" : "1111",
    "0100" : "1111",
    "0001" : "1111",
    "1000" : "1011",
    "1100" : "0101",
    "1010" : "0111"
    }

    for input, expected in data.items():
        bit0 = int(input[0])
        bit1 = int(input[1])
        bit2 = int(input[2])
        bit3 = int(input[3])

        c1 = circuit1(bit0, bit1, bit2, bit3)
        c2 = circuit2(bit0, bit1, bit2, bit3)
        c3 = circuit3(bit0, bit1, bit2, bit3)
        c4 = circuit4(bit0, bit1, bit2, bit3)

        print(f"Given     => {bit0}{bit1}{bit2}{bit3} : {c1}{c2}{c3}{c4}")
        print(f"Should be => {bit0}{bit1}{bit2}{bit3} : {expected}")

def generate():
    awn = ""
    for i in range(16):
        binary = "0"*(6-len(bin(i))) + bin(i).replace("0b", "")
        bit0 = int(binary[0])
        bit1 = int(binary[1])
        bit2 = int(binary[2])
        bit3 = int(binary[3])

        c1 = circuit1(bit0, bit1, bit2, bit3)
        c2 = circuit2(bit0, bit1, bit2, bit3)
        c3 = circuit3(bit0, bit1, bit2, bit3)
        c4 = circuit4(bit0, bit1, bit2, bit3)
        awn += f"{bit0}{bit1}{bit2}{bit3} : {c1}{c2}{c3}{c4}\n"

    print(awn)

test()
generate()