import random

while True:

  print("Welcome to Rock Paper Scissors!")
  print("------------------------------")

  Rock = "R"
  Paper = "P"
  Scissors = "S"

  print("R stands for Rock")
  print("P stands for Paper")
  print("S stands for Scissors")

  hands = ["Rock", "Paper", "Scissors"]

  player = input("\nPick a hand. R, P, S: ")
  if(player == "R" or player == "P" or player == "S"): 
    computer = random.choice(hands)

  

    def checkWinner (player, computer):
          if(player == "R" and computer == "Paper"):
            print("Sorry, you lost.")
          
          elif(player == "R" and computer == "Scissors"):
            print("Congrats! Rock smashes scissors! You have won :)")
          
          elif(player == "S" and computer == "Paper"):
            print("Congrats! Scissors cuts paper! You win :)")
          
          elif(player == "S" and computer == "Rock"):
            print("Sorry, you lost!")
          
          elif(player == "P" and computer == "Rock"):
            print("Congrats! Paper covers rock! You win :)")
          
          elif(player == "P" and computer == "Scissors"):
            print("Sorry, you lost!")
          
          else:
            print("It's a tie, play again!")
          
    print(f"player({player}) : CPU ({computer}).")
    
    result = checkWinner(player, computer)

  else:
        print("Invalid input. Try again.")
    
  break

print("Thanks for playing. :)")