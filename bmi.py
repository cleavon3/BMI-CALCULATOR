print("welcome to the BMI calculator")
name = input("whats your name?")
weight = float (input("whats your weight in kg?"))
height = float(input("whats your height in m?"))
bmi = weight/(height**2) 
print( name +  "Your BMI is " + str(bmi) ) 

if bmi < 18.5:
  print("you are underweight")
elif bmi < 25:
    print("Normal weight")
else:
    print("Overweight")