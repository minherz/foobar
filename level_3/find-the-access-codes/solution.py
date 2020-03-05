def find_all_dividables(l):
    dividables = dict()
    ll = len(l)
    for i in range(0, ll):
        dividables[i] = list()
        for j in range(i + 1, ll):
            if l[j] % l[i] == 0:
                dividables[i].append(j)
    return dividables

def solution(l):
    if len(l) < 3:
        return 0
    m = find_all_dividables(l)
    result = 0
    for i, _ in enumerate(l):
        if len(m[i]) > 0:
            for j in m[i]:
                result += len(m[j])
    return result
