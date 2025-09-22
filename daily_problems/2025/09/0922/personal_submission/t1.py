import sys
from math import gcd

# sys.setrecursionlimit(5005)
input = lambda: sys.stdin.readline().rstrip()
ip = input
il = lambda: list(map(int, input().split()))
ix = lambda: il()[0]
iis = lambda: input().split()
# printt = print
# print = lambda a: printt(" ".join(map(str, a))) if isinstance(a, list) or isinstance(a, tuple) else printt(a)
pl = lambda a: print(" ".join(map(str, a)))
py = lambda: print("Yes")
pn = lambda: print("No")
mod = 998244353  # ac
mod = 10 ** 9 + 7
inf = 10 ** 19

'''
good dp
'''
n, kr, kg, kb = il()
dpr = [0] * (n + 1)
dpg = [0] * (n + 1)
dpb = [0] * (n + 1)
dpr[1] = 1
dpg[1] = 1
dpb[1] = 1
for i in range(2, n + 1):
    total = dpr[i - 1] + dpg[i - 1] + dpb[i - 1]
    dpr[i] = total
    if i > kr + 1:
        dpr[i] -= dpg[i - kr - 1] + dpb[i - kr - 1]
    elif i == kr + 1:
        dpr[i] -= 1
    dpg[i] = total
    if i > kg + 1:
        dpg[i] -= dpr[i - kg - 1] + dpb[i - kg - 1]
    elif i == kg + 1:
        dpg[i] -= 1
    dpb[i] = total
    if i > kb + 1:
        dpb[i] -= dpr[i - kb - 1] + dpg[i - kb - 1]
    elif i == kb + 1:
        dpb[i] -= 1
    dpr[i] %= mod
    dpg[i] %= mod
    dpb[i] %= mod
print((dpr[n] + dpg[n] + dpb[n]) % mod)





