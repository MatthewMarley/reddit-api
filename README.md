# reddit-api

# To Do List
- Set up reddit API connection
- Create ETL pipeline
	- Extract datasets (AWS lambda function scheduled by Eventbridge?)
	- Load into S3 landing stage
	- S3 module to transfer from landing stage to working stage
	- Trigger Python ETL jobs using pandas within working stage
	- Once transformation is complete, move to processed zone in S3
	- From processed zone, load into Athena table (using glue?)
- Create visualisations from athena dataset

- Use airflow to orchstrate pipeline
- Use AWS to host process

- Add tests

Package specific
- Makefile
- .env file for credentials
- venv
- requirements.txt