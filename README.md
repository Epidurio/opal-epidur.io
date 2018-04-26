
[![supported_by_apperta.png](https://github.com/AppertaFoundation/apperta-image-assets/blob/master/supported_by_apperta.png)](https://apperta.org/)

------

# opal-epidur.io
Port of epidur.io using the [Opal](https://github.com/openhealthcare/opal) healthcare application framework

### Try out the Epidur.io web demo
https://epidurio.herokuapp.com
username: super
password: super1

### Get a local demo of Epidur.io running with Docker
Definitely the easiest way to get up and running with a locally-running version of Epidur.io is to use Docker and Docker-Compose to automatically install all dependencies and create discrete containers for the web application and database.

#### Prerequisites:
* git
* Docker
* Docker-Compose
* Some familiarity with the command-line/shell on your platform of choice

Installation instructions for Docker and Docker Compose vary according to the platform you are using, so please search the web for instructions appropriate to your OS platform.

#### howto
Clone this repo to a directory on your local machine
```bash
$ git clone git@github.com:Epidurio/opal-epidur.io.git
```
cd into the new directory
```bash
$ cd opal-epidur.io.git
```
start docker-compose:
```bash
$ docker-compose up
```
docker-compose will orchestrate the creation of two Docker containers:

`db` - which will contain postgresql in a minimal linux operating system

`web` - which contains python and our Python web application in a minimal operating system

It also:
* connects the two containers so that Python can connect to the database
* Sets up port forwarding from the `web` container to the 'outside world' (your local machine which is the 'host' of the Docker containers). In this case, it's forwarding Django's default port of 8000 to your localhost:8001 (just in case you want to run a local Django as well, then they won't cause a port conflict). This can be modified in the file `docker-compose.yml` if you want a different port.
* Arranges the file system so that changes you make in your `opal-epidurio/` directory are synced with the webapp inside the `web` container. You can make changes to files on your local machine, using any text editor or IDE, and the files will remain in sync with the files inside the container.

There are just one or two other things needed at this point, one of which is to migrate the database so that it has all the tables and fields we need for our application.
```bash
$ sudo docker-compose run web python manage.py migrate
```

(WIP)

### Developing Epidur.io
(with notes for the errant Rubyist and indication of what is Python, what is Django, and what is Opal)

**Prerequisites:** you should have [Python 3](https://www.python.org/downloads/) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) installed on your machine.

* clone the sources locally

`git clone https://github.com/Epidurio/opal-epidur.io epidurio/`

* enter source directory

`cd epidurio`

* if using virtualenv & virtualenvwrapper (like RVM but for Python), set up your virtualenv (virtualenvs are like RVMs Gemsets and Ruby versions in one)

`mkvirtualenv {{ your_virtualenv_name }}`

* tell virtualenv that the current directory is where you work on epidur.io (this enables you to use the 'workon' command in future)

`setvirtualenvproject`

* install dependencies (Python - equivalent to Bundler's `bundle install`)

`pip install -r requirements.txt`

* create and migrate the database (Django - equivalent of `rake db:create && rake db:migrate`)

`python manage.py migrate`

* install lookup_lists which are picklists of clinical content (Opal-specific)
* eventually we hope to have these lookup_lists SNOMED-ized

`python manage.py load_lookup_lists`

* Create superuser

`python manage.py createsuperuser`

* run the server (Django equivalent of 'rails s')

`python manage.py runserver`

* navigate to the application in a browser, usually it is at [http://localhost:8000/](http://localhost:8000/)

* check out Admin interface at /admin


### FHIR integration
* Epidur.io simply uses the Python `Requests` library to interface with the FHIR server.
* We did experiment with the FHIRClient [fhirclient](https://github.com/smart-on-fhir/client-py) library, which is designed to provide a Pythonic, object oriented API for the FHIR server, however for our purposes it was simply much more than we needed.


### Deploying your new Opal application to Heroku for testing/demo
http://opal.openhealthcare.org.uk/docs/guides/deployment/


### Running Epidur.io in development
* to create seed data with patients and locations in Labour Ward:
```python
python manage.py create_dev_labour_ward
```

### Copyright
This software is Copyright (c) 2018 Tim Knowles and is released without warranty as open source software under the GNU Affero GPL (AGPL) v3 license.
