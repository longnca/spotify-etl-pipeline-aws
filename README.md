# Spotify data pipeline tutorial

Building an end-to-end data pipeline for Spotify.

In this tutorial, I've completed an end-to-end ETL pipeline for Spotify data:
1. Set up Spotify API.
1. Testing out the codes to extract and transform data in Jupyter Notebook.
1. Set up **AWS S3** buckets with folder structures.
1. Add **AWS Lambda** functions (using Python codes in the Jupyter Notebook) to fetch data from Spotify API and store in `raw_data` folder in S3 buckets.
1. Add **Lambda** functions to transform data and store in `transformed_data` in S3.
1. Create triggers in Lambda to automatically do the extraction and transformation tasks.
1. Set up the crawlers using **AWS Glue** to get data from S3 and then populate the AWS Glue Data Catalog with tables.
1. Use **AWS Athena** to run SQL queries for analytical purposes.

Process flowchart

1. Extract:
- Use Python to connect to Spotify's API to fetch data.
- Automatic load: Set up a schedule with Amazon CloudWatch, which triggers an AWS Lambda function to run in a defined schedule (e.g. daily).
- AWS Lambda function collects the data and stores it in in an Amazon S3 bucket.

2. Transformation:
- After the data is stored in S3, any new data addition triggers another AWS Lambda function. - This function is responsible for cleaning and transforming data.
- This "cleaned" data is then saved back to Amazon S3, but in a different location called "transformed_data" folder to distinguish it from the raw data.

3. Load:
- Set a crawler (infer schema)
- Catalog data using AWS Glue.
- Run analytics and queries directly on Amazon Athena.