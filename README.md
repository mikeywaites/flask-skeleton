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
