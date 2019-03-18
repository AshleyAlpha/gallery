## GALLERY
## Author: Alpha Mbabazi
## Description

GALLERY PIC is a simple photo gallery web application that shows beautiful pictures and designs. Users will be able to view photos updated by the admin. Users can see photos based on their categories, by clicking on the listed locations in the menu. They can also copy the link to a photo to paste at their discretion. The search functionality will search photos based on the categories.

## Set Up and Installations

# Prerequisites
* Ubuntu Software
* Python3.6
* Postgres
* python virtualenv

# Clone the Repo
Run the following command on the terminal: git clone https://github.com/AshleyAlpha/gallery.git && cd gallery

# Activate virtual environment
Activate virtual environment using python3.6 as default handler

# Install dependancies

Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

# Create the Database
* psql
* CREATE DATABASE gallery;
# .env file
Create .env file and paste paste the following filling where appropriate:

* SECRET_KEY = '<Secret_key>'
* DBNAME = 'gallery'
* USER = '<Username>'
* PASSWORD = '<password>'
* DEBUG = True

# Run initial Migration

python3.6 manage.py makemigrations gllry
python3.6 manage.py migrate

# Run the app

* python3.6 manage.py runserver
* Open terminal on localhost:8000

## Known bugs
* gettibg image by filter id
* search image by its location

## Technologies used

- Python 3.6
- HTML
- Bootstrap 4
- JavaScript
- Heroku
- Postgresql

## Support and contact details
Contact me on mashleyalpha@gmail.com for any feedback

## License
MIT Copyright (c) 2019 **Alpha Mbabazi**