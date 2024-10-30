# Setting Up MySQL and MindsDB with Docker

## Overview
This guide will walk you through the steps to set up a MySQL database, Adminer for database management, and MindsDB for machine learning predictions using Docker. We will use Docker Compose to manage our containers.

## Prerequisites
- **Docker**: Ensure you have Docker Desktop installed on your machine.
- **Docker Compose**: This usually comes with Docker Desktop, but verify it's available by running `docker-compose --version` in your terminal.

## Install MindsDB Extension
If you are running MindsDB via the Docker Desktop Extension, it is recommended to install the dependencies for Lightwood. To do this:
Open Docker Desktop.
Go to MindsDB Extension
Go to Settings.
Navigate to Manage Integrations.
Follow the instructions to install the Lightwood dependencies. Note that it may take a few minutes to install these dependencies, depending on your network speed and bandwidth.
If you are having trouble installing the MindsDB extension on docker desktop use the following guide => https://docs.mindsdb.com/setup/self-hosted/docker-desktop
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
     db:
       image: mysql:8.0
       environment:
         MYSQL_ROOT_PASSWORD: rootpassword
         MYSQL_DATABASE: complaints_db
         MYSQL_USER: mindsdb_user
         MYSQL_PASSWORD: mindsdb_password
       ports:
         - "3306:3306"
       networks:
         - mindsdb_desktop_network  # Connects to the MindsDB extension network
   
     adminer:
       image: adminer
       ports:
         - 8080:8080
       networks:
         - mindsdb_desktop_network
   
   networks:
     mindsdb_desktop_network:  
       external:
         name: mindsdb_mindsdb-docker-extension-desktop-extension_default


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
2. Run ```python dummy_data.py``` to create & populate the mysql database
3. Run ```python mindsdb_demo.py``` to integrate it into mindsdb, create a predictor, create a forecast & set a job that retrains the model every two days.

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
