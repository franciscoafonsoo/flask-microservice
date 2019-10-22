# Flask template for microservices
Python Flask API template using type hints, ready for being used as a microservice.

Requirements: Python 3.7+

## Get Started

### Installation

```sh
$ pip install -r requirements.txt
```

### Type checking

```sh
# init pyre configuration
$ pyre init

# type check the project
$ pyre check
```

### Running in development

```sh
$ flask run
```

### Running in production

```sh
gunicorn -w 4 app:app --preload
```

