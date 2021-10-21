def main():
  import random
  rolled_dice = 2
  for i in range(0, rolled_dice):
    roll = random.randint(1,6)
    print(f'You rolled a {roll}')

if __name__== "__main__":
  main()
