import tkinter
from urllib.response import addbase

#window

screen = tkinter.Tk()
screen.minsize(300,300)
screen.title("BMI Calculator")

#text&entry

label1 = tkinter.Label(screen, text="Enter your weight (kg):")
label1.place(x=150-63, y=80+10.5)
entry1 = tkinter.Entry(screen)
entry1.place(x=150-62, y=90.5+19)
label2 = tkinter.Label(screen, text="Enter your height (cm):")
label2.place(x=150-64, y=109.5+21)
entry2 = tkinter.Entry(screen)
entry2.place(x=150-62, y=130.5+19)

#button&outputlabel&advicelabel

def calculate():
    try:
        weight = float(entry1.get())
        height_cm = float(entry2.get())
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        outputlabel.config(text=f"BMI: {bmi:.2f}")

        # BMI'ye göre tavsiye
        if bmi < 18.5:
            advicelabel.config(text="Eat more healthy foods")
        elif bmi < 25:
            advicelabel.config(text="Keep balanced diet & exercise")
        elif bmi < 30:
            advicelabel.config(text="Eat less, move more")
        elif bmi < 35:
            advicelabel.config(text="Diet + exercise, consult doctor")
        elif bmi < 40:
            advicelabel.config(text="Medical guidance needed")
        else:
            advicelabel.config(text="Intensive care")

    except ValueError:
        outputlabel.config(text="Enter a valid value")
        advicelabel.config(text="")

calculate_button = tkinter.Button(screen, text="Calculate",command=calculate)
calculate_button.place(x=150-30, y=150.5+26)

advicelabel = tkinter.Label(screen, text="")
advicelabel.pack(side="bottom")

outputlabel = tkinter.Label(screen, text="")
outputlabel.pack(side="bottom")

screen.mainloop()