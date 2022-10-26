def calculate_bmi (height ,weight):
    print("Height =" + str(height))
    print("Weight =" + str(weight))

    BMI = weight / (height * height)

    print(f"Your BMI is {BMI}")

    if BMI < 18.5:
        print("Under Weight")
    if 18.5 <= BMI <= 25:
        print("Normal Weight")
    if BMI > 25:
        print("Over Weight")

calculate_bmi(weight=57,height=1.73)