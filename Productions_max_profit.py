def print_result_func(best_sol, best_profit):
    print("a:" + str(best_sol[0]) + "b:" + str(best_sol[1]) + "c:" + str(best_sol[2]))
    print("total: "+ str(best_profit))


def solve_product(p, l, m, L, M):
    p1, p2, p3 = p
    l1, l2, l3 = l
    m1, m2, m3 = m

    best_profit = -float('inf')
    best_sol = (0.0, 0, 0)
    max_B = max(L // l2, M // m2) if (l2 > 0 and m2 > 0) else 0

    for b in range(max_B + 1):
        remaining_l = L - b * l2
        remaining_m = M - b * m2
        if remaining_l < 0 or remaining_m < 0:
            continue

        max_C = min(remaining_l // l3, remaining_m // m3) if (l3 > 0 and m3 > 0) else 0

        for c in range(max_C + 1):
            rem_l = L - c * l3
            rem_m = M - c * m3
            if rem_l < 0 or rem_m < 0:
                continue

        x1 = min(rem_l / l1, rem_m / m1)
        profit = p1*x1 + p2* b + p3*c

        if profit > best_profit or abs(profit - best_profit) < 1e-10 and (b > best_sol[1] or (b == best_sol[1] and c > best_sol[2])):
            best_profit = profit
            best_sol = (x1, b, c)

        return best_sol, best_profit



p = map(int, input().split())
l = map(int, input().split())
m = map(int, input().split())
L, M = map(int, input().split())

best_sol, best_profit = solve_product(p, l, m, L, M)
print_result_func(best_sol, best_profit)