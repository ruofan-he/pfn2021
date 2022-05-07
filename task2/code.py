def algo(b, k):
    m = len(b)
    l = [1]
    for i in range(k):
        memory = [0 for j in range(len(l) + m - 1 )]
        for j, v in enumerate(l):
            for p, u in enumerate(b):
                memory[j+p] += v*u
        l = memory

    output = l
    assert len(output) == (k*(m-1) + 1)
    return output

if __name__ == '__main__':
    m, k = map(int, input().split(' '))
    b = list(map(int, input().split(' ')))
    result = list(map(str,algo(b, k)))
    s = ' '.join(result)
    print(s)