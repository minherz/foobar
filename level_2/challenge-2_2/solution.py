def max_solution(total_lambs):
    henchmen = [1]
    total_lambs -= 1
    while True:
        lambs = henchmen[-1]
        if len(henchmen) > 1:
            lambs += henchmen[-2]
        if total_lambs - lambs < 0:
            break
        henchmen.append(lambs)
        total_lambs -= lambs
    return len(henchmen)

def min_solution(total_lambs):
    count = 1
    lambs = 1
    total_lambs -= 1
    while True:
        if total_lambs - (lambs * 2) < 0:
            break
        count += 1
        total_lambs -= lambs * 2
        lambs = lambs * 2

    return count

def​ ​solution(total_lambs):
    return max_solution(total_lambs) - min_solution(total_lambs)