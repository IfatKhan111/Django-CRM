import mysql.connector as mc

dataBase = mc.connect(
    host='localhost',
    user='root',
    passwd='@Q1w2e3r4',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crmco")

print("Database crmco created successfully!!!")
