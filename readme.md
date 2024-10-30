# Setting Up MySQL and MindsDB with Docker

## Overview
This guide will walk you through the steps to set up a MySQL database, Adminer for database management, and MindsDB for machine learning predictions using Docker. We will use Docker Compose to manage our containers.

## Prerequisites
- **Docker**: Ensure you have Docker Desktop installed on your machine.
- **Docker Compose**: This usually comes with Docker Desktop, but verify it's available by running `docker-compose --version` in your terminal.

## Step 1: Create a Docker Compose File
1. **Create a new directory** for your project:
   ```bash
   mkdir mysql_mindsdb_project
   cd mysql_mindsdb_project
   ```

2. **Create a `docker-compose.yml` file** in this directory:
   ```yaml
   version: '3.8'

   services:
     mysql:
       image: mysql:5.7
       restart: always
       environment:
         MYSQL_ROOT_PASSWORD: root_password
         MYSQL_DATABASE: complaints_db
         MYSQL_USER: mindsdb_user
         MYSQL_PASSWORD: mindsdb_password
       ports:
         - "3306:3306"

     adminer:
       image: adminer
       restart: always
       ports:
         - "8080:8080"

     mindsdb:
       image: mindsdb/mindsdb
       restart: always
       ports:
         - "47334:47334"  # MindsDB web interface
       depends_on:
         - mysql
   ```

3. **Save the file**.

## Step 2: Start the Docker Containers
1. **Open your terminal** and navigate to your project directory.
2. Run the following command to start the containers:
   ```bash
   docker-compose up -d
   ```
3. This command will start the MySQL, Adminer, and MindsDB containers in detached mode.

## Step 3: Verify the Setup
- **MySQL**: Access MySQL using Adminer by navigating to `http://localhost:8080` in your web browser.
  - **System**: MySQL
  - **Server**: mysql
  - **Username**: mindsdb_user
  - **Password**: mindsdb_password
  - **Database**: complaints_db
- **MindsDB**: Access MindsDB by navigating to `http://localhost:47334`.

## Step 4: Run the Provided Python Code
1. **Install the required libraries**:
   ```bash
   pip install mysql-connector-python mindsdb_sdk
   ```
2. **Create a Python file** (e.g., `setup_mindsdb.py`) and copy the provided code into it.

3. **Adjust the MySQL connection details** in your code if necessary to match the ones specified in your Docker Compose file.

4. **Run the Python script**:
   ```bash
   python setup_mindsdb.py
   ```

## Code Explanation
- **MySQL Connection**: The code connects to the MySQL database using the specified configuration and creates a table named `house_sales`.
- **Data Insertion**: It populates the `house_sales` table with dummy data, simulating house sales over time.
- **MindsDB Integration**: The code connects to MindsDB, creates a MySQL integration, trains a model on the `house_sales` data, and retrieves predictions.
- **Retraining Job**: A job is created to retrain the model every two days if new data is available.

## Step 5: Verify Data and Predictions
- You can check the data in the `house_sales` table using Adminer.
- Monitor the MindsDB interface for model training and predictions.

## Conclusion
You have successfully set up MySQL, Adminer, and MindsDB using Docker and run a Python script to train a predictive model on house sales data. You can now extend this project by integrating real data or enhancing your predictive model.
