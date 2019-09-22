import mysql.connector as mysql

def get_connection():
    connection = mysql.connect(
        host = "localhost",
        user = "root",
        passwd = "12345",
        database = "trafficviolation",
        auth_plugin = 'mysql_native_password'
    )

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)
    
    return connection



    

