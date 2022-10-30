# PYTHON 3
s = input()
m = int(input())
 
adj = [[float('inf')] * 26 for _ in range(26)]
for _ in range(m):
    x, y, cost = input().split()
    cost = int(cost)
    x = ord(x) - 97
    y = ord(y) - 97
    adj[x][y] = min(adj[x][y], cost)
    adj[y][x] = min(adj[y][x], cost)
    
for k in range(26):
    for i in range(26):
        for j in range(26):
            adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

ans = l = 0
r = len(s) - 1
while l < r:
    if s[l] != s[r]:
        x = ord(s[l]) - 97
        y = ord(s[r]) - 97
        ans += min(adj[x][y], adj[y][x])
    l += 1
    r -= 1
print(ans)
