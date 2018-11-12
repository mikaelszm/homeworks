s = input()
total=0

for x in range(len(s)):
    if ((x %2) !=0):
        if int(s[x])*2>9:
            total+= int(s[x])*2%10+int(int(s[x])*2/10)
        else:
            total+=int(s[x])*2
    else:
        total+=int(s[x])
    

print(total)
if total%10 ==0:
    print("Your number ID is okay!")
