import os

initial_pos = 0
count = 0


def main():
    depths_array = array_setup()
    count = get_sums(depths_array)
    print(count)


def array_setup():
    depths_array = []
    with open("input") as depths:
        for depth in depths:
            depths_array.append(int(depth))

    return depths_array


def get_range(depths_array):
    windows = len(depths_array) / 3
    return int(windows)


def get_sums(depths_array):
    pos = 0
    current_depth = 0
    count = 0
    for window in range(len(depths_array) - 3 + 1):
        window_depth = depths_array[pos] + depths_array[pos + 1] + depths_array[pos + 2]
        if current_depth != 0:
            if current_depth < window_depth:
                count += 1
        current_depth = window_depth
        pos += 1
    return count


if __name__ == "__main__":
    main()

'''
The Problem:
using a sliding window of 3 depths from the INPUT file, count the number of times our new depth sum, is deeper than the current depth sum.
'''
