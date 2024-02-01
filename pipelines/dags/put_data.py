import sqlite3
import pandas as pd

def put_data():
    emydb = sqlite3.connect("/opt/airflow/dags/yelp.db")

    cursor = emydb.cursor()
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS resto_scraped (
        city VARCHAR(255),
        name VARCHAR(255),
        review VARCHAR(255),
        nb_review VARCHAR(255),
        cuisine VARCHAR(255),
        price VARCHAR(255)
    )"""

    cursor.execute(create_table_query)
    df = pd.read_csv("data.csv")
    
    # Convert DataFrame to list of tuples
    df.to_sql("resto_scraped", emydb, if_exists="replace")
    
    # Commit the changes
    emydb.commit()

    print("Data has been put into the table")
