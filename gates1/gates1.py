

def circuit1(bit0, bit1, bit2, bit3):
    a = bit1^bit2
    b = bit0&bit3
    return a|b

def circuit2(bit0, bit1, bit2, bit3):
    a = bit1^bit3
    b = bit0^bit2
    return a|b

def circuit3(bit0, bit1, bit2, bit3):
    a = bit0^bit2
    b = a^bit1
    return b|bit3

def circuit4(bit0, bit1, bit2, bit3):
    a = bit0&bit2
    b = a&bit1
    return b&bit3

def main():
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
    
main()
