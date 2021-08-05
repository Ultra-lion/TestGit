import mysql.connector
import psycopg2
from psycopg2 import Error
from mysql.connector import Error
import sqlite3
import requests
import pandas as pd
import json
import csv

class CSVMANIPULATION:
    def __init__(self):
        pass

    def insertcsvintojason(self):
        data = []
        with open("jsontocsv.csv", 'r') as csvtojson:
            reader = csv.DictReader(csvtojson)
            for i in reader:
                data.append(i)
                print(i)

        # print(data)
        jsondata = json.dumps(data, indent=4)
        # print(jsondata)

        with open("csvtojsonresult.json", 'w') as f:
            f.write(jsondata)

    def csvtodb(self, connection):
        conn = None
        try:
            conn = connection

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


        except Error as e:
            print(e)

    def dbtocsv(self, connection):
        conn = None
        try:
            conn = connection


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
                    print(i)



        except Error as e:
            print(e)


class JSONMANIPULATION:

    def __init__(self):
        pass

    def insertjsonincsv(self):
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
                print(i)

    def jsontodb(self, connection):
        r = requests.get("https://gorest.co.in/public/v1/users")

        jsondata = json.dumps(r.json())
        with open("example.json", 'w') as jsonFile:
            json.dump(r.json(), jsonFile)

        with open("example.json", 'r') as jsonFile:
            data = json.load(jsonFile)
        onlydata = data["data"]
        conn = None
        try:
            conn = connection

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
        except Error as e:
            print(e)


class mysqldb:
    instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if mysqldb.instance == None:
            mysqldb()
        return mysqldb.instance

    def __init__(self):
        if mysqldb.instance == None:
            print("Mysql Connection created")
            self.conn = mysql.connector.connect(host='192.169.5.2',  # mysql2 container
                                               database='rohan',
                                               user='root',
                                               password='rohansqlpassword',
                                               )
            mysqldb.instance = self
        else:
            raise Exception("Singleton class cannot create another instance")

    def getconnection(self):
         return self.conn

    def terminateconnection(self):
        print("mysql connection terminated")
        self.conn.commit()
        self.conn.close()



class postgresdb:
    instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if postgresdb.instance == None:
            postgresdb()
        return postgresdb.instance

    def __init__(self):
        if postgresdb.instance == None:
            self.conn = psycopg2.connect(user="postgres", password="postgres", host="192.168.20.3", port=5432)
            postgresdb.instance = self
            print("postgres connection created")
        else:
            raise Exception("Singleton class cannot create another instance")

    def getconnection(self):
        return self.conn

    def terminateconnection(self):
        print("postgres connection terminated")
        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':


    conn = None
    mydb = None

    print("Enter 1 for mysqldb connection")
    print("Enter 2 for postgresdb connection")
    print("Enter 0 for no database")
    dbchoice = int(input("Enter db choice: "))

    if dbchoice == 1:
        mydb = mysqldb()
        conn = mydb.getconnection()
    elif dbchoice == 2:
        mydb = postgresdb()
        conn = mydb.getconnection()
    else:
        print("No DB Selected")

    print("Enter 1 for inserting json into csv")
    print("Enter 2 for inserting csv into json")
    print("Enter 3 for inserting json into DB")
    print("Enter 4 for inserting csv into DB")
    print("Enter 5 for inserting DB into csv")
    choice = int(input("Enter Value:"))

    c = CSVMANIPULATION()
    j = JSONMANIPULATION()

    if choice == 1:
        j.insertjsonincsv()
    elif choice == 2:
        c.insertcsvintojason()
    elif choice == 3:
        if conn is not None:
            j.jsontodb(conn)
        else:
            print("no connection created")
    elif choice == 4:
        if conn is not None:
            c.csvtodb(conn)
        else:
            print("no connection created")

    elif choice == 5:
        if conn is not None:
            c.dbtocsv(conn)
        else:
            print("no connection created")






    if mydb is not None:
        mydb.terminateconnection()

