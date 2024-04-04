# atlas-the-joy-of-painting-api

This project uses the concepts of ETL (extract, transform, load) to take different unorganized but related data sources and storing them in a SQL server.

# Requirements
    Docker
    python 3.10^
    python-mysql-connector 8.3.0^


UML documentation is done with [draw.io](https://draw.io)

# SQL server (./sql)

SQL server runs as a docker container. To build and run use these commands inside the sql folder. The api server's user is set as read only since the data will not need to be modified afterwards.
```
cd sql
make build
make run
```

# ETL (./ETL)

Extracts data from the given data files and generates a sql file to be used in the SQL server. Also gets all the possible options for the colors and subject

```
cd ETL
# get init.sql
./main.py
cp init.sql ../sql/init.sql
# get options
./get_all_opts.py
```

# api (./api)

Api with a single (/episodes) endpoint that queries the sql server for episodes that matches all/one or more of the episode air month, painting subject and painting color pallete.

This is the shape of the json query. Values in [] are the accepted values which are contained in (./check_query.py)

```
{
    "match": [match_accepted],
    "month": "YYYY-MM-DD"  # in range date_accepted
    "colors": [colors_accepted]
    "subject": [subject_accepted]
}
```


To run

```
cd ./api
python3 app.py
```