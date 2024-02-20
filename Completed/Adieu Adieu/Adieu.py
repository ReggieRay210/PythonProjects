from inflect import engine
p = engine()
name_list = []

while True:
    try:
        name:str = input("Name: ")
        name_list.append(name)
    except EOFError:
        print()
        break

names = p.join(tuple(name_list))
print("Adieu, adieu, to", names)
