def main():
  import random
  rolled_dice = int(input('How many dices would you like to roll?'))
  size_dice = int(input('How many sides are the dice?'))
  dice_sum = 0
  for i in range(0, rolled_dice):
    roll = random.randint(1,size_dice)
    if roll==1:
      print(f'You rolled a {roll} Critical fail!')
    elif roll==size_dice:
      print(f' You rolled a {roll} Critical success')
    else:
      print(f' You rolled a {roll}')
    dice_sum += roll
  print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()

  
