
# Задание 4
numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
l = []
for i in range(len(numbers)):
    if numbers[i]>0:
        l.append(1)
    elif numbers[i]<0:
        l.append(-1)
    else:
        l.append(0)
print(l)




