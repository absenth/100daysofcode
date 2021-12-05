import os



def main():
    diagnostics, bits = array_setup()
    bit_counter(diagnostics, bits)


def array_setup():
    diagnostics = []
    f = open('input-test', 'r')
    for line in f.readlines():
        diagnostics.append(line.split())
    bits = len(diagnostics[0][0])
    return diagnostics, bits

def bit_counter(diagnostics, bits):
    p0 = p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = p10 = p11 = p12 = 0
    for diagnostic in diagnostics:
        for bit in range(bits):
            if diagnostic[0][bit] == "1":
                p+bit += 1
    print(f"{p0}, {p1}, {p2}, {p3}, {p4}")



if __name__ == "__main__":
    main()
