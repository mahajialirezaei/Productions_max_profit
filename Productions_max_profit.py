def solve_product(p, l, m, L, M):
    p1, p2, p3 = p
    l1, l2, l3 = l
    m1, m2, m3 = m

    best_profit = -float('inf')
    best_sol = (0.0, 0, 0)
    max_B = max(L // l2, M // m2)