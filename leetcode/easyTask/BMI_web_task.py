def input_info(func):
    height = int(input("Enter your height in centimetres: "))/ 100
    weight = float(input("Enter your weight in kilogram: "))
    def bmi_decorator(info):
        print("Start calculating your BMI")
        func(weight/(height**2), info)
    return bmi_decorator

def table_bmi(bmi_ind, info):
    print(f"Your BMI index: {"%.2f" % bmi_ind}")
    if bmi_ind < 16:
        print(info[0])
    elif 15.9 < bmi_ind < 18.5:
        print(info[1])
    elif 18.4 < bmi_ind < 25:
        print(info[2])
    elif 24.9 < bmi_ind < 30:
        print(info[3])
    elif 29.9 < bmi_ind < 35:
        print(info[4])
    elif 34.9 < bmi_ind < 40:
        print(info[5])
    elif 39.9 < bmi_ind :
        print(info[6])


info_bmi = ["Eat something or you'll be blown away by the wind!I'm serious, you're almost transparent.",
            "Add one more meal a day, you near normal weight, but not enough",
            "Nice, keep it up.",
            "Okay, still in the normal weight class, but you'd better get some exercise.",
            "Hm, you need to cut down at least one meal and less sweets and more exercise.",
            "It's bad, you need professional help with your eating and exercise schedule.",
            "I think you need a check-up, maybe there's a serious health problem."]

bmi_index = input_info(table_bmi)
bmi_index(info_bmi)
