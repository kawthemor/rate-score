sc = 0
rt = 0
for i in range(1,11):
    s = int(input(f'people number {i} rate? (1-5)'))
    if s in range(1,6):
        sc += rt
        rt += 1
        if i == 1:
            print(f'{i}st person rate {s} star')
        elif i == 2:
            print(f'{i}nd person rate {s} star')
        elif i == 3:
            print(f'{i}rd person rate {s} star')
        else:
            print(f'{i}th person rate {s} star')
if sc > 0:
    avr = sc/(rt*5)
if avr >= 0.8:
    st = 5
elif avr >= 0.6:
    st = 4
elif avr >= 0.4:
    st = 3
elif avr >= 0.2:
    st = 2
else :
    st = 1
print(f'average star = {avr:,.2f}')
print(f'rating = {"*"*st}')