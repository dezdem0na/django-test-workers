# -*- coding: utf-8 -*-

import os

import django.utils.unittest as unittest2
from django.core.urlresolvers import reverse
from django.test import Client, RequestFactory
from pymongo import MongoClient
from django.db import models
import yaml

from workers.models import open_yaml
from workers.utils import get_all_models, get_model_fields
from workers.views import display


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class WorkersTest(unittest2.TestCase):
    def setUp(self):
        self.mdl = get_all_models().itervalues().next()

    def test_connection_alive(self):
        client = MongoClient()
        self.assertEquals(client.alive(), True)

    def test_index(self):
        c = Client()
        response = c.get('/workers/')
        self.assertEquals(response.status_code, 200)
        self.assertTrue('names_list' in response.context)

    def test_process_yaml_io(self):
        self.assertRaises(IOError, open_yaml(""))

    def test_process_yaml_err(self):
        self.assertRaises(yaml.YAMLError, open_yaml(os.path.join(BASE_DIR, 'workers/yaml/test_users.yaml')))

    def test_model_creation(self):
        self.assertTrue(isinstance(self.mdl, models.base.ModelBase))

    def test_display_view(self):
        c = Client()
        name = self.mdl.__name__
        url = reverse('workers:display', args=[name])
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_display_view_404(self):
        c = Client()
        name = 'abcdefghijklmnoprsth'
        url = reverse('workers:display', args=[name])
        response = c.get(url)
        self.assertEqual(response.status_code, 404)


class SimpleTest(unittest2.TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.mdl = get_all_models().itervalues().next()
        kwargs = {k: 0 for k, v in get_model_fields(self.mdl).items()}
        self.mod = self.mdl.objects.create(**kwargs)

    def test_display(self):
        request = self.factory.get('/workers/'+self.mdl.__name__)
        request.mod = self.mod
        response = display(request, self.mdl.__name__)
        self.assertEqual(response.status_code, 200)