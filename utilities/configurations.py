import configparser
import mysql.connector

from mysql.connector import Error


# Read config values from properties.ini
def get_config():
    config = configparser.ConfigParser()
    config.read('./utilities/properties.ini')
    return config


def get_api_password():
    return "mypassword"


# Dictionary for MySQL connection config
connection_config = {
    'host': get_config()['MySQL']['host'],
    'database': get_config()['MySQL']['database'],
    'user': get_config()['MySQL']['user'],
    'password': get_config()['MySQL']['password'],
}


# Connects to MySQL and returns connection object
def get_connection():
    try:
        conn = mysql.connector.connect(**connection_config)  # ** indicates that we send dictionary
        if conn.is_connected():
            print("Connection Successful")
            return conn
    except Error as e:
        print(e)


# Connects to MySQL, executes query and returns the first record
def get_query(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row
