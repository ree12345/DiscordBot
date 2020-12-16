import logging
import psycopg2
from datetime import datetime
logger=logging.getLogger()

# Database connection


def create_db_connection():
    conn = psycopg2.connect(host='localhost',database='postgres', port=5432)
    return conn


def post_search_data(user_id, keyword):
    try:
        connection = create_db_connection()
        sql_cursor = connection.cursor()
        sql_cursor.execute("Insert into public.searches Values('{}', '{}', '{}')".format(
            user_id, keyword, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        connection.commit()
        connection.close()
    except:
        logger.info("Error while inserting history data")


def get_search_data(user_id, keyword):
    results = ''
    try:
        connection = create_db_connection()
        sql_cursor = connection.cursor()
        print(keyword)
        sql_cursor.execute("Select distinct keyword from public.searches where user_id = '{}' and keyword like '%".format(user_id) + keyword +"%'")
        results = sql_cursor.fetchall()
        connection.close()
    except:
        logger.info("Error while fetching history data")
    return results