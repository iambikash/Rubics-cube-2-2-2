
rgw = flu = 0 # (0-th cubie; front face)
gwr = luf = 1 # (0-th cubie; left face)
wrg = ufl = 2 # (0-th cubie; up face)

rwb = fur = 3 # (1-st cubie; front face)
wbr = urf = 4 # (1-st cubie; up face)
brw = rfu = 5 # (1-st cubie; right face)

ryg = fdl = 6 # (2-nd cubie; front face)
ygr = dlf = 7 # (2-nd cubie; down face)
gry = lfd = 8 # (2-nd cubie; left face)

rby = frd = 9 #  (3-rd cubie; front face)
byr = rdf = 10 # (3-rd cubie; right face)
yrb = dfr = 11 # (3-rd cubie; down face)

owg = bul = 12 # (4-th cubie; back face)
wgo = ulb = 13 # (4-th cubie; up face)
gow = lbu = 14 # (4-th cubie; left face)

obw = bru = 15 # (5-th cubie; back face)
bwo = rub = 16 # (5-th cubie; right face)
wob = ubr = 17 # (5-th cubie; up face)

ogy = bld = 18 # (6-th cubie; back face)
gyo = ldb = 19 # (6-th cubie; left face)
yog = dbl = 20 # (6-th cubie; down face)

oyb = bdr = 21 # (7-th cubie; back face)
ybo = drb = 22 # (7-th cubie; down face)
boy = rbd = 23 # (7-th cubie; right face)

def perm_apply(perm, position):
    return tuple([position[i] for i in perm])

def perm_inverse(p):
    n = len(p)
    q = [0]*n
    for i in range(n):
        q[p[i]] = i
    return tuple(q)

def perm_to_string(p):
    """
    Convert p to string, slightly more compact
    than list printing.
    """
    s = "("
    for x in p: s = s + "%2d "%x
    s += ")"
    return s

# Identity: equal to (0, 1, 2, ..., 23).
I = (flu, luf, ufl, fur, urf, rfu, fdl, dlf, lfd, frd, rdf, dfr,bul, ulb, lbu, bru, rub, ubr, bld, ldb, dbl, bdr, drb, rbd)

"""
When any of the following Rubik's cube permutations are applied, the three faces on a cubie naturally stay together:
{0,1,2}, {3,4,5}, ..., {21,22,23}.
"""

# Front face rotated clockwise.
F = (fdl, dlf, lfd, flu, luf, ufl, frd, rdf, dfr, fur, urf, rfu, bul, ulb, lbu, bru, rub, ubr, bld, ldb, dbl, bdr, drb, rbd)
# Front face rotated counter-clockwise.
Fi = perm_inverse(F)

# Left face rotated clockwise.
L = (ulb, lbu, bul, fur, urf, rfu, ufl, flu, luf, frd, rdf, dfr,dbl, bld, ldb, bru, rub, ubr, dlf, lfd, fdl, bdr, drb, rbd)
# Left face rotated counter-clockwise.
Li = perm_inverse(L)

# Upper face rotated clockwise.
U = (rfu, fur, urf, rub, ubr, bru, fdl, dlf, lfd, frd, rdf, dfr,luf, ufl, flu, lbu, bul, ulb, bld, ldb, dbl, bdr, drb, rbd)
# Upper face rotated counter-clockwise.
Ui = perm_inverse(U)

# All 6 possible moves (assuming that the lower-bottom-right cubie
# stays fixed).
quarter_twists = (F, Fi, L, Li, U, Ui)

quarter_twists_names = {}
quarter_twists_names[F] = 'F'
quarter_twists_names[Fi] = 'Fi'
quarter_twists_names[L] = 'L'
quarter_twists_names[Li] = 'Li'
quarter_twists_names[U] = 'U'
quarter_twists_names[Ui] = 'Ui'
