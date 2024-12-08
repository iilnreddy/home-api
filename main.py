from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
from typing import List, Any
import app_settings

app = FastAPI()

# Define a Pydantic model for validation
#class Item(BaseModel):
#    name: str
#    description: str

# Create a function to connect to MySQL database
def get_db_connection():
    connection = mysql.connector.connect(
        host=app_settings.host,
        user=app_settings.user,
        password=app_settings.password,
        database=app_settings.database
    )
    return connection

@app.get("/api/items/", response_model=List[Any])
def get_items():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM laptops")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

if __name__ == '__main__':
    row = get_items()
    print('the output is',row)