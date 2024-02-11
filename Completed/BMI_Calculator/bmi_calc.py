
"""BMI calculator
BMI = (weight/(height**2))
Underweight = BMI < 18.5
Normal = BMI >= 18.5 and < 25 
Overweight = BMI >= 25 and <30
Obese = BMI >30"""

#input raw data of height and weight
weight = float(input("How much do you weight? (in whole pound)"))
ounces = float(input("Any ounces to your weight?"))
height = float(input("How Tall are you? (in whole feet): "))
inches = float(input("Any inches to your Height:"))

#specifing the extra information
adding_inches = inches / 12
adding_ounces = ounces / 16
new_height = height + adding_inches
new_weight = weight + adding_ounces

#convert to kg and meters
convert_to_kg = (new_weight * 0.45359237)
convert_to_meters = (new_height * 0.3048)
print("Your weight", new_weight, "lbs, is converted to ", convert_to_kg, "kg")
print("Your height", new_height, "ft, is converted to ", convert_to_meters, "m")

#Calculate the BMI 
BMI = (convert_to_kg/(convert_to_meters**2))

#if statements to see which condition the users input meets
if BMI >0:
    if BMI < 18.5:
        print("You are considered: 'Underweight'")
    elif BMI < 25:
        print("You are considered: 'Normal'")
    elif BMI < 30:
        print("You are considered: 'Overweight'")
    elif BMI >= 30:
        print("You are considered: 'Obese'")
