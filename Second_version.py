import pulp


def solve_with_pulp(p, l, m, L, M):
    p1, p2, p3 = p
    l1, l2, l3 = l
    m1, m2, m3 = m

    prob = pulp.LpProblem("Max_Profit_Problem", pulp.LpMaximize)

    x1 = pulp.LpVariable("x1", lowBound=0, cat="Continuous")
    x2 = pulp.LpVariable("x2", lowBound=0, cat="Integer")
    x3 = pulp.LpVariable("x3", lowBound=0, cat="Integer")

    prob += p1 * x1 + p2 * x2 + p3 * x3, "Total_Profit"

    prob += l1 * x1 + l2 * x2 + l3 * x3 <= L, "time"
    prob += m1 * x1 + m2 * x2 + m3 * x3 <= M, "material"
    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    status = pulp.LpStatus[prob.status]
    if status != "Optimal":
        print("توجه: وضعیت حل بهینه نیست! وضعیت فعلی:", status)

    # استخراج جواب‌ها
    x1_opt = pulp.value(x1)
    x2_opt = int(pulp.value(x2))
    x3_opt = int(pulp.value(x3))
    best_profit = pulp.value(prob.objective)

    return (x1_opt, x2_opt, x3_opt), best_profit


def print_result(best_sol, best_profit):
    x1_opt, x2_opt, x3_opt = best_sol
    print(f"x1: {x1_opt:.6f}, x2: {x2_opt}, x3: {x3_opt}")
    print(f"Total Profit = {best_profit:.6f}")


if __name__ == "__main__":
    # خواندن ورودی از استاندارد
    p = list(map(int, input().split()))  # p1 p2 p3
    l = list(map(int, input().split()))  # l1 l2 l3
    m = list(map(int, input().split()))  # m1 m2 m3
    L, M = map(int, input().split())  # L M (کل منابع)

    best_sol, best_profit = solve_with_pulp(p, l, m, L, M)
    print_result(best_sol, best_profit)
