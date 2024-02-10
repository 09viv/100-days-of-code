import random
options = ("stone","paper","scissor")
gamerunning = True
while gamerunning:
    computer = random.choice(options)
    Player = None
    while Player not in options:
        Player = input('''Namaskar Sneha!!
        Apale ya khela madhe swagat aahe.. krupaya khali dilelya
        paryayan paike ek nivda
        stone,paper,scissor: 
        ''')
        if Player not in options:
            print('''Jyada hoshiyar banane ki koi jarurat nahi hai chup chap jo options
                     diye huye hai unhi me se select karo.. ''')

    print(f"Sneha:{Player}")
    print(f"Vivek:{computer}")

    if Player == computer:
        print("Arey match Tie zali")
    elif Player == "stone" and computer == "scissor":
        print("Hurray!! Sneha tu jinkali..")
    elif Player == "paper" and computer == "stone":
        print("Hurray!! Sneha tu jinkali..")
    elif Player == "scissor" and computer == "paper":
        print("Hurray!! Sneha tu jinkali..")
    else:
        print("Arey arey tu harali..")

    again = input('''   Do you want to play again: 
            Enter yes or no: 
            ''').lower()
    if not again == "yes":
        gamerunning= False

print(''' Dhanyawad ha game khelalya baddal..
         mandal aple abhari aahe..''')