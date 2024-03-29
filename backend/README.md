# Flask demo

This demo of weather application backend with flask in python3.

## Recommended environment

Linux operating system and python 3.8+

## Project Setup

```sh
pip3 install -r requirements
```

## Project Run

```sh
gunicorn -c gunicorn.py main:app
```

## Swagger Doc
```
browser access address
http://localhost:8080/apidocs
```

## Unit Test
```shell
cd test
pytest
```