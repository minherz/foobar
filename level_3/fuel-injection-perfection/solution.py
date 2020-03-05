def zeros(i):
    count = 0
    while (i & 1) == 0:
        i = i >> 1
        count += 1
    return count

def solution(n):
    i = long(n)
    steps = 0
    while (i > 1):
        if i & 1 == 0:
            i = i >> 1
        else:
            a = i + 1
            b = i - 1
            if zeros(a) < zeros(b) or i == 3:
                i = b
            else:
                i = a
        steps += 1
    return steps