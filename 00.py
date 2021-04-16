import random

options = ['왼쪽','오른쪽','정면']
computer_choice = random.choice(options)
user_choice = input("어디를 수비하시겠어요?(왼쪽,오른쪽,정면)")
if computer_choice == user_choice:
    print("수비에 성공하셨습니다")
else:
    print("페널티 킥이 성공했습니다")