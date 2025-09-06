import random
rock='''
       ----------
------     ------)
           (-----)
           (----)
----  ---  (---)
'''
paper='''
      --------
------'   ----)--- 
         ---------)
         --------)
         ------)
    -- ------)   
'''
scissors='''
       -------
-----'   -----)---
           -------)
         -----------)
        (-----)
     ---(---)
'''
game_images=[rock,paper,scissors]
user_choice=int(input("enter your choice:type 0 for rock,1 for paper,2 for scissors."))
if user_choice>=3 or user_choice<0:
    print("you entered invalid number,you lose.")
else:
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print("computer chose:")
    print(game_images[computer_choice])
    if computer_choice == user_choice:
        print("it is a draw.")
    elif computer_choice==0 and user_choice==2:
        print("you loose")
    elif computer_choice==2 and user_choice==0:
        print("you win")
    elif computer_choice>user_choice:
        print("you loose")
    elif user_choice>computer_choice:
        print("you win")
