import psycopg2
from psycopg2 import Error


def insert_dollar_price(price, date):
    try:
        connection = psycopg2.connect(
            user="isaaccavallaro",
            password="",
            host="localhost",
            port="5432",
            database="wsj_data",
        )

        cursor = connection.cursor()
        insert_query = "INSERT INTO dollar_prices (price, date) VALUES (%s, %s)"
        record_to_insert = (price, date)
        cursor.execute(insert_query, record_to_insert)
        connection.commit()
        cursor.close()
        connection.close()

        print("Data inserted into the 'dollar_prices' table successfully.")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL or inserting data:", error)


def insert_news_headline(headline, date):
    try:
        connection = psycopg2.connect(
            user="isaaccavallaro",
            password="",
            host="localhost",
            port="5432",
            database="wsj_data",
        )

        cursor = connection.cursor()
        insert_query = "INSERT INTO news_headlines (headline, date) VALUES (%s, %s)"
        record_to_insert = (headline, date)
        cursor.execute(insert_query, record_to_insert)
        connection.commit()
        cursor.close()
        connection.close()

        print("Data inserted into the 'news_headlines' table successfully.")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL or inserting data:", error)
