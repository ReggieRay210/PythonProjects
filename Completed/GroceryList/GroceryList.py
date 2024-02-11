# Create a grocery list
def main():
  print(5*"#","Enter Grocery Items",5*"#")
  grocery_list()

def grocery_list():
  item_list = []
  dict_list = {}
  while True:
    try:
      entry = input().upper()
    except EOFError: # if user inputs CTRL-D, this will stop the program
      print()
      break
    else:
      if entry == 'REMOVE':   # if the user enters "Remove", prompt user on which item to remove with the current list to choose from. 
        rm_item = input('What item would you like to remove?: ').upper()
        item_list.remove(rm_item)
      item_list.append(entry) # ask for user to enter the items and add to the list
      item_list.sort()
      for _ in item_list: # remove any blank items that could be added by mistake as well as remove the 'REMOVE'entry from the list.
        if _ == '':
          item_list.remove('') 
        elif _ == "REMOVE":
          item_list.remove("REMOVE")


  
  # count how many times did a single item appear in the list
  for item in item_list:
    if item in dict_list:
      dict_list[item] += 1
    else:
      dict_list[item] = 1

  # display the items in ALL CAPS with the amount of times that the item was in the list.
  for item, count in dict_list.items():
    print(count, item)

main()
