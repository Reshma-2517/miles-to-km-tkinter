from tkinter import *

#Create main window
root = Tk()
root.title('Miles to Kilometers conversion')
root.minsize(width=250,height=50)
root.config(pady=20)

#Taking no of miles as input from the user.
input = Entry(root,width = 10,font=('Calibri',12),bg = 'beige')
input.place(x=80,y=20)

#You can also use grid() as geometry manager pack.

miles_label = Label(root,text='Miles',font=('Calibri',12))
miles_label.place(x=180,y=20)

is_equal_to_label = Label(root,text='is equal to',font=('Calibri',12))
is_equal_to_label.place(x=15,y=60)

answer_label = Label(root,text='0',font=('Calibri',12))
answer_label.place(x=100,y=60)

km_label = Label(root,text='Km',font=('Calibri',12))
km_label.place(x=180,y=60)

#Function to convert miles to km
def miles_to_km():
    user_input = input.get()
    answer = float(user_input)*(1.6)
    result = int(round(answer,4))
    answer_label.config(text=result)

calculate_button = Button(root,width=10,text='Calculate',font=('Calibri',12),command = miles_to_km ,bg='beige')
calculate_button.place(x=80,y=100)

root.mainloop()

