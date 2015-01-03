flask-skeleton
==============

A simple re-usable application skeleton.  This skeleton is for us with the fantastic app scoffolding library from @krak3n, ``facio``.
To use this skeleton head over to the ``facio`` docs [here](https://facio.readthedocs.org/en/latest/index.html)

Quickstart
==========

```
$ sudo easy_install facio
```

or

```
$ sudo pip install facio
```

```
$EDITOR ~/.facio.cfg
```

Add the following lines

```
[template]
flask = git+git@github.com:mikeywaites/flask-skeleton.git

[files]
copy_ignore = .env,*.pyc,.git
render_ignore = .coverage,*.ico
```

With facio installed we can now create a brand new flask app using the flask-skeleton template.

```
$ facio YOUR_PROJECT_NAME -t flask --vars PROJECT_NAME=YOUR_PROJECT_NAME,DOCKER_USER=YOUR_DOCKER_HUB_USER
```
and thats it.  You'll notice our folders have been renamed and all our package imports have been correctly set to the projectname we set above :)

Variables
=========

PROJECT_NAME = used to renmae the main directory containing our app.  This will form our python package import name later. **see setup.py**
DOCKER_USER = used when creating fugu scripts for managing docker. [here](https://github.com/mattes/fugu)


Installing docker & fugu
===========================

For users on OSX that haven't already installed boot2docker, head over to [dockers instillation docs](https://docs.docker.com/installation/mac/).

Once you have docker installed an running next you'll need fugu.  Fugu is a great tool for defining re-usable docker commands and IMO is much nicer than the alternative, more widely talked about, fig.

You can find [instillation docs for fugu here](https://github.com/mattes/fugu)


Runnning flask inside a docker container
========================================

Once everything is installed its time to get the app running. First step is to create the db container you will use with the app

`$ fugu run db`

You can test the db by connecting to it like so

`$ fugu exec db psql`

This will generate a new db container we can link from our app container using a database called postgres and the default postgres user.

`$ fugu run app`

This should start our app container in interactive mode with the familiar sight of flasks app logging in reloading mode.  now simply grab the boot2docker ip by running:

`$ boot2docker ip` and open this in your browser on port 5000:

`http://192.168.59.103:5000/`


You should now see a very basic json example being outputted from the uri /v1/


Generating Migrations
===========================

As an example, a basic User model is included for you.  Feel free to update or remove this.  Once you have some models you would like to persist to the db container we can auto-generate
some migrations.  Firstly ensure that all models are imported into models.__init__

This ensures that the models are discovered early on and also helps to make life easier when importing.

`$ fugu run dev python manage.py db migrate -m 'initial user schema'`

As alembic suggests you should always check the autogenerated migrations before you apply them.  To apply the migrations run:

`$ fugu run dev python manage.py db upgrade`

As you can see, everything passed after the word dev is handed over to docker as the command to run.


Running manage.py commands
===========================

Flask-Skeleton uses Flask-Script to enable django-esq manage.py commands.  These can be running via docker:

`$ fugu run dev python manage.py FOO`
`$ fugu run app python manage.py BAR`

Run `$ fugu run app python manage.py` to see a list of the commands available out of the box
