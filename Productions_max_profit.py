def print_result_func(best_sol, best_profit):
    print("a:" + str(best_sol[0]) + " b:" + str(best_sol[1]) + " c:" + str(best_sol[2]))
    print("total: " + str(best_profit))


def find_upper_bound_b(l1, m1, remaining_l_b, remaining_m_b, l3, m3, p1, p3, p2):
    if l1 > 0 and m1 > 0:
        x1_case1 = min(remaining_l_b / l1, remaining_m_b / m1)
        case1 = p1 * x1_case1
    else:
        case1 = 0.0

    if l3 > 0 and m3 > 0:
        x3_case2 = min(remaining_l_b / l3, remaining_m_b / m3)
        case2 = p3 * x3_case2
    else:
        case2 = 0.0

    det = l1 * m3 - l3 * m1
    if det != 0:
        x1_case3 = (remaining_l_b * m3 - remaining_m_b * l3) / det
        x3_case3 = (-1 * remaining_l_b * m1 + remaining_m_b * l1) / det
        if x1_case3 >= 0 and x3_case3 >= 0:
            case3 = p1 * x1_case3 + p3 * x3_case3
        else:
            case3 = 0.0
    else:
        case3 = 0.0

    bound_b = p2 + max(case1, case2, case3)
    return bound_b

def solve_product(p, l, m, L, M):
    p1, p2, p3 = p
    l1, l2, l3 = l
    m1, m2, m3 = m

    best_profit = -float('inf')
    best_sol = (0.0, 0, 0)
    max_B = max(L // l2 if l2 > 0 else 0, M // m2 if m2 > 0 else 0)

    for b in range(max_B + 1):
        remaining_l_b = L - b * l2
        remaining_m_b = M - b * m2


        if remaining_l_b < 0 or remaining_m_b < 0:
            continue

        bound_b = find_upper_bound_b(l1, m1, remaining_l_b, remaining_m_b, l3, m3, p1, p3, p2)
        if bound_b <= best_profit:
            continue
        max_C = min(remaining_l_b // l3 if l3 > 0 else 0,
                    remaining_m_b // m3 if m3 > 0 else 0)


        for c in range(max_C + 1):
            rem_l = remaining_l_b - c * l3
            rem_m = remaining_m_b - c * m3
            if rem_l < 0 or rem_m < 0:
                continue

            max_possible_x1 = min(rem_l / l1, rem_m / m1) if (l1 > 0 and m1 > 0) else 0
            upper_bound = p1 * max_possible_x1 + p2 * b + p3 * c

            if upper_bound < best_profit:
                continue

            x1 = max_possible_x1
            profit = p1 * x1 + p2 * b + p3 * c

            if profit > best_profit:
                best_profit = profit
                best_sol = (x1, b, c)

    return best_sol, best_profit


p = list(map(int, input().split()))
l = list(map(int, input().split()))
m = list(map(int, input().split()))
L, M = map(int, input().split())

best_sol, best_profit = solve_product(p, l, m, L, M)
print_result_func(best_sol, best_profit)
