import sys
import random
from pyfiglet import Figlet
# figlet syntax( pyfiglet.figlet_format([imported string] , font = [desired font, default is used if not specified.]) )
figlet = Figlet()
fonts = figlet.getFonts()

# if no arguments added(python figlet.py) - the outcome will be a random font.
if len(sys.argv) == 1: #ex. python figlet.py
    rndm_font = random.choice(fonts)
    figlet.setFont(font= rndm_font)

# If the user wants a specific font, the user
# will need to specify the type of font that
# will be used
elif len(sys.argv) == 3: #ex. python figlet.py -f/--font [font name]
    arguments = sys.argv[1:]
    font_caller = arguments[0]
    desired_font = arguments[1]
    if font_caller == '-f' or font_caller == "--font": # check if first argument matches '-f' or '--font'
        if desired_font in fonts: # check if entered font is in the getFonts list.
           figlet.setFont(font = desired_font)
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

# Prompt for the users input that will be used in
# changing the font in the output.
user_prompt = input("Input: ")
print(f"Output: {figlet.renderText(user_prompt)}")
