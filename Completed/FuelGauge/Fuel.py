def main():
  result = get_gauge("Fraction: ")
  print(result)

def get_gauge(prompt):
  while True:
    try:
      value = input(prompt).split('/')
      x = int(value[0])
      y = int(value[1])
      result = (x/y)
    except (ZeroDivisionError, ValueError):
      continue
    else:
      if x>y:
        continue
      elif result >= .99:
        return "F"
      elif result <= .01:
        return "E"
      else:
        return '{:.0%}'.format(result)

main()
