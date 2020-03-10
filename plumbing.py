#!/usr/bin/env python3
def get_answer():
    f = open('in.txt', 'r', encoding='utf-8')
    n = 0
    v = 0
    d1 = {}
    d2 = {}
    c = 0
    for line in f:
        if c == 0:
            n = int(line)
            d1 = {i: [] for i in range(1, n + 1)}
            d2 = {i: [] for i in range(1, n + 1)}
        elif c <= n:
            k = 0
            arr = line.split()
            for el in arr:
                if k == 0:
                    k += 1
                else:
                    d1[c].append(int(el))
        else:
            v = int(line)
        c += 1
    f.close()
    for key in d1.keys():
        if key == v:
            for el in d1[key]:
                d2[key].append(el)
        else:
            for el in d1[key]:
                if el == v:
                    d2[key].append(el)
                else:
                    d2[el].append(key)
    visited = {v}
    queue = [v]
    while len(queue) != 0:
        node = queue.pop(0)
        if len(visited) == n:
            break
        for child in d2[node]:
            if child not in visited:
                queue.append(child)
                visited.add(child)
    if len(visited) == n:
        answer = '{0} {1}'.format(v, 1)
    else:
        answer = '{0} {1}'.format(v, 0)
    f = open('out.txt', 'w', encoding='utf-8')
    f.write(answer)
    f.close()


if __name__ == '__main__':
    get_answer()
