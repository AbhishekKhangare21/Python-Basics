height = float(input())
weight = int(input())

bmi = weight / (height * height)
if bmi < 18.5:
    print("Your BMI is {bmi}, you are underwieght.")
elif bmi < 25:
    print("Your BMI is {bmi}, you have a normal weight.")
elif bmi < 35:
    print ("Your BMI is {bmi}, you are obese.")
else:
    print("Your BMI is {bmi}, you are clinically obese.")