import tkinter

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

#button&outputlabel

def calculate():
    try:
        global bmi
        weight = float(entry1.get())
        height = float(entry2.get())
        m = float(entry2.get())/100
        bmi = weight / (m * m)
        outputlabel.config(text=f"BMI: {bmi:.2f}")
    except ValueError:
        outputlabel.config(text="Enter a valid value")

calculate_button = tkinter.Button(screen, text="Calculate",command=calculate)
calculate_button.place(x=150-30, y=150.5+26)

outputlabel = tkinter.Label(screen, text="")
outputlabel.pack(side="bottom")

screen.mainloop()