num = int(input("Enter a number: "))
num_str = str(num)
nlist = []
num2 = 0
x = True
while x:
    for i in range(len(num_str)):
        nlist.append(num_str[i])
                
    for d in range(len(nlist)):
        num2 += int(nlist[d])
    if len(str(num2)) == 1:
        x = False
    else:
        continue
    print(num2, nlist, num_str)