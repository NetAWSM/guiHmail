import tkinter as tk
import psycopg2
from config import host, user, password, db_name

def hmail():
    try:
        #Коннект к базе
        connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
        )
        connection.autocommit = True
        w = True
        while(w):
            mail = input("Введите почту: ")
            if(mail == "exit"):
                break
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

btn1 = tk.Button(win, text="button", command=hmail)

btn1.pack()

win.mainloop()