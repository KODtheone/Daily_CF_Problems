for _ in range(times):
    n = ix()
    a = il()
    for i in range(3):
        for j in range(i):
            k = (a[i] - a[j]) / (i - j)
            vis = set()
            for idx in range(n):
                vis.add(a[idx] - idx * k)
                if len(vis) > 2:
                    break
            else:
                if len(vis) == 2:
                    py()
                    exit()
    pn()
