import mysql.connector as mysql

def get_connection():
    connection = mysql.connect(
        host = "localhost",
        user = "root",
        passwd = "12345",
        database = "trafficviolation",
        auth_plugin = 'mysql_native_password'
    )

    return connection





