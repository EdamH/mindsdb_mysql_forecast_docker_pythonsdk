from datetime import datetime, timedelta
import random
import mysql.connector
from mysql.connector import Error

# MySQL Database Configuration
mysql_config = {
    "user": "mindsdb_user",
    "password": "mindsdb_password",
    "host": "localhost",
    "port": 3306,
    "database": "complaints_db"  # Ensure this matches your MySQL setup
}

# Connect to MySQL and create table
try:
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()
    
    # Create the house_sales table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS house_sales (
            id INT AUTO_INCREMENT PRIMARY KEY,
            saledate DATE,
            ma DECIMAL(10, 2),
            type VARCHAR(10),
            bedrooms INT
        );
    """)
    
    # Insert dummy data into house_sales table
    # Dummy data with 30 entries
    base_date = datetime(2012, 1, 1)  # Start date for house sales
    base_ma = 250000  # Starting moving average price
    house_sales_data = []

    for i in range(50):
        room_num = random.randint(1, 4)  # Random number of bedrooms
        sale_date = base_date + timedelta(days=i * 90)  # Quarterly increments
        ma = base_ma + (i * (room_num/2 + 1/2) * 5000) + random.randint(-6000, 500) # Gradually increasing price
        entry = (sale_date.strftime('%Y-%m-%d'), ma, 'house', room_num)
        house_sales_data.append(entry)
    
    cursor.executemany("""
        INSERT INTO house_sales (saledate, ma, type, bedrooms)
        VALUES (%s, %s, %s, %s);
    """, house_sales_data)
    
    conn.commit()
    print("Dummy data inserted successfully into house_sales table.")
except Error as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    conn.close()