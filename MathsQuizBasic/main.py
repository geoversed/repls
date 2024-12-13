from random import randint

name = input("Welcome. Enter your name: ")

print("You will now be tested on 5 basic arithmetic questions.")
print("Answer to the best of your ability! Your score is tracked.")

user_score = 0
for _ in range(5):
  first_num = randint(1, 150)
  second_num = randint(1, 250)

  user_argument = int(input(f"{first_num} + {second_num} = "))
  user_is_correct = user_argument == (first_num + second_num)
  if user_is_correct:
    print("Correct answer!")
    user_score += 1
    continue
  print("Incorrect answer!")

score_prcnt = (user_score / 5) * 100
print(f"\n\nGood job {name}, your score is {user_score}/5 ({score_prcnt}%)!")