import tkinter as tk
import psycopg2
from config import host, user, password, db_name
import time



#Коннект к базе
connection = psycopg2.connect(
host=host,
user=user,
password=password,
database=db_name
)
connection.autocommit = True

def hmailServ():
    mail = name.get()
    try:
        if(mail == "exit"):
            return
        elif(len(mail) == 0):
            return
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO hm_rule_criterias (criteriaruleid, criteriausepredefined, criteriapredefinedfield, criteriaheadername, criteriamatchtype, criteriamatchvalue) VALUES (%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (1, 1, 2, ' ', 1, mail)
        cursor.execute(postgres_insert_query, record_to_insert)
        print ("Почта занесена в правило")
    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", -ex)
    finally:
        if connection:
            connection.close()
            #cursor.close()
            print("[INFO] PostgreSQL connection closed")


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