import psycopg2
from config import host, user, password, db_name
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