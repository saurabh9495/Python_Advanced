t = int(input())
for i in range(t):
    n, s = [int(x) for x in input().split()[:2]]
    arr = [int(x) for x in input().split()[:n]]
    flag, c, list = False, 0, []
    for j in range(n):
        list.append(arr[j])
        while sum(list) > s:
            list.pop(0)
            c += 1
        if sum(list) == s:
            flag = True
            break
    if flag:
        print(c+1, j+1)
    else:
        print(-1)
print()
