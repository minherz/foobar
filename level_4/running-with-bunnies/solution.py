from itertools import permutations

def edges(times):
    sz = len(times)
    for u in range(sz):
        for w in range(sz):
            yield u, w, times[u][w]

def bellman_ford(times, start):
    sz = len(times)
    distance = [9999 for _ in range(sz)]
    distance[start] = 0
    for _ in range(sz - 1):
        for u, w, t in edges(times):
            if distance[u] + t < distance[w]:
                distance[w] = distance[u] + t
    for u, w, t in edges(times):
        if distance[u] + t < distance[w]:
            return distance, True
    return distance, False

def calc_time(path, distances, start_time):
    time = start_time
    for i in range(len(path)-1):
        u, w = path[i], path[i+1]
        time -= distances[u][w]
    return time

def find_min_bunny_id(saved_bunies):
    min_id = 10
    min_index = 10
    for i, lst in enumerate(saved_bunies):
        n = min(lst)
        if n < min_id:
            min_id = n
            min_index = i
    return saved_bunies[min_index]

def solution(times, time_limit):
    distances, sz = [], len(times)
    for i in range(sz):
        d, f = bellman_ford(times, i)
        if f is True:
            return [i for i in range(sz-2)]
        distances.append(d)
    bunny_ids = [i for i in range(1, sz-1)]
    answer = []
    for n in range (sz-1, 0, -1):
        for ids in permutations(bunny_ids, n):
            if calc_time([0] + list(ids) + [(sz-1)], distances, time_limit) >= 0:
                answer = min(answer, ids) if len(answer) > 0 else ids
        if len(answer) > 0:
            return [(i-1) for i in sorted(answer) ]
    return answer
