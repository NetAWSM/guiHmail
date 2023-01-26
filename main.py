import tkinter as tk
from configFnkaud import host, user, password, db_name
from configFcaud import hostF, userF, passwordF, db_nameF
import psycopg2


def mailBox():
    #Коннект к базе fnkaud
    connectionFnkaud = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
    )
    connectionFnkaud.autocommit = True

    #Коннект к базе fcaud
    connectionFcaud = psycopg2.connect(
    host=hostF,
    user=userF,
    password=passwordF,
    database=db_nameF
    )
    connectionFcaud.autocommit = True
    mail = mail_box.get()
    try:
        if(len(mail) == 0):
            return
        cursorFnkaud = connectionFnkaud.cursor()
        cursorFcaud = connectionFcaud.cursor()
        postgres_insert_query = """ INSERT INTO hm_rule_criterias (criteriaruleid, criteriausepredefined, criteriapredefinedfield, criteriaheadername, criteriamatchtype, criteriamatchvalue) VALUES (%s,%s,%s,%s,%s,%s)"""
        record_to_insert_FNKAUD = (1, 1, 2, ' ', 2, mail)
        record_to_insert_FCAUD = (4, 1, 2, ' ', 2, mail)
        cursorFnkaud.execute(postgres_insert_query, record_to_insert_FNKAUD)
        cursorFcaud.execute(postgres_insert_query, record_to_insert_FCAUD)
        # print ("Ящик " + mail + " заблокирован на отправку.")
        inf = tk.Label(win, text = "Ящик " + mail + " заблокирован на отправку.")
        inf.grid(row=6, column=1)
    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", -ex)
    connectionFnkaud.close()
    connectionFcaud.close()      

def Domain():
    #Коннект к базе fnkaud
    connectionFnkaud = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
    )
    connectionFnkaud.autocommit = True

    #Коннект к базе fcaud
    connectionFcaud = psycopg2.connect(
    host=hostF,
    user=userF,
    password=passwordF,
    database=db_nameF
    )
    connectionFcaud.autocommit = True
    mail = domain.get()
    try:
        if(len(mail) == 0):
            return
        cursorFnkaud = connectionFnkaud.cursor()
        cursorFcaud = connectionFcaud.cursor()
        postgres_insert_query = """ INSERT INTO hm_rule_criterias (criteriaruleid, criteriausepredefined, criteriapredefinedfield, criteriaheadername, criteriamatchtype, criteriamatchvalue) VALUES (%s,%s,%s,%s,%s,%s)"""
        record_to_insert_FNKAUD = (1, 1, 2, ' ', 1, mail)
        record_to_insert_FCAUD = (4, 1, 2, ' ', 1, mail)
        cursorFnkaud.execute(postgres_insert_query, record_to_insert_FNKAUD)
        cursorFcaud.execute(postgres_insert_query, record_to_insert_FCAUD)
        # print ("Ящик " + mail + " заблокирован на отправку.")
        inf = tk.Label(win, text = "Домен " + mail + " заблокирован на отправку.")
        inf.grid(row=6, column=3)
    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", -ex)
    connectionFnkaud.close()
    connectionFcaud.close()


win = tk.Tk()
win.geometry("600x200")
win.title('hmail')

mail_box = tk.Entry(win)
mail_box.grid(row=1, column=1)

btn1 = tk.Button(win, text="Заблокировать почтовый ящик", command=mailBox)
btn1.grid(row=2, column=1)

domain = tk.Entry(win)
domain.grid(row = 1, column = 2)

btn2 = tk.Button(win, text="Заблокировать домен", command=Domain)
btn2.grid(row=2, column=2)


# win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=300)


if __name__ == "__main__":
    win.mainloop()
    #cursor.close()
    print("[INFO] PostgreSQL connection closed")
