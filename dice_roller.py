def main():
  import random
  rolled_dice = 2
  dice_sum = 0
  for i in range(0, rolled_dice):
    roll = random.randint(1,6)
    print(f'You rolled a {roll}')
    dice_sum += roll
  print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()
