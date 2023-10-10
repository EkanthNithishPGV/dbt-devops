#!/bin/sh

dbt --version
dbt --version --profiles-dir .  # Pulls the most recent version of the dependencies listed in your packages.yml from git
dbt deps --profiles-dir .  # Pulls the most recent version of the dependencies listed in your packages.yml from git


echo dbt run
dbt run