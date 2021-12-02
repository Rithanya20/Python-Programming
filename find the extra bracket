string = input()
n = len(string)
stack = []
count =0
for a in string:
    if(a == '['or a == '{'or a == '('):
        stack.append(a)
        count+=1
        continue
    if(len(stack)==0):
        print(count+1)
        exit()
    b = stack.pop()
    if(a==']' and b=='['):
        count+=1
    elif(a=='}' and b=='{'):
        count+=1
    elif(a==')' and b=='('):
        count+=1
if(len(stack)==0):
    print(0)
else:
    print(count+1)
    
   #[]{}]
   #5
    
    
