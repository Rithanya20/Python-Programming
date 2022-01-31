row, col = map(int, input().split(" "))
m= []
zr = []
zc = []
for i in range(row):
    r = list(map(int,input().split()))
    m.append(r)
for i in range(0,row):
    for j in range(0,col):
        if(m[i][j] == 0):
            zr.append(i)
            zc.append(j)

for i in zr:
    for j in range(0,col):
        m[i][j] = 0
for j in zc:
    for i in range(0,row):
        m[i][j] = 0

        
for i in range(0,row):
    for j in range(0,col):
        print(m[i][j], end=" ")
    print()
4 4
4 2 0 6
3 2 9 7
1 9 2 0
3 6 1 4
Answer--
0 0 0 0 
3 2 0 0 
0 0 0 0 
3 6 0 0 

    

    
