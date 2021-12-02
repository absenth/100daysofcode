import os

def main():
    forward, up, down, move = array_setup()
    x = sum_forward(forward)
    pos_y = sum_up(up)
    neg_y = sum_down(down)
    part1_distance = part1(x, pos_y, neg_y)
    part2_distance = part2(move)
    print(f"part 1 distanceance traveled is {part1_distance}")
    print(f"part 2 distance traveled is {part2_distance}")


def array_setup():
    forward = []
    up = []
    down = []
    move = []
    f = open('input', 'r')
    for line in f.readlines():
        direction,distance = line.split(' ')
        move.append([direction,int(distance)])
        if direction == 'forward':
            forward.append([direction,int(distance)])
        elif direction == 'up':
            up.append([direction,int(distance)])
        else:
            down.append([direction,int(distance)])
    return forward, up, down, move


def part1(x, pos_y, neg_y):
    part1_distance = abs(pos_y - neg_y) * x
    return part1_distance


def part2(move):
    a = 0
    x = 0
    y = 0
    for dest in move:
        if dest[0] == 'forward':
            if a == 0:
                x = x + dest[1]
            else:
                x = x + dest[1]
                y = y + (a * dest[1])
        elif dest[0] == 'down':
            a = a + dest[1]
        else:
            a = a - dest[1]
    traveled = (x * y)
    return traveled


def sum_forward(forward):
    x = 0
    for dest in forward:
        x += dest[1]
    return x


def sum_up(up):
    pos_y = 0
    for dest in up:
        pos_y += dest[1]
    return pos_y


def sum_down(down):
    neg_y = 0
    for dest in down:
        neg_y += dest[1]
    return neg_y


if __name__ == "__main__":
    main()
