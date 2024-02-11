def main():
  total = 50
  while total > 0:
    print(f'Amount Due: {total}')
    coin = int(input("Insert Coin: "))
    acceptable = [5,10,25]
    if coin in acceptable:
      total -= coin
  else:
    print(f'Change Owed: {abs(total)}')

main()
