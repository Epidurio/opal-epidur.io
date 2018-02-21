# opal-epidur.io
Port of epidur.io code using the [Opal](https://github.com/openhealthcare/opal) healthcare application framework

###

To get started, run the following commands:

```
    python manage.py migrate
    python manage.py runserver
```

### Developing Epidur.io
(with notes for the errant Rubyist and indication of what is Python, what is Django, and what is Opal)

```
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

* Opal has already added a default superuser with username: super and password: super1

* run the server (Django equivalent of 'rails s')
`python manage.py runserver`

* navigate to the application in a browser

* check out Admin interface at /admin


### Deploying your new Opal application to Heroku for testing/demo
http://opal.openhealthcare.org.uk/docs/guides/deployment/


### Running Epidur.io in development
* to create seed data with patients and locations in Labour Ward:

`python manage.py create_dev_labour_ward`
