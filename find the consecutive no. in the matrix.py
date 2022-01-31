row,col = map(int, input().split(" "))
list_num = [];
M = []
for i in range(row):
    row_no= list(map(int, input().split()))
    M.append(row_no)
for i in range(0, row):
    for j in range(0, col):
        if(j < col-3):  #in rows
            if(M[i][j] == M[i][j+1] == M[i][j+2] == M[i][j+3]):
                list_num.append(M[i][j])
        if(i < row-3):  #in col
            if(M[i][j] == M[i+1][j] == M[i+2][j] == M[i+3][j]):
                list_num.append(M[i][j])
        if(j<col-3 and i>=3):   #rights to left diagonal
            if(M[i][j] == M[i-1][j+1] == M[i-2][j+2] == M[i-3][j+3]):
                list_num.append(M[i][j])
        if(j >= 3 and i >= 3):       #left to right diagonals 
            if(M[i][j] == M[i-1][j-1] == M[i-2][j-2] == M[i-3][j-3]):
                list_num.append(M[i][j])
if(len(list_num) == 0):
    print("-1")
else:
    print(min(list_num))
    
6 6
1 3 3 3 3 9
1 6 9 2 3 9
1 2 2 5 4 9
2 2 4 5 7 9
2 4 5 6 7 2
1 2 3 4 5 6
2
