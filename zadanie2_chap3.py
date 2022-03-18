#Задание2
while True:
    text = input('text: ')
    t = text.split()
    if len(text)<6:
        print('Введите больше 6 символов')
    elif len(t)<6:
        print('Введить больше 6 слов')
    else:break
if len(t)%2!=0:
    p = len(t)//2+1
else:
    p = len(t)//2
part1 = t[:p]
part2 = t[p:]
final_list = part2+part1
print(final_list)
