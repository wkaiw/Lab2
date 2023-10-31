def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    # Calculate BMI
    bmi = weight / (height * height)

    if bmi < 18.5:
        classification = -1  # Underweight
    elif 18.5 <= bmi <= 25.0:
        classification = 0  # Normal Weight
    else:
        classification = 1  # Overweight

        # Return BMI and weight classification
    return bmi, classification


bmi, weight_classification = calculate_bmi(weight=57, height=1.73)

print("BMI:", bmi)

if weight_classification == -1:
    print("Underweight")
elif weight_classification == 0:
    print("Normal Weight")
else:
    print("Overweight")
