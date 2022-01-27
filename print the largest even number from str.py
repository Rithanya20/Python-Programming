import re
string = input()
digits = [i for i in set(string) if i.isdigit()]
digits.sort()
digits.reverse()
num = int(''.join(digits))
if(num%2 == 0):
    print(num)
else:
    length = len(digits)
    cnt = 0
    for i in range(length-1, -1, -1):
        if int(digits[i])%2 == 0:
            a = digits[i]
            digits.remove(a)
            digits.insert(length-1,a)
            even=int(''.join(digits))
            print(even)
            break
        else:
            cnt += 1
    if(cnt == length):
        print(-1)
    
infy@37519
-1
infy4$46789231
98764312
