import mysql.connector
import psycopg2
from psycopg2 import Error
from mysql.connector import Error
import sqlite3
import requests
import pandas as pd
import json
import csv


#
# def connect():
#     """ Connect to MySQL database """
#     conn = None
#     try:
#         conn = mysql.connector.connect(host='localhost',
#                                        database='python_mysql',
#                                        user='root',
#                                        password='1234qwerASDF_',
#                                        auth_plugin='mysql_native_password')
#         if conn.is_connected():
#             print('Connected to MySQL database')
#         cursor = conn.cursor()
#         cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#         sql = '''CREATE TABLE EMPLOYEE(
#            FIRST_NAME CHAR(20) NOT NULL,
#            LAST_NAME CHAR(20),
#            AGE INT
#         )'''
#
#         sql1 = ''' INSERT INTO EMPLOYEE VALUES("Rohan","Akhtar",22) '''
#         sql2 = ''' INSERT INTO EMPLOYEE VALUES("Usama","Bashir",23) '''
#         sql3 = ''' INSERT INTO EMPLOYEE VALUES('John','Doe',54) '''
#         sql4 = '''select * from EMPLOYEE;'''
#
#         cursor.execute(sql)
#         cursor.execute(sql1)
#         cursor.execute(sql2)
#         cursor.execute(sql3)
#         cursor.execute(sql4)
#         records = cursor.fetchall()
#         print(records)
#         conn.commit()
#         conn.close()
#         print("connection to mysql database closed")
#
#
#     except Error as e:
#         print(e)
#
#     finally:
#         if conn is not None and conn.is_connected():
#             conn.close()
#
# def connectpostgres():
#     conn = None
#     try:
#         conn = psycopg2.connect(user="postgres", database="suppliers", password="postgres", host="localhost", port=5432)
#         conn.autocommit = True
#         cursor = conn.cursor()
#         cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#         sql = '''CREATE TABLE EMPLOYEE(
#                    FIRST_NAME CHAR(20) NOT NULL,
#                    LAST_NAME CHAR(20),
#                    AGE INT
#                 )'''
#
#         sql1 = ''' INSERT INTO EMPLOYEE VALUES('Rohan','Akhtar',22) '''
#         sql2 = ''' INSERT INTO EMPLOYEE VALUES('Usama','Bashir',23) '''
#         sql3 = ''' INSERT INTO EMPLOYEE VALUES('John','Doe',54) '''
#         sql4 = '''select * from EMPLOYEE;'''
#
#         cursor.execute(sql)
#         cursor.execute(sql1)
#         cursor.execute(sql2)
#         cursor.execute(sql3)
#         cursor.execute(sql4)
#         records = cursor.fetchall()
#         print(records)
#
#         conn.close()
#         print("Connection Terminated")
#     except Error as e:
#         print(e)

# def connectsqlite():
#     conn = None
#     try:
#         conn = sqlite3.connect('SQLite_Python.db')
#
#         cursor = conn.cursor()
#         cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#         sql = '''CREATE TABLE EMPLOYEE(
#                    FIRST_NAME CHAR(20) NOT NULL,
#                    LAST_NAME CHAR(20),
#                    AGE INT
#                 )'''
#
#         sql1 = ''' INSERT INTO EMPLOYEE VALUES('Rohan','Akhtar',22) '''
#         sql2 = ''' INSERT INTO EMPLOYEE VALUES('Usama','Bashir',23) '''
#         sql3 = ''' INSERT INTO EMPLOYEE VALUES('John','Doe',54) '''
#         sql4 = '''select * from EMPLOYEE;'''
#
#         sql5 = '''UPDATE EMPLOYEE
#         SET AGE = 23
#         WHERE FIRST_NAME = 'Rohan';'''
#
#         cursor.execute(sql)
#         cursor.execute(sql1)
#         cursor.execute(sql2)
#         cursor.execute(sql3)
#         cursor.execute(sql4)
#         records = cursor.fetchall()
#         print("records before updation")
#         print(records)
#
#         cursor.execute(sql5)
#         cursor.execute(sql4)
#         records2 = cursor.fetchall()
#         print("records after updation")
#         print(records2)
#
#         conn.commit()
#         conn.close()
#         print("Connection Terminated")
#     except Error as e:
#         print(e)


# def getapi():
#     response = requests.get("http://jsonplaceholder.typicode.com/todos")
#
#     for i in response.json():
#         print(i)


# def postapi():
#     apiurl = "https://pastebin.com/api/api_post.php"
#
#     # your API key here
#     key = "Sd5gud15zRqHu6YGLjVmoKf5iOW_Fmq6"
#
#     source_code = '''
#     print("Hello, world!")
#     a = 1
#     b = 2
#     print(a + b)
#     '''
#
#     data = {'api_dev_key': key,
#             'api_option': 'paste',
#             'api_paste_code': source_code,
#             'api_paste_format': 'python'}
#
#     # sending post request and saving response as response object
#     r = requests.post(url=apiurl, data=data)
#
#     # extracting response text
#     pastebin_url = r.text
#     print("The pastebin URL is:%s" % pastebin_url)


