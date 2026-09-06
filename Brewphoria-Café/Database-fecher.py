import mysql.connector
from mysql.connector import Error


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        database="Brewphoria_Cafe",
        user="root",
        password="FaceAttendBy$ahaj",
    )


def add_customer(name, country, contact):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO customers
                (name, country, contact, total_purchase, visited_at)
            VALUES (%s, %s, %s, %s, NOW())
            """,
            (name, country, contact, 0),
        )
        connection.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        connection.close()


def update_customer_review(customer_id, rating, total_purchase):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            """
            UPDATE customers
            SET review = %s, total_purchase = %s
            WHERE customer_id = %s
            """,
            (rating, total_purchase, customer_id),
        )
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def fetch_customers():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM customers")
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    for customer in fetch_customers():
        print(customer)

