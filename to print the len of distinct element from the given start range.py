n = int(input())
lst = list(map(int,input().split(" ")))
result = sorted(lst, key = lst.count)
length = len(result)
lst2 = result[n:length]
print(len(set(lst2)))

4
1 1 1 2 2 3 3 4 5 6
3
