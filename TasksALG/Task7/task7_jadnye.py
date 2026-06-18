n = int(input())
price = [0] + [int(input()) for _ in range(n)]

# dp[day][coupons] = минимальная стоимость первых day дней,
# если после day-го дня осталось coupons купонов
dp = [[10**9] * (n + 2) for _ in range(n + 1)]
parent = [[None] * (n + 2) for _ in range(n + 1)] # (предыдущее количество купонов, использовали ли купон в этот день)
dp[0][0] = 0  # До начала обедов стоимость 0 и купонов нет

for day in range(1, n + 1):
    cost = price[day]
    for coupons in range(n + 1):
        # Платим за обед деньгами и получаем купон
        if cost > 500 and coupons > 0:
                candidate = dp[day-1][coupons-1] + cost
                if candidate < dp[day][coupons]:
                    dp[day][coupons], parent[day][coupons] = (candidate, (coupons - 1, False))
        # Платим за обед деньгами без получения купона
        else:
            candidate = dp[day-1][coupons] + cost
            if candidate < dp[day][coupons]:
                dp[day][coupons], parent[day][coupons] = (candidate, (coupons, False))
        # Используем купон: стоимость обеда = 0, число купонов уменьшается на 1
        if coupons < n:
            candidate = dp[day - 1][coupons + 1]
            if candidate < dp[day][coupons]:
                dp[day][coupons], parent[day][coupons] = (candidate, (coupons + 1, True))

# Ищем состояние с минимальной итоговой стоимостью
best_coupons, best_cost = 0, dp[n][0]
for coupons in range(n + 1):
    if dp[n][coupons] < best_cost:
        best_cost, best_coupons = dp[n][coupons], coupons
# Восстанавливаем дни использования купонов
days, cur = [], best_coupons
for day in range(n, 0, -1):
    prev, used_coupon = parent[day][cur]
    if used_coupon:
        days.append(day)
    cur = prev
days.reverse()
print(best_cost)
print(len(days))
if days:
    print(*days)