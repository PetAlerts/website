## Setup

Install `git` and clone the GitHub repository:
    
    $ sudo apt-get install git
    $ git clone https://github.com/PetAlerts/website.git

Install system-wide dependencies:

    $ sudo apt-get install libpq-dev libjpeg-dev python-dev python-virtualenv

Install Heroku Toolbelt:

    $ wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh

Use `virtualenv` and install required packages:

    $ cd website
    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt

Create an `.env` file with content:

    DATABASE_URL="sqlite:////path/to/db.sqlite3"

Migrate:

    $ foreman run ./manage.py migrate

Run the development server:

    $ foreman run ./manage.py runserver
