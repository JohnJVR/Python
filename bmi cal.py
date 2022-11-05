weight = float(input("Enter your weight :"))
height = float(input("Enter you height : "))
bmi= weight/(height**2)
if bmi <= 18.5:
    print("Person is Under weight")
elif bmi <=25.0:
    print("Person is Normal")
elif bmi <= 30:
    print("Person is Over Weight")
else:
    print("Person is Obese")