print('''Welcome to Treasure Island
      Your mission is to find the treasure''')
turn = input("Select turn either left or right: ").lower()
if turn == "left":
    print("Right Move")
else:
    print('''Ohh!!! that was a wrong move..
          Game Over!!''')

decision = input("What will you do Swim or Wait: ").lower()
if decision == "wait":
    print("Right decision.. carry on!!")
else:
    print('''unfortunately you loose..
          Game Over''')
    
door = input('''Select only one door from the below options: 
             Red
             Blue
             Yellow: 
             ''').lower()
if door == "Yellow":
    print("Hurray!! You Win")
else:
    print("Great efforts but you lost the treasure")