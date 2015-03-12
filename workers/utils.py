# -*- coding: utf-8 -*-

import datetime

from django.contrib.contenttypes.models import ContentType
from django.db import models


def django_ftypes(ft):
    """Return an appropriate Django field type.

    Args:
        ft (str): Field type. Types can be - 'char', 'int', 'date'.
    """
    return {
        'char': models.CharField(max_length=200),
        'int': models.IntegerField(default=0),
        'date': models.DateField(default=datetime.date.today())
    }.get(ft, None)


def html_types(ft):
    """Return an appropriate HTML5 field type.

    Args:
        ft (str): Field type. Types can be - 'CharField', 'IntegerField', 'DateField'.
    """
    return {
        'CharField': 'text',
        'IntegerField': 'number',
        'DateField': 'date'
    }.get(ft, None)


def get_all_models():
    """Return a dictionary of models with names as keys."""
    all_models = dict()
    for ctw in ContentType.objects.filter(app_label='workers'):
        m = ctw.model_class()
        all_models[m.__name__] = m
    return all_models


def get_model_by_name(name):
    """Return a model.

    Args:
        name (str): Model's name.
    """
    all_models = get_all_models()
    model = all_models.get(name)
    return model


def get_model_fields(model):
    """Return a dictionary of model's fields except an auto field with HTML5 types as keys.

    Args:
        model (django.db.models.base.ModelBase): Django Model.
    """
    fields = dict()
    fnames = filter(lambda s: not s == 'id', model._meta.get_all_field_names())
    for fname in fnames:
        ftype = type(model._meta.get_field(fname)).__name__
        fields[fname] = html_types(ftype)
    return fields