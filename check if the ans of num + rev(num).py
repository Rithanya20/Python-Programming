string = int(input())
sum = 0
sum = string + int(str(string)[::-1])
rev = int(str(sum)[::-1])
if(rev == sum):
    print("palindrome")
else:
    print("not palindrome")


