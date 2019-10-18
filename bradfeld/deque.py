# hotpotato implemention, working off https://bradfieldcs.com/algos/
# imports go here
from collections import deque


# number of times to rotate
def hotpotato(d, num):
    while len(d) > 1:
        d.rotate(num)
        tossed = d.pop()
        print(f'{tossed} has left the game')
    winner = d[0]
    print(f'{winner} has won the game! All hail Master Tosser {winner}!')


def is_palindrome(s):
    s_deque = deque(s)
    for _ in range(len(s) // 2):
        if s_deque.popleft() != s_deque.pop():
            return False
    return True


def main():
    tosser_roster = [
        'cloud',
        'tifa',
        'barret',
        'yuffie',
        'sid',
        'red xiii',
        'vincent',
        'cait sith',
        'aeris'
    ]
    potato_tossers = deque(tosser_roster)

    hotpotato(potato_tossers, 5)
    potato_tossers = deque(tosser_roster)
    hotpotato(potato_tossers, 11)

    print(is_palindrome('toot'))
    print(is_palindrome('tootoot'))
    print(is_palindrome('root'))
    print(is_palindrome('racecar'))
    print(is_palindrome('tacocat'))
    print(is_palindrome('leroyjenkins'))
    print(is_palindrome(''))



if __name__ == '__main__':
    main()
