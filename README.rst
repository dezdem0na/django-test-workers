=======
Workers
=======

Workers is a simple Django test app. Application dynamically creates models from yaml file. 


Requirements:
-django-datetime-widget (https://github.com/asaglimbeni/django-datetime-widget),
-PyYAML,

----------------------------
For usage along with MongoDB:

Requirements:
-django-mongodb-engine,
-djangotoolbox,
-pymongo,
-django-nonrel(https://github.com/django-nonrel)

DATABASES = {
     'default': {
         'ENGINE': 'django_mongodb_engine',
         'NAME': 'dbname',
        # 'USER': '',
        # 'PASSWORD': '',
        # 'HOST': 'localhost',
        # 'PORT': 27017,
    }
}
