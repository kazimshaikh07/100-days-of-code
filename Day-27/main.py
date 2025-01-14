import tkinter

window = tkinter.Tk()

window.title("My first tkinter program")
window.minsize(width=500,height=500)
# to add padding
window.config(padx=20,pady=20)


# Label
label = tkinter.Label(window, text="This is label", font=("Arial", 20,"bold "))
# label.pack(expand=True)
label.grid(column = 0, row = 0)


# new text
label["text"]="New text"
# or
label.config (text="New text")


# Creating button
def button_click():
    print("button got clicked")
    label.config(text="Button Got Clicked")


# button = tkinter.Button(text= "Click Me", command=button_click)
# button.pack()
# Show "Button Got Clicked" on label when the button get's clicked.
# button = tkinter.Button(text= "Click Me", command=button_click)
# button.pack()


# entry
entry = tkinter.Entry(width= 10)
entry.grid(column = 3, row = 2)

def get_text():
    text = entry.get()
    print(text)
    label.config(text=text)
button = tkinter.Button(text= "Click Me", command=get_text)
button.grid(column = 1, row = 1)


new_button = tkinter.Button(text="new button")
new_button.grid(column = 2, row = 0)

window.mainloop()