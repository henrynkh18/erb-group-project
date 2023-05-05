def bmi_cal (height, weight):
    height /= 100
    bmi = round(weight / (height ** 2), 1)   

    # if bmi < 18.5:
    #     result = "Underweight"
    # elif bmi <= 25:
    #     result = "Normal"
    # elif bmi <= 30:
    #     result = "Slighty overweight"
    # elif bmi <= 35:
    #     result = "Obese!"
    # else:
    #     result = "Clinically obese!"

    return bmi
