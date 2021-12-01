import os
import time

depths = open("input", "r")

def main():
    step = 0
    count = 0
    for depth in depths:
        if step == 0:
            c_depth = int(depth)
            print(f"S{step}, D{c_depth}")
        else:
            if int(depth) > c_depth:
                count += 1
                print(f"S{step}, C{count}, D{c_depth}, ND{depth}")
            c_depth = int(depth)
        step +=1
    print(f"in {step} steps, we got a count of {count}")


if __name__ == "__main__":
    main()

    
'''
The Problem:
    For each depth in the INPUT file, provide a total count for the number of times our new depth is deeper than our previous depth
'''
