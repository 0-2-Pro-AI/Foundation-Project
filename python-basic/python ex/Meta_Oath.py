import tkinter as tk

def click_the_button():
    label.config(text="Metaverse Next Evolution!🚀", fg="red")

window = tk.Tk()
window.title("Mission Reminder")
window.geometry("400x300")

label = tk.Label(window, text="Hi buddy, let click the f*k button", font=("Arial",14))
label.pack(pady=50)

button = tk.Button(window, text="MOVE YOUR ASS, CONSISTENT BAE", font=("Arial",12), bg="blue", fg="white", command=click_the_button)
button.pack()

window.mainloop()