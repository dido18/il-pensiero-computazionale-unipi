def partizione(a):
    if (sum(a) % 2) != 0:
        return False
    
    n = len(a)
    s = sum(a)/2
    parti = []
    
    for i in range(n+1):
        parti.append([])
        for j in range(s+1):
            parti[i].append(False)

    parti[0][0] = True
    for i in range(1, n+1):
        for j in range(s+1):
            if parti[i-1][j]:
                parti[i][j] = True
            if j >= a[i-1] and parti[i-1][j-a[i-1]]:
                parti[i][j] = True
    return parti[n][s]



print(partizione([1, 2, 3]))
print(partizione([1, 2, 5]))
