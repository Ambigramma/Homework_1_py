bingo = int(input('Ваше число: '))
first_half = 0
second_half = 0

while bingo>0:
    if len(str(bingo))>3:
        second_half += bingo % 10
        bingo//=10
    elif len(str(bingo))<4:
        first_half +=bingo%10
        bingo//=10

if first_half  == second_half:
    print('yes')
else:
    print('no')


