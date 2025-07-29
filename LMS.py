from tkinter import *
from tkinter import simpledialog, messagebox

root = Tk()
root.title("Library Management System")

books = []

book_listbox = Listbox(root, font=('',15,''), width=40)
book_listbox.pack(pady=10)

def show_books():
    book_listbox.delete(0, END)
    if books:
        for book in books:
            book_listbox.insert(END, book)
    else:
        book_listbox.insert(END, "The collection is empty")

def add_books():
    name = simpledialog.askstring("Add book", "Enter book name: ")
    if name:
        books.append(name)
        show_books()

def del_book():
    select = book_listbox.curselection()
    if select:
        index = select[0]
        books.pop(index)
        show_books()
    else:
        messagebox.showinfo("Info", "Select a book")

add_btn = Button(root, text="Add Book", command=add_books)
add_btn.pack(pady=5)

del_btn = Button(root, text="Delete book", command=del_book)
del_btn.pack(pady=5)

show_books()


root.mainloop()