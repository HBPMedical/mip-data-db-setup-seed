[![CHUV](https://img.shields.io/badge/CHUV-LREN-AF4C64.svg)](https://www.unil.ch/lren/en/home.html) [![License](DATA_LICENSE_BADGE)](https://github.com/LREN-CHUV/CUSTOM-data-db-setup/blob/master/LICENSE)
[![build status](GIT_HTTP_REPO/CUSTOM-data-db-setup/badges/master/build.svg)](GIT_HTTP_REPO/CUSTOM-data-db-setup/commits/master)

# Docker image for CUSTOM_LABEL dataset

This Docker image manages the database migration scripts for the CUSTOM_LABEL dataset.

A table is created to host CUSTOM_LABEL data.

IFDATA: The data is loaded from the csv file included in the Docker image, then uploaded into the database.
IFNODATA: This image does not contain any data from CUSTOM_LABEL, only the definitions.

## How to build the Docker image

Run: `./build.sh`

## Testing

```
  ./test/test.sh
```

## Usage

Run:

```console
$ docker run -i -t --rm -e FLYWAY_HOST=`hostname` DOCKER_REPO/CUSTOM-data-db-setup:0.0.1 migrate
```

where the environment variables are:

* FLYWAY_HOST: database host, default to 'db'.
* FLYWAY_PORT: database port, default to 5432.
* FLYWAY_DATABASE_NAME: Optional, name of the database or schema, default to 'data'
* FLYWAY_URL: JDBC url to the database, constructed by default from FLYWAY_DBMS, FLYWAY_HOST, FLYWAY_PORT and FLYWAY_DATABASE_NAME
* FLYWAY_DRIVER: Optional, fully qualified classname of the jdbc driver (autodetected by default based on flyway.url)
* FLYWAY_USER: database user, default to 'meta'.
* FLYWAY_PASSWORD: database password, default to 'meta'.
* FLYWAY_SCHEMAS: Optional, comma-separated list of schemas managed by Flyway, default to 'public'

After execution, you should have:

* A table named **CUSTOM_features** whose columns match the CUSTOM_LABEL-specific variables.
* The **CUSTOM_LABEL** dataset loaded into **CUSTOM_features**.

# Acknowledgements

This work has been funded by the European Union Seventh Framework Program (FP7/2007­2013) under grant agreement no. 785907 (HBP)

This work is part of SP8 of the Human Brain Project (SGA2).