# def deleteapi():
#     x = requests.delete('https://w3schools.com/python/demopage.php')
#
#     print(x)


# def putapi():
#     apiurl = "https://pastebin.com/api/api_post.php"
#
#     # your API key here
#     key = "Sd5gud15zRqHu6YGLjVmoKf5iOW_Fmq6"
#
#     source_code = '''
#             print("Hello, world!")
#             a = 1
#             b = 3
#             print(a + b)
#             '''
#
#     data = {'api_dev_key': key,
#             'api_option': 'paste',
#             'api_paste_code': source_code,
#             'api_paste_format': 'python'}
#
#     r = requests.put(apiurl, data)
#     print(r)
#     print(r.text)


# def patchapi():
#     apiurl = "https://pastebin.com/api/api_post.php"
#
#     # your API key here
#     key = "Sd5gud15zRqHu6YGLjVmoKf5iOW_Fmq6"
#
#     source_code = '''
#         print("Hello, world!")
#         a = 1
#         b = 3
#         print(a + b)
#         '''
#
#     data = {'api_dev_key': key,
#             'api_option': 'paste',
#             'api_paste_code': source_code,
#             'api_paste_format': 'python'}
#
#     r = requests.patch(apiurl, data)
#     print(r)
#     print(r.text)


# def insertintosqldb():
#     r = requests.get("http://jsonplaceholder.typicode.com/todos")
#
#     conn = None
#     try:
#         conn = sqlite3.connect('SQLite_Python.db')
#
#         cursor = conn.cursor()
#         cursor.execute("DROP TABLE IF EXISTS APIDATA")
#         sql = '''CREATE TABLE APIDATA(
#                        userId INT NOT NULL,
#                        id INT,
#                        title nvarchar(100)
#                     )'''
#         cursor.execute(sql)
#
#         for i in r.json():
#             cols = []
#             cols.append(i['userId'])
#             cols.append(i['id'])
#             cols.append(i['title'])
#             insertsql = '''INSERT INTO APIDATA (userId,id,title) VALUES (?,?,?);'''
#             cursor.execute(insertsql, cols)
#
#         sql3 = '''SELECT * FROM APIDATA'''
#         cursor.execute(sql3)
#         records = cursor.fetchall()
#         print(records)
#         conn.commit()
#         conn.close()
#         print("Connection Terminated")
#     except Error as e:
#         print(e)


def insertjsonincsv():
    r = requests.get("https://gorest.co.in/public/v1/users")

    jsondata = json.dumps(r.json())
    with open("example.json", 'w') as jsonFile:
        json.dump(r.json(), jsonFile)

    with open("example.json", 'r') as jsonFile:
        data = json.load(jsonFile)

    onlydata = data["data"]
    # onlydata = r.json["data"]
    header = []
    for x in onlydata:
        keys = list(x.keys())
        if (keys not in header):
            header.append(keys)
    # print(header[0])
    with open("jsontocsv.csv", 'w') as jcsvfile:
        writer = csv.DictWriter(jcsvfile, fieldnames=header[0])
        writer.writeheader()
        for i in onlydata:
            writer.writerow(i)


def insertcsvintojason():
    data = []
    with open("jsontocsv.csv", 'r') as csvtojson:
        reader = csv.DictReader(csvtojson)
        for i in reader:
            data.append(i)
            print(i)

    # print(data)
    jsondata = json.dumps(data, indent = 4)
    # print(jsondata)

    with open("csvtojsonresult.json", 'w') as f:
        f.write(jsondata)


def jsontomysqldb():
    r = requests.get("https://gorest.co.in/public/v1/users")

    jsondata = json.dumps(r.json())
    with open("example.json", 'w') as jsonFile:
        json.dump(r.json(), jsonFile)

    with open("example.json", 'r') as jsonFile:
        data = json.load(jsonFile)
    onlydata = data["data"]
    conn = None
    try:
        conn = mysql.connector.connect(host='192.168.20.6', #mysql2 container
                                       database='rohan',
                                       user='root',
                                       password='rohansqlpassword',
                                       )
        if conn.is_connected():
            print('Connected to MySQL database')
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS APIDATA")
        sql = '''CREATE TABLE APIDATA(
                               Id INT NOT NULL,
                           Name char(50),
                           Email char(100),
                           Gender char(50),
                           Status char(20)
                        )'''
        cursor.execute(sql)

        for i in onlydata:
            cols = []
            cols.append(i['id'])
            cols.append(i['name'])
            cols.append(i['email'])
            cols.append(i['gender'])
            cols.append(i['status'])
            insertsql = '''INSERT INTO APIDATA (Id,Name,Email,Gender,Status) VALUES (%s,%s,%s,%s,%s);'''
            cursor.execute(insertsql, cols)
            # print(cols)

        sql3 = '''SELECT * FROM APIDATA'''
        cursor.execute(sql3)
        records = cursor.fetchall()
        print(records)
        conn.commit()
        conn.close()
        print("Connection Terminated")
    except Error as e:
        print(e)


