PATCHED_REVERSES = [
    [[True,False],[False,False]],
    [[False,True],[False,False]],
    [[False,False],[True,False]],
    [[False,False],[False,True]]
]
NOT_PATCHED_REVERSES = [
    # 0 patches
    [[False,False],[False,False]],
    # 2 patches
    [[True,True],[False,False]],
    [[False,False],[True,True]],
    [[True,False],[True,False]],
    [[False,True],[False,True]],
    [[True,False],[False,True]],
    [[False,True],[True,False]],
    # 3 patches
    [[True,True],[True,False]],
    [[True,True],[False,True]],
    [[True,False],[True,True]],
    [[False,True],[True,True]],
    # 4 patches
    [[True,True],[True,True]],
]
TEMPLATE1 = '{0:0'
TEMPLATE2 = 'b}'

class Nebula:
    def __init__(self):
        self.nmap = [0]
        self.w = self.h = 1

    def __eq__(self, other):
        return hash(self) == hash(other)
        
    def __hash__(self):
        l = ''
        t = TEMPLATE1 + self.w + TEMPLATE2
        for r in self.nmap:
            l += t.format(r)
        return hash(l)

    def __str__(self):
        l = ''
        t = TEMPLATE1 + self.w + TEMPLATE2 + '\n'
        for r in self.nmap:
            l += t.format(r)
        return l.replace('0', '.').replace('1', 'o').rstrip()

    @classmethod
    def empty(cls, height, width):
        n = Nebula()
        n.nmap = [0] * width
        n.w = width
        n.h = height
        return n

    @classmethod
    def from_array(cls, array):
        n = Nebula()
        n.w = len(array[0])
        n.h = len(array)
        n.nmap = [0] * n.w
        for x in range(n.h):
            gx = g[x]
            b = 1 << x
            for y in range(n.w):
                if array[x][y]:
                    n.nmap[y] |= b
        return n

    def clone(self):
        another = Nebula()
        another.w, another.h = self.w, self.h
        another.nmap = [v for v in self.nmap]
        return another

    def width(self):
        return self.w

    def height(self):
        return self.h

    def apply_patch(self, start_x, start_y, patch):
        for x in range(2):
            for y in range(2):
                self.nmap[start_x+x][start_y+y] = patch[x][y]
        return self

    def count_patches(self, start_x, start_y):
        count = 0
        for x in range(start_x, start_x+2):
            for y in range(start_y, start_y+2):
                if self.nmap[x][y]:
                    count += 1
        return count

    def valid(self, next, x, y):
        if x < 0 or y < 0 or x+1 > next.rows() or y+1 > next.cols():
            return True
        p = next.nmap[x][y]
        n = self.count_patches(x, y)
        return (p and n == 1) or (not p and n != 1)

# end of class Nebula


def eval_nebulas(g, x, y, results):
    if not results:
        results.add(Nebula.empty(g.rows()+1, g.cols()+1))
    for r in list(results):
        results.discard(r)
        patches = PATCHED_REVERSES if g.nmap[x][y] else NOT_PATCHED_REVERSES
        for p in patches:
            #TBD: recursion is here
            s = r.clone().apply_patch(x, y, p)
            if s.valid(g, x, y) and s.valid(g, x+1, y) and s.valid(g, x, y+1) and s.valid(g, x+1, y+1):
                results.add(s)

def solution(g):
    results = set()
    g = Nebula.from_array(g)
    for y in range(g.cols()-1,-1,-1):
        for x in range(g.rows()-1,-1,-1):
            eval_nebulas(g, x, y, results)
    for r in results:
        print r
        print '-' * r.cols()
    return len(results)