# Andela Master Class SuperMarket
This repo is to demonstrate how to connect a Flask API to a Postgres database

## Getting Started
* Clone the repo
	`git clone https://github.com/KengoWada/MasterClass.git`
* Then
	`cd MasterClass`
* If you don't have virtualenv installed
	`pip install virtualenv`
* Create a virtual environment
	`python -m virtualenv venv` 
	OR
	`python3 -m venv venv` if you have more than one python version installed
* Activate the virtual environment
	`source venv/bin/activate` for Unix/Linux
	`source venv/Scripts/activate` for Windows
* Install the packages from requirements.txt
	`pip install -r requirements.txt`
* Change database credentials in db.py
* Run the app
	`python app.py` OR
	`python3 app.py` if you have more than one python version installed

### Built With
* [Python/Flask](http://flask.pocoo.org/)
* [psycopg2](http://initd.org/psycopg/docs/)

### Author
* [Kengo Wada](https://github.com/KengoWada)

### Acknowledgements
Thanks to [Andela](https://uganda.andela.com) for giving me the opportunity to help other grow.
