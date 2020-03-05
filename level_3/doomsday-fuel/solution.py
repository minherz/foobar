from fractions import Fraction

def reshufle(r, terminals):
    offset = 0
    for i in terminals:
        v = r[i]
        del r[i]
        r.insert(offset, v)
        offset +=1
    return r

def order_matrix(M):
    # get row indices for terminal and non-terminal states
    terminals = []
    transients = []
    for i, l in enumerate(M):
        if sum(l) == 0:
            terminals.append(i)
        else:
            transients.append(i)
    # set 100% probability to stay in the state
    for i in terminals:
        M[i][i] = 1
    # shuffle rows to have terminal rows first and shuffle columns to have columns with indices of terminal states first
    newm = []
    for i in terminals:
        newm.append(reshufle(M[i], terminals))
    for i in transients:
        newm.append(reshufle(M[i], terminals))
    # convert to fraction (probabilities)
    for r in newm:
        denum = sum(r)
        for i, v in enumerate(r):
            r[i] = Fraction(v, denum)
    R = []
    Q = []
    for i in range(-len(transients), 0):
        R.append(newm[i][:len(terminals)])
        Q.append(newm[i][len(terminals):])
    return R, Q

def matrix_multiply(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    C = [[0 for i in range(colsB)] for j in range(rowsA)]
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total
    return C

def copy_matrix(M):
    MC = []
    for mr in M:
        nr = list(mr)
        MC.append(nr)
    return MC

def identity_matrix(size):
    M = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        M[i][i] = Fraction(1,1)
    return M

def calculate_f(Q):
    size = len(Q)
    I = identity_matrix(size)
    ImQ = []
    for i in range(size):
        r = []
        for j in range(size):
            r.append(I[i][j] - Q[i][j])
        ImQ.append(r)
    # calculate inverse
    ImQM = copy_matrix(ImQ)
    IM = copy_matrix(I)
    n = len(ImQ)
    indices = list(range(n)) # to allow flexible row referencing ***
    for fd in range(n): # fd stands for focus diagonal
        fdScaler = Fraction(1,1) / ImQM[fd][fd]
        # FIRST: scale fd row with fd inverse. 
        for j in range(n): # Use j to indicate column looping.
            ImQM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        # SECOND: operate on all rows except fd row as follows:
        for i in indices[0:fd] + indices[fd+1:]: 
            # *** skip row with fd in it.
            crScaler = ImQM[i][fd] # cr stands for "current row".
            for j in range(n): 
                # cr - crScaler * fdRow, but one element at a time.
                ImQM[i][j] = ImQM[i][j] - crScaler * ImQM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]    
    return IM

def gcd(a, b):
    while b: 
       a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) / gcd(a, b)


def format_answer(A):
    maxdenum = A[0].denominator
    for f in A[1:]:
        maxdenum = lcm(maxdenum, f.denominator)
    ans = []
    for f in A:
        ans.append(f.numerator * (maxdenum / f.denominator))
    ans.append(maxdenum)
    return ans

def solution(m):
    mtag = copy_matrix(m)
    R, Q = order_matrix(mtag)
    if not R and not Q:
        return [1, 1]
    F = calculate_f(Q)
    FR = matrix_multiply(F, R)
    return format_answer(FR[0])