import tkinter as tk
def middle_position(window, width, height):
    width_window= window.winfo_screenwidth()
    height_window=window.winfo_screenwidth()

    x = int((width_window / 2) - (width / 2))
    y =int((height_window / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x}+{y}")

def content():
    frame_hello.pack_forget()
    frame_content.pack(fill="both", expand=True)

app = tk.Tk()
app.title("Meta Dream v1.0")

middle_position(app, 500,400)

frame_hello = tk.Frame(app)

lbl_caption = tk.Label(frame_hello, text="Move Your Ass, Consistent B*tch", font=("Helverica", 16))
lbl_caption.pack(pady=30)

btn_active = tk.Button(frame_hello,
                       text="VISION 🚀",
                       font=("Helvetica", 14, "bold"),
                       bg="#0078D4", fg="white", 
                       command=content)
btn_active.pack(ipadx=10, ipady=10)

frame_hello.pack(fill="both", expand=True, pady=50)

frame_content = tk.Frame(app)

lbl_oath = tk.Label(frame_content,
                    text="META NEXT EVOLUTION\n\n1. Not sleep more\n2. 3 constribuitions GitHub\n3. English",
                    font=("Helvetica", 14),
                    justify="center")
lbl_oath.pack(pady=50)

exit_button= tk.Button(frame_content, text="Excuted(EXIT)", command=app.destroy)
exit_button.pack(pady=20)

app.mainloop()