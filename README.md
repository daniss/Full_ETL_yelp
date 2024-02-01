# Yelp Data ETL Pipeline with Apache Airflow and Docker-compose

## Overview
This project implements an end-to-end Extract, Transform, Load (ETL) pipeline to gather restaurant data from Yelp.fr, process it, and store it in a SQLite database. Leveraging web scraping techniques with Python and BeautifulSoup, the script collects restaurant details including name, rating, reviews, cuisine type, price range, and location. Apache Airflow is utilized to orchestrate the ETL process, automating tasks and scheduling workflows. Docker-compose simplifies deployment by providing a containerized environment for running Airflow and its dependencies.

## Features
- **Data Collection**: Web scraping is used to extract restaurant data from Yelp.fr, capturing essential information for analysis.
- **Data Transformation**: The collected data is cleaned and transformed to ensure consistency and usability, including handling missing values and standardizing formats.
- **Data Loading**: Processed data is stored in a SQLite database for easy access and retrieval, facilitating further analysis and reporting.
- **Automation with Apache Airflow**: Airflow is employed to automate the ETL process, scheduling tasks and managing dependencies to ensure seamless execution.
- **Containerization with Docker-compose**: Docker-compose is used to containerize Airflow and its dependencies, simplifying deployment and ensuring consistency across environments.

## Getting Started
To run the ETL pipeline locally using Docker-compose, follow these steps:
1. Clone the repository to your local machine.
2. Install Docker and Docker-compose if not already installed.
3. Navigate to the project directory containing the `docker-compose.yaml` file.
4. Run `docker-compose up` to start the Docker containers.
5. Access the Airflow web interface at `http://localhost:8080` and configure the necessary connections and variables.
6. Trigger the ETL pipeline to initiate data extraction, transformation, and loading tasks.
7. Monitor the pipeline execution and access the processed data in the SQLite database.
