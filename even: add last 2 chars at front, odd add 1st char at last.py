input_str = input().split(',')
final = ""

for a in input_str:
    x,y = a.split(':')
    length = len(x);
    sum = 0;

    for i in y:
        sum += int(i)**2
    if sum%2!= 0:
         final += x[1: length]
         final += x[0]+" "
    else:
         final += x[length-2: length]
         final += x[0:length-2] + " "
    
print(final)

abcd:1234,bcdgfhf:127836
cdab cdgfhfb 
