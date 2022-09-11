# Interologic Python Microservice Template

This repo acts as a template to create restful microservices providing CRUD-based operations in python. 

You can use this repo to get you started with a shell and build upon it. 

## Requirements

* docker >= 2.1.0.0
* pip >= 19.2.3
* pipenv >= 2018.11.26
* python >= 3.7.4

## Running Locally for Development (Quickstart)

### Get Code
```bash
# Clone the repo
git clone git@github.com:interologic/python-microservice-template.git
```

### Setup Virtual Environment
```bash
pipenv shell
```

### Install Dependencies
```bash
pipenv install
```

### Start Development Server
```bash
invoke start
```

## Structure

### Top-level

    .
    ├── .circleci               # circleci configuration
    ├── src                     # source files i.e. routes, models and data access
    ├── tests                   # unit tests
    ├── app.py                  # application entrypoint
    ├── config.py               # configuration class
    ├── Dockerfile              # docker configuration
    ├── Pipfile                 # python dependencies declaration (should be committed to github)
    ├── Pipfile.lock            # lock file to ensure deterministic builds (should also be committed to github)
    ├── task.py                 # defines and invokes various tasks e.g. `invoke start`, `invoke lint`, etc.
    ├── .flake8                 # linting configuration
    ├── .env                    # local configuration settings
    └── README.md

### API

    .
    ├── ...
    ├── api
    │   ├── data                # data access code e.g. database schemas & mapping files 
    │   ├── models              # resource modes that contain business logic, validation & error handling
    │   └── routes              # restful api routes
    └── ...

## Important Routes

### Version
```
/v1/version
```

### Docs
```
/v1/docs
```

### Health
```
/v1/health
```

## Tasks

### Start Development Server
```bash
invoke start
```

### Lint
```bash
invoke lint
```

### Test
```bash
invoke test
```
