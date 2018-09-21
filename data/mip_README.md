# Data registration

Data must be described using [Tabular data package descriptor](https://frictionlessdata.io/specs/tabular-data-package/) and the file datapackage.json should be included into this directory.

To get started quickly,

* create CSV files containing the data that you want to upload to the database, or sample data if you want only to prepare the database to store your data.
* use a tool such as [Goodtables CLI](https://github.com/frictionlessdata/goodtables-py#running-on-cli) to generate the data package json descriptor.
```
  goodtables -o datapackage.json init mip_cde.csv CUSTOM.csv
```
* if you do not want to upload any data in the database, delete the csv file or empty it of data and keep only the CSV header, then set the path property in datapackage.json to ""
* in the schema section of datapackage json, add the following properties:
  * "tableName": name of the table to be created in the database
  * "primaryKey": name of the primary key
  * "datasetKey": name of the key used to identify the dataset if you plan to store different datasets into the same table
