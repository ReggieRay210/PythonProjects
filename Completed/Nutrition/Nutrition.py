
def nutrition_info():
  #create a dictionary for all the fruits and the corresponding calories
  fruits_info = {'Apple': '130',
                 'Avocado': '50',
                 'Banana': '110',
                 'Cantaloupe': '50',
                 'Grapefruit': '60',
                 'Grapes': '90',
                 'Honeydew Melon': '50',
                 'Kiwifruit': '90',
                 'Lemon': '15',
                 'Lime': '20',
                 'Nectarine': '60',
                 'Orange': '80',
                 'Peach': '60',
                 'Pear': '100',
                 'Pineapple': '50',
                 'Plums': '70',
                 'Strawberries': '50',
                 'Sweet Cherries': '100',
                 'Tangerine': '50',
                 'Watermelon': '80'}

  # Prompt for user input
  item = input("Item: ").title()

  # iterate through the dictionary
  for key in fruits_info:
    if key in item: # Check if the keys in the dictionary matches the user input.
      print('Calories:',fruits_info[key]) # if so then provide the calorie value.

nutrition_info()
