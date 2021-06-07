from collections import deque
m, n = map(int, input().split())
data = []
for _ in range(m):
    data.append(list(input()))
 
def find_volume(i, j):
    dq = deque() #When ever it runs creates empty deque
    dq.append((i, j))
 
    res = 0
 
    while(dq):
        x, y = dq.pop()
        if x < 0 or y < 0 or x >= m or y >= n:
            res += float('inf')
        elif data[x][y] != '*':
            data[x][y] = '*'
            dq.append((x,y+1))
            dq.append((x,y-1))
            dq.append((x+1,y))
            dq.append((x-1,y))
            res += 1
    
    return res if res != float('inf') else 0
 
total_volume = 0
 
for i in range(m):
    for j in range(n):
        if(data[i][j] == '*'): continue  #if this executes the respective index will not go to below function 
        curr_volume = find_volume(i,j)
        total_volume += curr_volume
 
print(total_volume)
"""
4 4
.**.
*.*.
*..*
****
"""
