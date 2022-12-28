
def in_all(l):
    """
    Takes a list of lists and returns the elements that are in
    all this list of lists
    """

    corres = l[0]
    for autre_l in l:
        for item in corres:
            if not item in autre_l:
                corres.remove(item)
    return corres



def t(bit0, bit1, bit2, bit3, resultat):
    """
    Returns all possible combinations for the 4 bits in parameter
    to give the result resultat
    
    bit0, bit1, bit2, bit4 -> int or str that is either a 0 or 1
    resultat -> str that is 4 time a 0 or 1
    """
    bit0 = int(bit0)
    bit1 = int(bit1)
    bit2 = int(bit2)
    bit3 = int(bit3)
    resultat = int(resultat)
    possible = ["^", "|", "&"]
    possible2 = ["bit0", "bit1", "bit2", "bit3"]

    results = []

    # test each combination
    for b1 in possible2:
        temp_pos = possible2[:]
        temp_pos.remove(b1)
        for b2 in temp_pos:
            temp_pos1 = temp_pos
            temp_pos1.remove(b2)
            for b3 in temp_pos1:
                temp_pos2 = temp_pos1
                temp_pos2.remove(b3)
                for b4 in temp_pos2:
                    for op1 in possible:
                        for op2 in possible:
                            for op3 in possible:
                                # if the result is good then add it to our list
                                if eval(f"{b1}{op1}{b2}{op2}{b3}{op3}{b4} == resultat"):
                                    results.append(f"{b1}{op1}{b2}{op2}{b3}{op3}{b4}")
    return results

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

    equ0 = []
    equ1 = []
    equ2 = []
    equ3 = []

    for input, expected in data.items():
        for i in range(4):
            eval(f"equ{i}.append(t(input[0], input[1], input[2], input[3], expected[i]))")


    # Once each possibilty has been tried, we only
    # print those who are true for all the inputs
    print("equ0 :", in_all(equ0))
    print("equ1 :", in_all(equ1))
    print("equ2 :", in_all(equ2))
    print("equ3 :", in_all(equ3))

test()