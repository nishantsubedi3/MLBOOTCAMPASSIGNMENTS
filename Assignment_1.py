#ASSIGNMENT SUBMITTED BY NISHANT SUBEDI (nishantsubedi.079@kathford.edu.np)

height = float(input("Enter your height (in meters): "))
weight = float(input("Enter your weight (in kilograms): "))
if height <= 0:
    print("Error the value for height can not be less than or equal to zero")
elif weight <= 0:
    print("Error the value for weight can not be less than or equal to zero")
else:
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        print("Underweight")
    elif bmi >= 18.5 and bmi < 25:
        print("Normal Weight")
    elif bmi >= 25 and bmi < 30:
        print("Overweight")
    else:
        print("Obesity")