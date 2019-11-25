# imports go here
BASENUM = '0123456789abcdef'


def num_sum(numbers):
    # three laws:
    # our base base
    if len(numbers) == 0:
        return 0
    else:
        # list splicing moves us towards the base case
        # calling num_sum is the recursion
        return numbers[0] + num_sum(numbers[1:])


def int_to_base(i, base=10):
    """
    Convert a base-10 int to its string representation
    May specify the base for the string representation
    :param i: base-10 int
    :param base: new base to convert to
    :return: str
    """
    # our base case: if i < base we can't resonably divide further
    # thus, return the str representation of i
    if i < base:
        return BASENUM[i]
    # we approach the base case by passing in the quotient of i div base
    # the remainder gives us what we need to convert for the current call
    return int_to_base(i // base, base) + BASENUM[i % base]


def main():
    l0 = [1, 2, 3, 4, 5]
    l1 = [0, 1, 1, 2, 3, 5, 8, 13, 21]
    print(num_sum(l0))
    print(num_sum(l1))

    print(int_to_base(9))
    print(int_to_base(11, 2))
    print(int_to_base(11, 16))
    print(int_to_base(769, 11))


if __name__ == '__main__':
    main()
