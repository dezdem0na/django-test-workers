# -*- coding: utf-8 -*-

import os

from django.db import models
from django.contrib import admin
import yaml

from workers.utils import django_ftypes


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def open_yaml(fname):
    """Open YAML file.

    Args:
        fname (str): Path to a file.
    """
    try:
        with open(fname, "r") as filename:
            stream = filename
            yaml_models = yaml.safe_load_all(stream)
            process_yaml(yaml_models)
    except IOError, exc:
        print "Cannot open file:", exc
    except yaml.YAMLError, exc:
        print "YAMLError:", exc


def process_yaml(yaml_models):
    """Create Model from each YAML document.

    Args:
        yaml_models(generator): YAML's load method's result. Returns YAML documents.
    """
    for doc in yaml_models:
        create_model(doc)


def create_model(description):
    """Dynamically create Django models.

    Args:
        description (dict): A YAML document that contains a description
            of a single Model. YAML stream is a collection of zero or
            more documents. An empty stream contains no documents.
            Documents are separated with ---.
    """
    name = description.keys()[0]
    fields = description.values()[0][1].get('fields')

    class Meta:
        app_label = 'workers'

    attrs = {
        '__module__': __name__,
        'Meta': Meta,
    }

    for elems in fields:
        if django_ftypes(elems.get('type')) is not None:
            attrs[elems.get('title')] = django_ftypes(elems.get('type'))

    model = type(name, (models.Model,), attrs)
    admin.site.register(model)


ymlfile = BASE_DIR+'/workers/yaml/users.yaml'
open_yaml(ymlfile)