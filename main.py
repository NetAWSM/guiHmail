import tkinter as tk
from configFnkaud import host, user, password, db_name
from configFcaud import hostF, userF, passwordF, db_nameF
import psycopg2


def hmailServ():
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
    mail = name.get()
    try:
        # Функция для fnkaud
        if(len(mail) == 0):
            return
        cursorFnkaud = connectionFnkaud.cursor()
        cursorFcaud = connectionFcaud.cursor()
        postgres_insert_query = """ INSERT INTO hm_rule_criterias (criteriaruleid, criteriausepredefined, criteriapredefinedfield, criteriaheadername, criteriamatchtype, criteriamatchvalue) VALUES (%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (4, 1, 2, ' ', 2, mail)
        cursorFnkaud.execute(postgres_insert_query, record_to_insert)
        cursorFcaud.execute(postgres_insert_query, record_to_insert)
        print ("Ящик " + mail + " заблокирован на отправку.")
    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", -ex)
    connectionFnkaud.close()
    connectionFcaud.close()      


win = tk.Tk()
win.geometry("600x200")
win.title('hmail')

name = tk.Entry(win)
name.grid(row=1, column=3)

btn1 = tk.Button(win, text="Отправить", command=hmailServ)
btn1.grid(row=2, column=3)

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)


if __name__ == "__main__":
    win.mainloop()
    #cursor.close()
    print("[INFO] PostgreSQL connection closed")
