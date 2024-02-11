def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(string):
    # All vanity plates must start with at least two letters.
    if not string[:2].isalpha(): # result is False
      return False

    # Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if not 2 <= len(string) <=6:
      return False

    # Numbers cannot be used in the middle of a plate; they must come at the end.
    # For example, AAA222 would be an acceptable vanity plate; AAA22A would not be acceptable.
    # The first number used cannot be a '0'.
    if len(string) > 2:
      if string[2:].isdigit():
        if string[2] != "0":
          return True
        else:
          return False
      elif string[2].isdigit() and not string[-2:].isalpha():
        return False

    # No periods, spaces, or punctuation marks are allowed.
    bad_chars = [" ", ".", '"', "(", ")", "/", "'", ";", ":", "!", "?"]
    for char in string:
      if char in bad_chars:
        return False

    # Passed all tests...Return True
    return True
main()
