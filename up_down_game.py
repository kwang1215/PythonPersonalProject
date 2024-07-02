import random

computer_number = random.randint(1, 100)
max = 9999
count = 0

while True:
    # print(computer_number)

    try:
        player_number = int(input('1~100까지 숫자를 입력하세요.'))
    except ValueError:
        print("문자가 감지되었습니다. 올바른 번호를 입력하세요.")
        player_number = int(input('1~100까지 숫자를 입력하세요.'))

    if player_number > 100 or player_number < 1:
        print("1~100까지 숫자를 입력해야 합니다. 올바른 번호를 입력하세요.")
        continue
    else:
        if player_number > computer_number:
            print('down')
            count += 1
        elif player_number < computer_number:
            print('up')
            count += 1
        else:
            count += 1
            print("정답입니다.")
            print(f'정답까지 시도한 횟수 : {count}')
            print(f'지금까지 가장 적게 시도한 횟수 : {max}')
            if count < max:
                max = count
            while True :
                game_continue = input('게임을 한번더 하시겠습니까? (Y/N)')
                if game_continue == 'y' or game_continue == 'Y':
                    computer_number = random.randint(1, 100)
                    count = 0
                    break
                elif game_continue == 'n' or game_continue == 'N':
                    print('게임이 종료 되었습니다.')
                    exit()
                else :
                    print("Y/N로만 작성해주세요.")