def failure_function(P):
    print('Generating failure function for pattern = ', P)
    f = [0] * len(P)
    m = len(P)

    f[0] = 0

    k = 1
    x = 0

    while k < m:
        if P[k] == P[x]:
            f[k] = x + 1
            k += 1
            x += 1
        else:
            if x == 0:
                f[k] = 0
                k += 1
            else:
                x = f[x - 1]
                
    return f

def KMP_search(T, P):
    n = len(T)
    m = len(P)

    # if len(P) == 0:
    #     return -1
    
    f = failure_function(P)

    i0 = 0
    i = 0
    j = 0

    while i < n:
        if P[j] == T[i]:
            i += 1
            j += 1
            if j == m:
                return i0
        else:
            if j == 0:
                i0 += 1
                i = i0
                j = 0
            else:
                k = f[j - 1]
                j = k
                i0 = i - j
    
    return -1

# T = "baaababbaaabaabaabaaaaa"
# P = "baabaaax"

# r = KMP_search(T, P)

# if r == -1:
#     print('Not found')
# else:
#     print('Found at ',r)