# Flask template for microservices
Python Flask API template using type hints, ready for being used as a microservice.

Requirements: Python 3.9+

## Get Started

### Installation

```sh
$ pip install -r requirements/development.txt
```

This will install all dependencies necessary to develop the project. If you wish
just to run the application, instal `requirement.txt` instead

### Running in development

```sh
$ flask run
```

### Running in production

```sh
gunicorn -w 4 app:app --preload
```

