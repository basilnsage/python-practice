# from Bradfeld Practical Algorithms and Data Structures
# section Searching/Hashing
# imports go here


# simple string hash
def naive_string_hash(s):
    return sum([ord(c) for c in s])


def better_string_hash(s):
    return sum([(i + 1) * ord(s[i]) for i in range(len(s))])
