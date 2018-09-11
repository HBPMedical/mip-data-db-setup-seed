[![CHUV](https://img.shields.io/badge/CHUV-LREN-AF4C64.svg)](https://www.unil.ch/lren/en/home.html) [![License](DATA_LICENSE_BADGE)](https://github.com/LREN-CHUV/CUSTOM-data-db-setup/blob/master/LICENSE)
[![build status](https://gitlab.com/hbpmip_private/CUSTOM-data-db-setup/badges/master/build.svg)](https://gitlab.com/hbpmip_private/CUSTOM-data-db-setup/commits/master)

# Docker image for CUSTOM_LABEL dataset

This Docker image manages the database migration scripts for the CUSTOM_LABEL dataset.

CUSTOM_LABEL dataset is split into table mip_cde_features for the CDE features and CUSTOM_features for the CUSTOM_LABEL specific features.

The view mip_local_features contains the variables from both MIP CDE and CUSTOM_LABEL.

This image does not contain any data from CUSTOM_LABEL, only the definitions.

## How to build the Docker image

Run: `./build.sh`

## Usage

Run:

```console
$ docker run -i -t --rm -e FLYWAY_HOST=`hostname` donotdistribute.local/hbpmip_private/CUSTOM-data-db-setup:0.0.1 migrate
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
