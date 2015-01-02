#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import environ

from flask import Flask

from {{PROJECT_NAME}}.api.views import api_mod


def create_app(config_name='DEV'):
    """Flask app factory.

    Useage::

        from {{PROJECT_NAME}}.app import create_app
        def run():
            app = create_app(config_name='STAGE')
            app.run(host='0.0.0.0', port=5000, debug=app.debug)

        if __name__=="__main__":
            run()

    :param config_name: manually provide the name of the config object to use
        when creating the :py:class:``flask.Flask`` instance.  Defaults to
        os.environ['{{PROJECT_NAME}}_CONFIG']

    :rtype: :py:class:``flask.Flask``
    :returns: A new :py:class:``flask.Flask`` application instance
    """

    app = Flask(__name__)

    if config_name is not None:
        environ['{{PROJECT_NAME}}_CONFIG'] = config_name

    app.template_folder = app.config.get('TEMPLATE_FOLDER', 'templates')
    app.register_blueprint(api_mod, url_prefix='/v1')

    return app
