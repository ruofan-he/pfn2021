import numpy as np
import sys

def algo(s):
    s = list(s)
    convert_dict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15
    }
    s = [convert_dict.get(i) for i in s]
    l = []
    count = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            for k in range(j+1,len(s)):
                l.append(16**2 * s[i] + 16 * s[j] + s[k])
    return np.min(l)

if __name__ == '__main__':
    for l in sys.stdin:
        result = algo(l.rstrip('\r\n'))
        print(result)