# imports go here
PEGS = [[], [], []]
POSITIONS = {
    '01': 2,
    '02': 1,
    '10': 2,
    '12': 0,
    '20': 1,
    '21': 0
}


def towers(height, start, end):
    """
    Solve the Towers of Hanoi puzzle
    :return: None
    """
    if height == 1:
        ring = PEGS[start].pop()
        PEGS[end].append(ring)
        print(PEGS)
    else:
        intermediate = POSITIONS[str(start) + str(end)]
        towers(height - 1, start, intermediate)
        ring = PEGS[start].pop()
        PEGS[end].append(ring)
        print(PEGS)
        towers(height - 1, intermediate, end)


def main():
    global PEGS
    PEGS = [
        [5,4,3,2,1],
        [],
        []
    ]
    print("NEW GAME")
    towers(5, 0, 2)
    PEGS = [
        [],
        [5,4,3,2,1],
        []
    ]
    print("NEW GAME")
    towers(5, 1, 2)

if __name__ == '__main__':
    main()
