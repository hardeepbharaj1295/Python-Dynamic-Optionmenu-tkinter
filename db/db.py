import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="py_optionmenu"
)

cursor = con.cursor()


def show_options():
    cursor.execute("select * from options_table")
    # fetch all fetch all the data
    return cursor.fetchall()