for _ in range(times):
    n, k , x = il()
    a = il()
    v = x ** k
    pref = a[:]
    suff = a[:]
    for i in range(1, n):
        pref[i] |= pref[i - 1]

    for i in range(1, n)[::-1]:
        suff[i - 1] |= suff[i]
    ans = 0
    mx = max(a).bit_length()  
    for i in range(n):
        if a[i].bit_length() < mx - 1: continue # 没什么用的剪枝; -1 因为可能有*3情况, wa
        cur = a[i] * v
        if i: cur|= pref[i - 1]
        if i < n - 1: cur|= suff[i + 1]
        ans = max(ans, cur)
    print(ans)
