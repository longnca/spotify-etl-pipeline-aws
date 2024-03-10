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

Check out the [detailed tutorial](./docs/detailed_tutorial.md)
