def find_sequences(l, t):
    i, j = 0, 0
    sum_ = 0
    while True:
        try:
            if sum_ < t:
                sum_ += l[j]
                j += 1
            elif sum_ == t:
                yield i, (j-1)
                sum_ -= l[i]
                i += 1
            else:
                sum_ -= l[i]
                i += 1
        except IndexError:
            break

def solution(l, t):
    all_results = list(find_sequences(l, t))
    if not all_results:
        return [-1, -1]
    i, j = min(all_results, key=lambda x: "{0:3d}.{1:3d}".format(x[0], x[1] - x[0]))
    return [i, j]
