# from Bradfeld Practical Algorithms and Data Structures
# chapter titled Searching
# imports go here


def recursive_bin_search(olist, item):
    if len(olist) == 0:
        return False
    i = len(olist) // 2
    if olist[i] == item:
        return True
    elif item > olist[i]:
        return recursive_bin_search(olist[i + 1:], item)
    else:
        return recursive_bin_search(olist[:i], item)


def iterative_bin_search(olist, item):
    if len(olist) == 0:
        return False
    i = len(olist) // 2
    top_i = len(olist) - 1
    bottom_i = 0
    while True:
        if olist[i] == item:
            return True
        if i == bottom_i or i == top_i:
            return False
        # item is greater than the mid point so search upper half of list
        # we won't go lower than the mid point, so update bottom index
        if item > olist[i]:
            bottom_i = i + 1
            i += (1 + top_i - i) // 2
        # item is less than them mid point, so search bottom half of list
        # we wont go higher than the mid point, so update top index
        elif item < olist[i]:
            top_i = i - 1
            i -= (1 + i - bottom_i) // 2


def recursive_bin_search_idx(olist, bottom, top, item):
    if top < bottom:
        return False
    i = bottom + (top - bottom) // 2
    if olist[i] == item:
        return True
    elif item > olist[i]:
        return recursive_bin_search_idx(olist, i + 1, top, item)
    else:
        return recursive_bin_search_idx(olist, bottom, top - 1, item)


def iterative_bin_search_idx(olist, bottom, top, item):
    while bottom <= top:
        i = bottom + (top - bottom) // 2
        if olist[i] == item:
            return True
        elif item > olist[i]:
            bottom = i + 1
        else:
            top = i - 1
    return False



def main():
    l1 = [0]
    l2 = []
    l3 = [0, 1, 2, 3, 4, 5]

    print("print testing recursive binary search")
    print(recursive_bin_search(l1, 0))
    print(recursive_bin_search(l1, 1))
    print(recursive_bin_search(l2, 0))
    print(recursive_bin_search(l3, 0))
    print(recursive_bin_search(l3, 2))
    print(recursive_bin_search(l3, -1))
    print(recursive_bin_search(l3, 6))

    print("print testing iterative binary search")
    print(iterative_bin_search(l1, 0))
    print(iterative_bin_search(l1, 1))
    print(iterative_bin_search(l2, 0))
    print(iterative_bin_search(l3, 0))
    print(iterative_bin_search(l3, 2))
    print(iterative_bin_search(l3, -1))
    print(iterative_bin_search(l3, 6))

    print("testing recursive binary search with indexes")
    print(recursive_bin_search_idx(l1, 0, len(l1) - 1, 0))
    print(recursive_bin_search_idx(l1, 0, len(l1) - 1, 1))
    print(recursive_bin_search_idx(l2, 0, len(l2) - 1, 0))
    print(recursive_bin_search_idx(l3, 0, len(l3) - 1, 1))
    print(recursive_bin_search_idx(l3, 0, len(l3) - 1, 4))
    print(recursive_bin_search_idx(l3, 0, len(l3) - 1, -1))
    print(recursive_bin_search_idx(l3, 0, len(l3) - 1, 6))

    print("testing recursive binary search with indexes")
    print(iterative_bin_search_idx(l1, 0, len(l1) - 1, 0))
    print(iterative_bin_search_idx(l1, 0, len(l1) - 1, 1))
    print(iterative_bin_search_idx(l2, 0, len(l2) - 1, 0))
    print(iterative_bin_search_idx(l3, 0, len(l3) - 1, 1))
    print(iterative_bin_search_idx(l3, 0, len(l3) - 1, 4))
    print(iterative_bin_search_idx(l3, 0, len(l3) - 1, -1))
    print(iterative_bin_search_idx(l3, 0, len(l3) - 1, 6))


if __name__ == '__main__':
    main()
