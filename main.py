height = float(input( "Enter your height in cm:"))
weight = float(input( "Enter your weight in kg:"))

bmi = weight / (height / 100) ** 2

print('BMI', bmi)

if bmi <= 18.5:
    print("You are underweight")
elif bmi <= 29.5:
    print("You are healthy")
elif bmi <= 29.9:
    print("You are overweight")
elif bmi <= 34.9:
    print("You are severly overweight")
elif bmi <= 39.9:
    print("You are obese")
else:
    print("You are severly obese")