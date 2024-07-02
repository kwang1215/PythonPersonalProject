import random

choices = ["가위", "바위", "보"]
game_score = {
    "win" : 0,
    "loss" : 0,
    "draw" : 0
}

while True:
    computer_choice = random.choice(choices)
    player_choice = input("가위, 바위, 보 중 하나를 입력하세요: ")

    if player_choice not in choices:
        print("유효한 입력이 아닙니다.")
        continue

    print(f'사용자: {player_choice}, 컴퓨터: {computer_choice}')

    # 무승부
    if player_choice == computer_choice:
        print("무승부 입니다.")
        game_score["draw"] += 1
    # 사용자 승리 조건
    elif (player_choice == "가위" and computer_choice == "보") or \
         (player_choice == "바위" and computer_choice == "가위") or \
         (player_choice == "보" and computer_choice == "바위"):
        print("사용자 승리!")
        game_score["win"] += 1
    # 컴퓨터 승리 조건
    else:
        print("컴퓨터 승리!")
        game_score["loss"] += 1

    # 게임 더 할건지 물어보기
    while True:
        game_continue = input('한번 더 하시겠습니까? (Y/N): ').lower()
        if game_continue == "y":
            break
        elif game_continue == "n":
            print(f'승: {game_score["win"]}, 패: {game_score["loss"]}, 무승부: {game_score["draw"]}')
            exit()
        else:
            print("Y/N로만 작성해주세요.")
