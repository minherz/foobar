HAS_GAS_PATCHES = [
    [[True,False],[False,False]],
    [[False,True],[False,False]],
    [[False,False],[True,False]],
    [[False,False],[False,True]]
]
NO_GAS_PATCHES = [
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

class Nebula:
    def __init__(self):
        self.nmap = [[False]] # 1x1 map
    
    @classmethod
    def empty(cls, sz_x, sz_y):
        n = Nebula()
        n.nmap = [[False for _ in range(sz_y)] for _ in range(sz_x)]
        return n

    @classmethod
    def from_array(cls, array):
        n = Nebula()
        n.nmap = [r[:] for r in array]
        return n

    def clone(self):
        another = Nebula.from_array(self.nmap)
        return another

    def rows(self):
        return len(self.nmap)

    def cols(self):
        return len(self.nmap[0])

    def __str__(self):
        l = ''
        for r in self.nmap:
            for b in r:
                l += 'o' if b else '.'
            l += '\n'
        return l.rstrip()

    def __eq__(self, other):
        return hash(self) == hash(other)
        
    def __hash__(self):
        l = ''
        for r in self.nmap:
            for b in r:
                l += 'o' if b else '.'
        return hash(l) 

    def __getitem__(self, x):
        return self.nmap[x]

    def count_patches(self, start_x, start_y):
        count = 0
        for x in range(start_x, start_x+2):
            for y in range(start_y, start_y+2):
                if self.nmap[x][y]:
                    count += 1
        return count

    def patch_area(self, start_x, start_y, patch):
        for x in range(2):
            for y in range(2):
                self.nmap[start_x+x][start_y+y] = patch[x][y]

    def check(self, x, y, expected):
        if x < 0 or y < 0 or x+1 > expected.rows() or y+1 > expected.cols():
            return True
        patched = expected[x][y]
        count = self.count_patches(x, y)
        return (patched and count == 1) or (not patched and count != 1)



def update_maps(current, x, y, maps, hashes):
    updates = []
    for m in maps:
        hashes.discard(hash(m))
        if current[x][y]:
            patches = HAS_GAS_PATCHES
            #optimize:
            n = m.count_patches(x, y)
            if n == 1:
                updates.append(m)
                hashes.add(hash(m))
            if n >= 1:
                continue
        else:
            patches = NO_GAS_PATCHES

        for p in patches:
            prev = m.clone()
            prev.patch_area(x, y, p)
            if (
                prev.check(x, y-1, current) and prev.check(x-1, y-1, current) and
                prev.check(x-1, y, current) and prev.check(x-1, y+1, current) and
                hash(prev) not in hashes
            ):
                updates.append(prev)
                hashes.add(hash(prev))
    return updates

def solution(g):
    hashes = set()
    g = Nebula.from_array(g)
    maps = [Nebula.empty(g.rows()+1, g.cols()+1)]
    for x in range(g.rows()):
        for y in range(g.cols()):
            maps = update_maps(g, x, y, maps, hashes)
    return len(hashes)
