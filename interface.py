from tkinter import *
from DB_controller import *

path = './DB_PASS.sqlite'

try:
    open(path)
except:
    create_bd(False, path)


connect = create_connection(path)

def window_deleted():
    print(u'Окно закрыто')
    root.quit() # явное указание на выход из программы

def clear():
    list_site.delete(0,END)
    list_login.delete(0,END)
    list_pass.delete(0,END)

def renderListbox():
    list1 = execute_read_query(connect, "SELECT site, login, pass from main")
    
    for i in list1:
        list_site.insert(END, i[0])
        list_login.insert(END, i[1])
        list_pass.insert(END, i[2])

def add_entry():
    site = v_site.get()
    login = v_login.get()
    passw = v_passw.get()

    v_site.set('')
    v_login.set('')
    v_passw.set('')

    if login != '' or passw != '':
        execute_query(connect, create_main_entry.format(site, login, passw))
        clear()
        renderListbox()

root=Tk()
root.title(u'Пример приложения')

root.geometry('650x250')
root.protocol('WM_DELETE_WINDOW', window_deleted)

v_site, v_login, v_passw = StringVar(),StringVar(),StringVar()

list_site= Listbox(root)
list_login= Listbox(root)
list_pass = Listbox(root)

renderListbox()

column_1 = Label(root, text='Site').grid(column=0,row=0)
column_2 = Label(root, text='Login').grid(column=1,row=0)
column_3 = Label(root, text='Pass').grid(column=2,row=0)

list_site.grid(column=0,row=1)
list_login.grid(column=1,row=1)
list_pass.grid(column=2,row=1)

input_site = Entry(root, textvariable=v_site).grid(column=0,row=2)
input_login = Entry(root, textvariable=v_login).grid(column=1,row=2)
input_passw = Entry(root, textvariable=v_passw).grid(column=2,row=2)
enter = Button(root, text='add', command=add_entry).grid(column=3,row=2)

root.resizable(False, False) # размер окна может быть изменён только по горизонтали
root.mainloop()