import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
userselect = input(f"lets play a game of rock, paper, scissors . Type 1 for rock 2 for paper and 3 for scissors  \n")
if userselect == (f"{1}"):
   print(f"you choose rock {rock}")
if userselect == (f"{2}"):
   print(f"you choose paper {paper}")
if userselect == (f"{3}"):
   print(f"you choose scissors {scissors}")
random_float = random.randint(1, 3)
print(random_float)
if random_float == 1:
   print(f"computer choose rock {rock}")
if random_float == 2:
   print(f"computer choose paper {paper}")
if random_float == 3:
   print(f"computer choose scissors {scissors}")
if userselect not in (f"{1}{2}{3}"):
   print("you have cheated! Computer Won")
if userselect == (f"{1}") and random_float == 2:
   print("You choose rock while computer choose paper you loose")
if random_float == 1 and userselect == (f"{2}"):
   print("You choose paper while computer choose rock you win")
if random_float == 3 and userselect == (f"{1}"):
   print("You choose paper while computer choose scissors you win")
if random_float == 1 and userselect == (f"{1}"):
   print("You choose rock while computer choose rock its a tie")
if userselect == (f"{2}") and random_float == 3:
   print("You choose paper while computer choose scissors you loose")
if random_float == 2 and userselect == (f"{3}"):
   print("You choose scissors while computer choose paper you win")
if random_float == 2 and userselect == (f"{2}"):
   print("You choose paper while computer choose paper its a tie")
if userselect == (f"{3}") and random_float == 1:
   print("You choose scissors while computer choose rock you loose")
if random_float == 3 and userselect == (f"{1}"):
   print("You choose rock while computer choose scissors you win")
if random_float == 2 and userselect == (f"{3}"):
   print("You choose scissors while computer choose paper its a win")
if random_float == 3 and userselect == (f"{3}"):
   print("You choose scissors while computer choose scissors its a win")










