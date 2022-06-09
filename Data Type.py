from tkinter import *
root=Tk()
root.title("Addition")
root.geometry("600x400")
input_box = Entry(root)
input_box.pack()

def addition():
    number = 5
    get_input = input_box.get()

    
    try:
       print(number + get_input)
    
    except(TypeError):
       messagebox.showinfo("Error", "Cannot add 2 different data types: Integer and String")
        
        
button = Button(root, text= "addition", command = addition)
button.place(relx = 0.5,rely = 0.5, anchor = CENTER)
button.pack()
root.mainloop()
        
    