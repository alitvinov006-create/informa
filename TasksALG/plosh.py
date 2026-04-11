import numpy as np

def simpson_rule(f, a, b, n):
    if n % 2 == 1:
        n += 1  # Делаем n четным
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    fx = f(x)

    integral = (h / 3) * (fx[0] + 4 * sum(fx[1:-1:2]) + 2 * sum(fx[2:-2:2]) + fx[-1])
    return integral

# Пример использования
f1 = lambda x: x - 2 # функ1
f2 = lambda x: -x + 4 # функ2

S1 = simpson_rule(f1, 2, 3, 2)
S2 = simpson_rule(f2, 3, 4, 2)

print(S1 + S2)
# немного изменил для удобства