import tkinter as tk
gui = tk.Tk()
gui.geometry("500x300")
gui.title("ADDER")
lbl1 = tk.Label(gui,text = "Enter num1")
lbl1.pack()
input1 = tk.Entry(gui)
input1.pack()
lbl2 = tk.Label(gui,text = "Enter num2")
lbl2.pack()
input2 = tk.Entry(gui)
input2.pack()
def displaySum():
    result = int(input1.get()) + int(input2.get())
    resultLabel.config(text = result)
computeButton = tk.Button(gui,text = "ADD",command = displaySum)
computeButton.pack()
resultLabel = tk.Label(gui,text = "Result here!!!")
resultLabel.pack()
gui.mainloop()


