# atlas-the-joy-of-painting-api

This project uses the concepts of ETL (extract, transform, load) to take different unorganized but related data sources and storing them in a SQL server.

UML documentation is done with [draw.io](https://draw.io)

# SQL server (./sql)

SQL server runs as a docker container. To build and run use these commands inside the sql folder. The api server's user is set as read only since the data will not need to be modified afterwards.
```
make build
make run
```
