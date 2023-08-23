def BMI(w,h):
    bmi = w / (h*h)
    if(bmi>0):
        if(bmi<18.5):
            print("Underweight")
        elif(bmi<25):
            print("Normal")
        elif(bmi<30):
            print("Overweight")
        else:
            print("Obese")
    else:
        print("Invalid input")

if __name__ == "__main__":
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in m: "))
    BMI(weight,height)