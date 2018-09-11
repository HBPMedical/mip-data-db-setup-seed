[![CHUV](https://img.shields.io/badge/CHUV-LREN-AF4C64.svg)](https://www.unil.ch/lren/en/home.html) [![License](https://img.shields.io/badge/license-proprietary-AF4C64.svg)](https://github.com/LREN-CHUV/besta-data-db-setup/blob/master/LICENSE)
[![build status](https://gitlab.com/hbpmip_private/besta-data-db-setup/badges/master/build.svg)](https://gitlab.com/hbpmip_private/besta-data-db-setup/commits/master)

# Docker image for Besta dataset

This Docker image manages the database migration scripts for the Besta dataset.

Besta dataset is split into table mip_cde_features for the CDE features and besta_features for the Besta specific features.

The view mip_local_features contains the variables from both MIP CDE and Besta.

This image does not contain any data from Besta, only the definitions.

## How to build the Docker image

Run: `./build.sh`

## Usage

Run:

```console
$ docker run -i -t --rm -e FLYWAY_HOST=`hostname` donotdistribute.local/hbpmip_private/besta-data-db-setup:0.1.3 migrate
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

* A table named **mip_cde_features** where the columns match the MIP CDE variables.
* The **Besta** dataset loaded into **mip_cde_features**, using only the columns belonging to MIP CDEs. Other datasets can be loaded in parellel from related Docker images (adni-merge-db-setup, edsd-data-db-setup...)
* A table named **besta_features** whose columns match the Besta-specific variables.
* The **Besta** dataset loaded into **besta_features**, using only the Besta-specific variables.
* A view named **mip_local_features** that joins the columns of **mip_cde_features** with **besta_features**.

# Acknowledgements

This work has been funded by the European Union Seventh Framework Program (FP7/2007­2013) under grant agreement no. 604102 (HBP)

This work is part of SP8 of the Human Brain Project (SGA1).
