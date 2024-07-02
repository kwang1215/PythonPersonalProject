import random

choices = ["가위", "바위", "보"]
game_score = {
    "win" : 0,
    "loss" : 0,
    "draw" : 0
}

while True:
    computer_choice = random.choice(choices)
    player_choice = input("가위, 바위, 보 중 하나를 입력하세요. ")

    if player_choice != "가위" and player_choice != "바위" and player_choice != "보" :
        print("유효한 입력이 아닙니다.")
        continue
    else:
        print(f'사용자 : {player_choice}, 컴퓨터 : {computer_choice}')

        # 무승부
        if player_choice == computer_choice:
            print("무승부 입니다.")
            game_score["draw"] += 1

        # 사용자가 승리했을 경우
        elif player_choice == "가위" and computer_choice == "보" :
            print("사용자 승리!")
            game_score["win"] += 1
        elif player_choice == "바위" and computer_choice == "가위" :
            print("사용자 승리!")
            game_score["win"] += 1
        elif player_choice == "보" and computer_choice == "바위":
            print("사용자 승리!")
            game_score["win"] += 1

        # 컴퓨터가 승리했을 경우
        elif computer_choice == "가위" and player_choice == "보":
            print("컴퓨터 승리!")
            game_score["loss"] += 1
        elif computer_choice == "바위" and player_choice == "가위":
            print("컴퓨터 승리!")
            game_score["loss"] += 1
        elif computer_choice == "보" and player_choice == "바위":
            print("컴퓨터 승리!")
            game_score["loss"] += 1

        # 게임 더 할건지 물어보기
        while True:
            game_continue = input('한번더 하시겠습니까? (Y/N)')
            if game_continue.lower() == "y":
                break
            elif game_continue.lower() == "n":
                print(f'승: {game_score["win"]} 패: {game_score["loss"]} 무승부: {game_score["draw"]}')
                exit()
            else:
                print("Y/N로만 작성해주세요.")