def csvtopostgresdb():
    conn = None
    try:
        conn = psycopg2.connect(user="postgres", password="rohansqlpassword", host="192.168.20.3", port=5432)
        print('Connected to postgres database')
        with open("jsontocsv.csv", 'r') as f:
            reader = csv.DictReader(f)
            # header = next(reader)
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS APIDATA")
            sql = '''CREATE TABLE APIDATA(
                                          Id INT NOT NULL,
                                      Name char(50),
                                      Email char(100),
                                      Gender char(50),
                                      Status char(20)
                                   )'''
            cursor.execute(sql)

            for i in reader:
                cols = []
                cols.append(i['id'])
                cols.append(i['name'])
                cols.append(i['email'])
                cols.append(i['gender'])
                cols.append(i['status'])
                insertsql = '''INSERT INTO APIDATA (Id,Name,Email,Gender,Status) VALUES (%s,%s,%s,%s,%s);'''
                cursor.execute(insertsql, cols)
                # print(cols)

            sql3 = '''SELECT * FROM APIDATA'''
            cursor.execute(sql3)
            records = cursor.fetchall()
            print(records)
            conn.commit()
            conn.close()

    except Error as e:
        print(e)


def mysqldbtocsv():
    conn = None
    try:
        conn = mysql.connector.connect(host='192.169.5.2',  # mysql2 container
                                       database='rohan',
                                       user='root',
                                       password='rohansqlpassword',
                                       )
        if conn.is_connected():
            print('Connected to MySQL database')

        cursor = conn.cursor()
        sql = '''Select * from APIDATA'''
        cursor.execute(sql)
        records = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        # print(field_names)
        with open("DBTOCSV.csv", 'w') as f:
            writer = csv.writer(f)

            writer.writerow(field_names)

            for i in records:
                writer.writerow(list(i))
                # print(type(list(i)))

        conn.commit()
        conn.close()
        print("Connection Terminated")
    except Error as e:
        print(e)




def localfiletomysql():
    conn = None
    try:
        conn = mysql.connector.connect(host='192.169.5.2',  # mysql2 container
                                       database='rohan',
                                       user='root',
                                       password='rohansqlpassword',
                                       )
        if conn.is_connected():
            print('Connected to MySQL database')

        with open("jsontocsv.csv", 'r') as f:
            reader = csv.DictReader(f)
            # header = next(reader)
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS APIDATA")
            sql = '''CREATE TABLE APIDATA(
                                          Id INT NOT NULL,
                                      Name char(50),
                                      Email char(100),
                                      Gender char(50),
                                      Status char(20)
                                   )'''
            cursor.execute(sql)
            cols = []

            for i in reader:
                cols.append((i['id'], i['name'], i['email'], i['gender'], i['status']))

                # print(cols)
            insertsql = '''INSERT INTO APIDATA (Id,Name,Email,Gender,Status) VALUES (%s,%s,%s,%s,%s);'''
            cursor.executemany(insertsql, cols)

            sql3 = '''SELECT * FROM APIDATA'''
            cursor.execute(sql3)
            records = cursor.fetchall()
            print(records)
            conn.commit()
            conn.close()

    except Error as e:
        print(e)





if __name__ == '__main__':
    # connect()
    # connectpostgres()
    # connectsqlite()

    # print("ENTER 1 for get, 2 for post, 3 for delete, 4 for put, 5 for patch, 6 to push api data to sql database : ")
    # i = int(input("Enter value:"))
    # if i == 1:
    #     getapi()
    # elif i == 2:
    #     postapi()
    # elif i == 3:
    #     deleteapi()
    # elif i == 4:
    #     putapi()
    # elif i == 5:
    #     patchapi()
    # elif i == 6:
    #     insertintodb()

    print("Enter 1 for inserting json into csv")
    print("Enter 2 for inserting csv into json")
    print("Enter 3 for inserting json into DB(mysql)")
    print("Enter 4 for inserting csv into DB(postgres)")
    print("Enter 5 for inserting DB into csv")
    print("Enter 6 for batch insert csv into DB")
    choice = int(input("Enter Value:"))
    if choice == 1:
        insertjsonincsv()
    elif choice == 2:
        insertcsvintojason()
    elif choice == 3:
        jsontomysqldb()
    elif choice == 4:
        csvtopostgresdb()
    elif choice == 5:
        mysqldbtocsv()
    elif choice == 6:
        localfiletomysql()