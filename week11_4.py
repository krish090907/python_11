import tkinter as tk
root = tk.Tk()
root.title('FOOD MENU')
root.geometry('300x300')
meal = tk.StringVar()
rb1=tk.Radiobutton(root, text="Veg", variable=meal, value="Veg")
rb1.pack()
rb2=tk.Radiobutton(root, text="Non-Veg", variable=meal, value="Non-Veg")
rb2.pack()
v = tk.IntVar()
nv = tk.IntVar()
cb1=tk.Checkbutton(root, text="Paneer (Veg)", variable=v)
cb1.pack()
cb2=tk.Checkbutton(root, text="Chicken (Non-Veg)", variable=nv)
cb2.pack()
def show():
    if meal.get() == "Veg" and v.get() == 1:
        result = "Selected: Veg - Paneer"
    elif meal.get() == "Non-Veg" and nv.get() == 1:
        result = "Selected: Non-Veg - Chicken"
    else:
        result = "No valid selection"
    lbl.config(text=result)
btn=tk.Button(root, text="Submit", command=show)
btn.pack()
lbl = tk.Label(root)
lbl.pack()
root.mainloop()

