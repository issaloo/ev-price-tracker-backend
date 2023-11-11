# EV Price Tracker - Backend

## Overview

The backend repository is built using Django Rest Framework (DRF) to provide robust API routes for interacting with vehicle data. The integration of Redis as the database adds a layer of efficiency, allowing for fast and responsive data retrieval.

## Technologies

- Secret Manager (GCP)
  - Store secrets
- Cloud Source Repositories (GCP)
  - Mirror this repository for cloud function
- Redis (External)
  - Short term data retention for serving to backend
- Django Rest Framework
  - Create Rest API

## Contributing

### General Guidelines

Please take a look at the following guides on writing code:

- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/) for Python

### Set Up Development Environment

1. Clone and navigate to the repository

   ```shell
   cd ~/GitHub/issaloo
   git clone git@github.com:issaloo/ev-price-tracker-scraper.git
   cd ev-price-tracker-scraper
   ```

2. Copy `.env.template` to environment file and fill in configs

For development,

    ```shell
    cp .env.local.template .env.local
    ```

For production,

    ```shell
    cp .env.local.template .env
    ```

3. Install pdm globally

   ```shell
   pip install pdm
   ```

4. Install general & development packages with pdm

   ```shell
   pdm install --dev
   ```

> :information_source: This will install packages [pre-commit](https://pre-commit.com/), [commitizen](https://commitizen-tools.github.io/commitizen/), and [gitlint](https://jorisroovers.com/gitlint/latest/)

(Optional) Install only the general packages

    ```shell
    pdm install
    ```

5. Activate the virtual environment

   ```shell
   eval $(pdm venv activate)
   ```

> :information_source: Virtual environment will use the same python version as the system

(Optional) Deactivate the virtual environment

```shell
deactivate
```

### Set Up Standardized Version Control

1. Automate scripts (i.e., linting and autoformatting)
   ```shell
   pre-commit install
   ```
2. Enforce template at commit with pre-commit
   ```shell
   gitlint install-hook
   ```

### Test It Out

1. **Check if `commitizen` is working**

   - :mag_right: Try using commitizen in command line
     1. Add files to staging
     2. Run commitizen
        ```shell
        git cz c
        ```
        Or, if possible
        ```shell
        cz c
        ```
   - :white_check_mark: You should get structured commits

2. **Check if `gitlint` is working**

   - :mag_right: Try writing a bad commit
     1. Add files to staging
     2. Write a bad commit (e.g., `git commit -m 'WIP: baD commit'`)
   - :white_check_mark: You should get a question on whether to continue the commit.

3. **Check if `pre-commit` is working**

   - :mag_right:
     1. Add files to staging, where at least one python file is not formatted well
     2. Run commitizen
        ```shell
        git cz c
        ```
        Or, if possible
        ```shell
        cz c
        ```
   - :white_check_mark: You should get automatic fixes to poorly formatted python files with some errors

   > :information_source: Ctrl+C to exit commit template

## Running Django Environments

### Local

1. Download the service account credentials json and relocate to the root of this directory

2. Run Redis Cache Locally

   1. Set up network proxy to the redis app hosted on Fly.io

      ```shell
      fly proxy 6379 -a evpricetrackercache
      ```

   2. Open another terminal to connect to the redis app

      ```shell
      redis-cli
      ```

   3. Input password to access the redis app

      ```shell
      auth <password>
      ```

3. Run the local environment settings

   ```Shell
   python manage.py runserver --settings=main.settings.local
   ```

### Production

1. If you have not already, navigate to the repo and deploy

```Shell
gcloud app deploy
```

2. Point your browser to [https://ev-price-tracker.uc.r.appspot.com/](https://ev-price-tracker.uc.r.appspot.com/)

(Optional) Clear deployed app

```Shell
gcloud app deploy dispatch.yaml
```
