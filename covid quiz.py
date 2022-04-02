from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("700x700")
root.title("Covid Quiz")
root.config(background = "")

q1_input = StringVar(value = "0")
q1Label = Label(root, text="1. Is Covid 19 deadly?")
q1radioY = Radiobutton(root, text="yes", variable=q1_input, value="yes")
q1radioN = Radiobutton(root, text="no", variable=q1_input, value="no")
q1Label.place(relx=0.5, rely=0.5, anchor=CENTER)
q1radioY.place(relx=0.5, rely=0.1, anchor=CENTER)
q1radioN.place(relx=0.5, rely=0.15, anchor=CENTER)

q2_input = StringVar(value = "0")
q2Label = Label(root, text="2. Is Covid 19 a heart condition?")
q2radioY = Radiobutton(root, text="yes", variable=q2_input, value="yes")
q2radioN = Radiobutton(root, text="no", variable=q2_input, value="no")
q2Label.place(relx=0.5, rely=0.2, anchor=CENTER)
q2radioY.place(relx=0.5, rely=0.25, anchor=CENTER)
q2radioN.place(relx=0.5, rely=0.3, anchor=CENTER)

q3_input = StringVar(value = "0")
q3Label = Label(root, text="3. Did Covid 19 start in Brazil?")
q3radioY = Radiobutton(root, text="yes", variable=q3_input, value="yes")
q3radioN = Radiobutton(root, text="no", variable=q3_input, value="no")
q3Label.place(relx=0.5, rely=0.35, anchor=CENTER)
q3radioY.place(relx=0.5, rely=0.4, anchor=CENTER)
q3radioN.place(relx=0.5, rely=0.45, anchor=CENTER)

q4_input = StringVar(value = "0")
q4Label = Label(root, text="4. Does the vaccine contain Covid 19?")
q4radioY = Radiobutton(root, text="yes", variable=q4_input, value="yes")
q4radioN = Radiobutton(root, text="no", variable=q4_input, value="no")
q4Label.place(relx=0.5, rely=0.5, anchor=CENTER)
q4radioY.place(relx=0.5, rely=0.55, anchor=CENTER)
q4radioN.place(relx=0.5, rely=0.6, anchor=CENTER)

q5_input = StringVar(value = "0")
q5Label = Label(root, text="5. Does it take up to 14 days to see symptoms of Covid 19?")
q5radioY = Radiobutton(root, text="yes", variable=q5_input, value="yes")
q5radioN = Radiobutton(root, text="no", variable=q5_input, value="no")
q5Label.place(relx=0.5, rely=0.65, anchor=CENTER)
q5radioY.place(relx=0.5, rely=0.7, anchor=CENTER)
q5radioN.place(relx=0.5, rely=0.75, anchor=CENTER)

q6_input = StringVar(value = "0")
q6Label = Label(root, text="6. Will Covid 19 end the world?")
q6radioY = Radiobutton(root, text="yes", variable=q6_input, value="yes")
q6radioN = Radiobutton(root, text="no", variable=q6_input, value="no")
q6Label.place(relx=0.5, rely=0.8, anchor=CENTER)
q6radioY.place(relx=0.5, rely=0.85, anchor=CENTER)
q6radioN.place(relx=0.5, rely=0.9, anchor=CENTER)

score_label = Label(root, text="Score : 0")
score_label.place(relx=0.05, rely=0.05, anchor=CENTER)

def teachercheck():
    score = 0
    if q1_input.get() == "yes":
        score = score + 1
        score_label['text'] = "Score : " + str(score)
    if q2_input.get() == "no":
        score = score + 1
        score_label['text'] = "Score : " + str(score)
    if q3_input.get() == "no":
        score = score + 1
        score_label['text'] = "Score : " + str(score)
    if q4_input.get() == "no":
        score = score + 1
        score_label['text'] = "Score : " + str(score)
    if q5_input.get() == "yes":
        score = score + 1
        score_label['text'] = "Score : " + str(score)
    if q1_input.get() == "yes":
        score = score + 1
        score_label['text'] = "Score : " + str(score)
    
    if score < 3:
        messagebox.showinfo("Score", "Your chances of survival are 30%.")
    if score >= 3 and score <=5:
        messagebox.showinfo("Score", "Your chances of survival are 60%.")
    if score == 6:
        messagebox.showinfo("Score", "Your chances of survival are 90%.")


btn = Button(root, text="check", command=teachercheck)
btn.place(relx=0.5, rely=1, anchor=CENTER)

root.mainloop()