# -*- coding: utf-8 -*-

from django.forms.models import modelform_factory
from datetimewidget.widgets import DateWidget


def fun_date_widget(x):
    date_options = {
        'bootstrap_version': 3,
        'attrs': {'id': 'id' + x},
        'options': {'format': 'yyyy-mm-dd'}
    }

    date_widget = DateWidget(**date_options)
    return date_widget


def get_form(cur_model, fields):
    all_date_fields = [k for k, v in fields.items() if v == "date"]
    widgets_dict = {x: fun_date_widget(x) for x in all_date_fields}
    form = modelform_factory(cur_model, widgets=widgets_dict)
    return form