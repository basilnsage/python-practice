# imports go here
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...


def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iter(n):
    first = 0
    second = 1
    for _ in range(n):
        first, second = first + second, first
    return first


def main():
    for i in range(1, 10):
        print(fib_recursive(i))
    for i in range(1, 10):
        print(fib_iter(i))


if __name__ == '__main__':
    main()
