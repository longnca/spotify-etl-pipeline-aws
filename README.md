# Spotify data pipeline tutorial

This project aims to build a serverless extract, transform, and load (ETL) pipeline on Spotify data.

## Architecture 

![diagram](assets/spotify-etl-pipeline-aws-architecture.png)

The workflow illustrated in the diagram consists of these high-level steps:

1. At a predefined schedule (e.g. daily), an **AWS Lambda function** uses Python scripts to connect to Spotify's API to fetch the raw data in JSON format.
1. A daily schedule using **Amazon EventBridge** will trigger the AWS Lambda Data Extraction function.
1. The AWS Lambda Data Extraction function collects the raw JSON files and stores them in in a "raw_data/to_process" folder on the **Amazon S3** bucket.
1. After the data is stored in S3, any new data addition triggers another AWS Lambda function called "Data Transformation function". This function will clean and transform raw data to CSV files.
1. The transformed CSV data will be saved back to Amazon S3, but in a different location called "transformed_data" folder to distinguish it from the raw data.
1. An **AWS Glue Crawler** creates the schema from the transformed file stored in Amazon S3.
1. The resulting schema is stored in **AWS Glue Data Catalog**.
1. The schema can be used by any analytics job by using **Amazon Athena** to run ad-hoc queries.