import mindsdb_sdk

# Connect to MindsDB
mdb = mindsdb_sdk.connect()

# Step 1: Create the MySQL integration in MindsDB
try:
    mysql_demo_db = mdb.create_database(
        engine = "mysql",
        name = "mysql_demo_db",
        connection_args = {
        "user": "mindsdb_user",
        "password": "mindsdb_password",
        "host": "db",
        "port": "3306",
        "database": "complaints_db"
        }
    )
    print("MySQL integration with MindsDB created successfully.")
except Exception as e:
    print("Error creating MySQL integration:", e)

# Step 2: Train a model to predict the 'ma' column
try:
    mdb.query("""
        CREATE MODEL mindsdb.house_sales_model
        FROM mysql_integration
        (SELECT * FROM house_sales)
        PREDICT ma
        ORDER BY saledate
        GROUP BY bedrooms, type
        WINDOW 8
        HORIZON 4;
    """)
    print("Model training initiated successfully.")
except Exception as e:
    print("Error training model:", e)

# Query to get predictions using the trained model
try:
    result = mdb.query("""
        SELECT m.saledate AS date, m.ma AS forecast
        FROM mindsdb.house_sales_model AS m
        JOIN mysql_demo_db.house_sales AS t
        WHERE t.saledate > LATEST
        AND t.type = 'house'
        AND t.bedrooms = 3
        LIMIT 4;
    """)
    print(result.fetch())
    # for row in result:
    #     print(row)
except Exception as e:
    print("Error querying model for predictions:", e)

# Create a job to retrain the model every 2 days if new data is available
try:
    mdb.query("""
        CREATE JOB retrain_model_and_save_predictions (
            RETRAIN mindsdb.house_sales_model
            FROM mysql_integration
            (SELECT * FROM house_sales)
        )
        EVERY 2 days
        IF (SELECT * FROM mysql_integration.house_sales WHERE created_at > LAST);
    """)
    print("Retraining job created successfully.")
except Exception as e:
    print("Error creating retraining job:", e)

