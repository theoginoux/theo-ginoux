def p(n, f):
    """
    TODO
    """
    b = [False, True]
    for i in b:
        for j in b:
            print(f"{i} {n} {j} = {f(i, j)}")


if __name__ == "__main__":
    p("&", lambda x, y: x and y) #et
    p("|", lambda x, y: x or y)  #ou inclusif
    p("^", lambda x, y: x ^ y)  #ou exclusif


def met_ordre_alphabet(u):
    """
    TODO
    """
    s = []
    while u:
        i = None
        m = None
        for j, k in enumerate(u):
            if m is None or ord(k) < m:
                m = ord(k)
                i = j
        assert i is not None
        s.append(u[i])
        u = u[:i] + u[i + 1 :]
    return "".join(s)


if __name__ == "__main__":
    print(met_ordre_alphabet("qwertyuiop"))
    print(met_ordre_alphabet("asdfghjkl"))
    print(met_ordre_alphabet("zxcvbnm"))