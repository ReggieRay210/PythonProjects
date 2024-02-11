def main():
  total = get_item("Item: ")

def get_item(prompt):
  num = 0
  menu = {"Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00}

  while True:
    try:
      x = input(prompt).title()
    except EOFError:
      print()
      break
    except KeyError:
      continue
    else:
      for key in menu:
        if x == key:
          num += menu[key]

    print(f"Total: ${num:.2f}")

main()
