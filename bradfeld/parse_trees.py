# from Bradfeld Practical Algorithms and Data Structures
# chapter on Trees/Parse Trees
# imports go here
import copy
import string


OPERATORS = ['+', '-', '*', '/']
NEW_NODE = {
    'value': None,
    'left': None,
    'right': None
}


def parse_math_expr(s):
    parse_tree = copy.copy(NEW_NODE)
    curr = parse_tree
    prev = []
    for c in s:
        print(c)
        if c in string.whitespace:
            continue
        elif c == '(':
            curr['left'] = copy.copy(NEW_NODE)
            prev.append(curr)
            curr = curr['left']
        elif c in OPERATORS:
            curr['value'] = c
            curr['right'] = copy.copy(NEW_NODE)
            prev.append(curr)
            curr = curr['right']
        elif c != ')':
            curr['value'] = c
            curr = prev.pop()
        elif c == ')':
            if len(prev) > 0:
                curr = prev.pop()
        else:
            raise TypeError(f'unable to parse character: {c}')
    return parse_tree


def main():
    s = '(1 + 1)'
    print(parse_math_expr(s))


if __name__ == '__main__':
    main()
