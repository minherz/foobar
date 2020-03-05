def gcd(a, b):
    while b: 
       a, b = b, a % b
    return a

def is_loop(a, b):
    r = (a+b)/gcd(a,b)
    return bool(r & (r-1))

def remove_guard(guard, guards):
    for i in range(len(guards)):
        try:
            guards[i].remove(guard)
        except ValueError:
            pass
    guards[guard] = [-1]

def solution(banana_list):
    ll = len(banana_list)
    guards = [[] for _ in range(ll)]
    for i in range(ll):
        for j in range(ll):
            if is_loop(banana_list[i], banana_list[j]):
                guards[i].append(j)
    unprocessed = ll
    unpaired = 0
    while unprocessed > 0: 
        next_guard = 0
        for i in range(1, ll):
            if (len(guards[i]) < len(guards[next_guard]) or guards[next_guard] == [-1]) and guards[i] != [-1]:
                next_guard = i
        if len(guards[next_guard]) == 0:
            remove_guard(next_guard, guards)
            unpaired += 1
        else:
            next_guard_pair = guards[next_guard][0]
            for i in range(1, len(guards[next_guard])):
                another = guards[next_guard][i]
                if len(guards[next_guard_pair]) > len(guards[another]):
                    next_guard_pair = another
            remove_guard(next_guard, guards)
            remove_guard(next_guard_pair, guards)
            unprocessed -=1
        unprocessed -=1
    return unpaired