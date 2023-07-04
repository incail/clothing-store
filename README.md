<p align="center">
      <img src="https://img.freepik.com/premium-vector/clothing-store-logo-design-with-hanger-vector-illustration_500223-959.jpg?w=740" width="300" height="250">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/Python-3.10.6-orange" alt="Python Version">
   <img src="https://img.shields.io/badge/Django-3.2.13-blue" alt="Django Version">
   <img src="https://img.shields.io/badge/License-No-green" alt="License">
</p>
The project for study Django.

## About

The project implements applications:
- products - which is responsible for working with products
- users - responsible for authorization, registration, email confirmation, working with the shopping cart, profile display
- orders - ability to pay for goods

<p>Celery is used to send a message to the client's email</p>
<p>Redis is used for caching product cards</p>

## Stakc
- Python
- PostgreSQL
- Redis

## Local Developing

All actions should be executed from the source directory of the project and only after installing all requirements.

1. Firstly, create and activate a new virtual environment:
     <p>python3.9 -m venv ../venv</p>
     <p>source ../venv/bin/activate</p>
      
2. Install packages:
      <p>pip install --upgrade pip</p>
      <p>pip install -r requirements.txt</p>

3. Run project dependencies, migrations, fill the database with the fixture data etc.:
      <p>./manage.py migrate</p>
      <p>./manage.py loaddata <path_to_fixture_files></p>
      <p>./manage.py runserver</p>
      
4. Run Redis Server:
      <p>redis-server</p>
      
5. Run Celery:
      <p>celery -A store worker --loglevel=INFO</p>

## Distribute

- [store-clothing](http://storeclo.fatboy.hostflyby.net/)


## Developers

- [incail](https://github.com/incail)
