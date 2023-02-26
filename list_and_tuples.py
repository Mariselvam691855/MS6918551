def last(n):
    return n[-1]

def list(tuples):
    return sorted(tuples, key=last)

print(list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))        