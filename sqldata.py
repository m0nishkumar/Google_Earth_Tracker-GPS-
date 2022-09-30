import mysql.connector
def main():

    connection = mysql.connector.connect(
    host="sql6.freesqldatabase.com",
    port="3306",
    user="sql6514013",
    password="Z64ed66aI7",
    database="sql6514013"
  )

    sql_select_Query = "select * from data"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        lat=row[1]
        lon=row[0]
        listt.append([lat,lon])
        
listt=[]
main()


