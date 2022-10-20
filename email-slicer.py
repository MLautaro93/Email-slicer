import tkinter as tk

# Create the window
root = tk.Tk()
root.geometry('768x512')
root.resizable(False, False)
root.config(bg = 'brown')
root.title('Email Slicer')

# Adding the labels
greeting = tk.Label(text = 'Welcome to Email Slicer', font = 'helvetica 15 bold', fg = 'white', bg = 'black')
info = tk.Label(text = 'Please, enter your Email and click the done button.\nThe program will extract your username and domain name.', font = 'helvetica 10', fg = 'white', bg = 'brown')
entry_label = tk.Label(text = 'Enter your Email:', font = 'helvetica 10', fg = 'white', bg = 'black')
result_label = tk.Label(text = 'Result:', font = 'helvetica 10', fg = 'white', bg = 'black')

greeting.place(relx = .5, y = 50, anchor = tk.CENTER)
info.place(relx = .5, y = 100, anchor = tk.CENTER)
entry_label.place(relx = .5, y = 175, anchor = tk.CENTER)
result_label.place(relx = .5, y = 350, anchor = tk.CENTER)

# The entry box
entry = tk.StringVar()
entry_box = tk.Entry(font = 'helvetica 10', width = 50, justify = 'center', textvariable = entry)
entry_box.place(relx = .5, y = 225, anchor = tk.CENTER)



# The esult box
result_box = tk.Text(height = 5, width = 50, font = 'helvetica 10')
result_box.place(relx = .5, y = 425, anchor = tk.CENTER)

# The functions
def result():
    try:
        email = entry_box.get()
        email = email.strip()
        username = email[:email.index('@')]
        domain = email[email.index('@') + 1:]
        result_box.delete(1.0, tk.END)
        message = f'Email entered was: {email}\nYour username is {username}\nAnd your domain server is {domain}'
        result_box.insert(tk.END, message)
    except:
        result_box.delete(1.0, tk.END)
        result_box.insert(tk.END, 'Please, enter a valid email ID.')

def reset():
    entry_box.delete(0, 'end')
    result_box.delete(1.0, tk.END)

# The buttons
done_button = tk.Button(text = 'Done', font='helvetica 10 bold', command = result)
reset_button = tk.Button(text = 'Reset', font='helvetica 10 bold', command = reset)

done_button.place(x = 325, y = 275, anchor = tk.CENTER)
reset_button.place(x = 440, y = 275, anchor = tk.CENTER)

root.mainloop()