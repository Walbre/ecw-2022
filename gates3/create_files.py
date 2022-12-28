from time import perf_counter



def t(bit0, bit1, bit2, bit3, bit4, bit5, bit6, bit7, resultat):
    bit0 = int(bit0)
    bit1 = int(bit1)
    bit2 = int(bit2)
    bit3 = int(bit3)
    bit4 = int(bit4)
    bit5 = int(bit5)
    bit6 = int(bit6)
    bit7 = int(bit7)
    resultat = int(resultat)
    possible = ["^", "|", "&"]
    possible2 = ["bit0", "bit1", "bit2", "bit3", "bit4", "bit5", "bit6", "bit7"]

    results = []

    for b1 in possible2:
        temp_pos = possible2[:]
        temp_pos.remove(b1)
        for b2 in temp_pos:
            temp_pos1 = temp_pos
            temp_pos1.remove(b2)
            for b3 in temp_pos1:
                temp_pos2 = temp_pos1[:]
                temp_pos2.remove(b3)
                for b4 in temp_pos2:
                    temp_pos3 = temp_pos2[:]
                    temp_pos3.remove(b4)
                    for b5 in temp_pos3:
                        temp_pos4 = temp_pos3[:]
                        temp_pos4.remove(b5)
                        for b6 in temp_pos4:
                                    for op1 in possible:
                                        for op2 in possible:
                                            for op3 in possible:
                                                for op4 in possible:
                                                    for op5 in possible:
                                                                if eval(f"{b1}{op1}{b2}{op2}{b3}{op3}{b4}{op4}{b5}{op5}{b6} == resultat"):
                                                                    results.append(f"{b1}{op1}{b2}{op2}{b3}{op3}{b4}{op4}{b5}{op5}{b6}")
    return results

def test():
    data = {
    "01101001" : "11111111",
    }

    equ0 = []
    equ1 = []
    equ2 = []
    equ3 = []
    equ4 = []
    equ5 = []
    equ6 = []
    equ7 = []

    for input, expected in data.items():
        for i in range(8):
            print(f"Starting equ{i}")
            print("starting time:", perf_counter())
            eval(f"equ{i}.append(t(input[0], input[1], input[2], input[3], input[4], input[5], input[6], input[7], expected[i]))")
            with open("eq"+str(i), 'w') as f:
                f.write(str(eval("equ"+str(i))))
            print("ending time:", perf_counter())

test()
