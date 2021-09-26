from tkinter import *
from tkinter import messagebox
import database

window= Tk()
window.title("Bookstore")
window.geometry("350x400")

def selected_row(event):
    global selected_values
    index= List.curselection()[0] #through this we will get id of the selected row
    selected_values= List.get(index)
    entTitle.delete(0, END)
    entTitle.insert(END, selected_values[1])
    entAuthor.delete(0, END)
    entAuthor.insert(END, selected_values[2])
    entYear.delete(0, END)
    entYear.insert(END, selected_values[3])
    entISBN.delete(0, END)
    entISBN.insert(END, selected_values[4])

def view_command():
    List.delete(0, END)
    for data in database.viewAll():
        List.insert(END, data)

def add_command():
    List.delete(0, END)
    database.addRecord(Titleval.get(), Authorval.get(), Yearval.get(), ISBNval.get())
    List.insert(END, (Titleval.get(), Authorval.get(), Yearval.get(), ISBNval.get()))
    messagebox.showinfo("Add", "One Record Added Successfully")

def search_command():
    List.delete(0, END)
    for data in database.searchRecord(Titleval.get(), Authorval.get(), Yearval.get(), ISBNval.get()):
        List.insert(END, data)

def delete_command():
    database.deleteRecord(selected_values[0])
    view_command()
    entTitle.delete(0, END)
    entYear.delete(0, END)
    entYear.insert(END, 0)
    entAuthor.delete(0, END)
    entISBN.delete(0, END)
    entISBN.insert(END, 0)
    messagebox.showinfo("Delete", "One Record Deleted")

def update_command():
    database.updateRecord(selected_values[0], Titleval.get(), Authorval.get(), Yearval.get(), ISBNval.get())
    messagebox.showinfo("Update", "One Record Updated")
    List.delete(0, END)
    List.insert(END, (Titleval.get(), Authorval.get(), Yearval.get(), ISBNval.get()))

labelFont= ('Arial', 16, 'bold', 'underline')
label= Label(window, text= "My Book Store", font= labelFont)
label.place(x= 90, y= 5)

ExitButtonFont= ('Arial', 10, 'bold')
ExitButton= Button(window, text= "Exit", font= ExitButtonFont, command= sys.exit)
ExitButton.place(x= 300, y=5)

BookName= Label(window, text= "Book Name")
BookName.place(x= 20, y= 50)

Titleval= StringVar()
entTitle= Entry(window, width= 25, textvariable= Titleval)
entTitle.place(x= 120, y= 50)

AuthorName= Label(window, text= "Author Name")
AuthorName.place(x= 20, y= 80)

Authorval= StringVar()
entAuthor= Entry(window, width= 25, textvariable= Authorval)
entAuthor.place(x= 120, y= 80)

YearLabel= Label(window, text= "Year")
YearLabel.place(x= 20, y= 110)

Yearval= IntVar()
entYear= Entry(window, width= 10, textvariable= Yearval)
entYear.place(x= 120, y= 110)

ISBNLabel= Label(window, text= "ISBN")
ISBNLabel.place(x= 20, y= 140)

ISBNval= IntVar()
entISBN= Entry(window, width= 25, textvariable= ISBNval)
entISBN.place(x= 120, y= 140)

line= "_"*55
LineLabel= Label(window, text= line)
LineLabel.place(x= 25, y= 160)

AddButton= Button(window, text= "Add", font= ('', 10, 'bold'), command= add_command)
AddButton.place(x= 25, y= 180)

UpdateButton= Button(window, text= "Update", font= ('', 10, 'bold'), command= update_command)
UpdateButton.place(x= 65, y= 180)

DeleteButton= Button(window, text= "Delete", font= ('', 10, 'bold'), command= delete_command)
DeleteButton.place(x= 125, y= 180)

SearchButton= Button(window, text= "Search", font= ('', 10, 'bold'), command= search_command)
SearchButton.place(x= 180, y= 180)

ViewButton= Button(window, text= "View All", font= ('', 10, 'bold'), command= view_command)
ViewButton.place(x= 240, y= 180)

List= Listbox(window, width= 45)
List.place(x= 30, y= 210)

Scroll= Scrollbar(window)
Scroll.place(x= 280, y= 240)

List.configure(yscrollcommand= Scroll.set)
Scroll.configure(command= List.yview)

List.bind('<<ListboxSelect>>', selected_row)
List.bind()

window.mainloop()