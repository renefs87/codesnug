# Codesnug readme

Codesnug is an application which purpose is the storage and categorization of code to access it later.

## Requirements

* Python 2.7.x
* Python pip
* Database: PostgreSQL, MySQL, SQLite

## Installation

Install the dependencies:
```
pip install -r pip-requirements.txt
```

Rename the `settings.py.sample` file to `settings.py`

Configure the database connection settings to your own.

Create the tables in the database:
```
python manage.py migrate
```


## Development

To run the development server:
```
python manage.py runserver
```

## Test

To run the test suite:
```
python manage.py test
```

