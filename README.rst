=======
Workers
=======

Workers is a simple Django test app. Application dynamically creates models from yaml file. You can add your yaml file to project directory (along with your manage.py) and name it "models.yaml". Without that file provided default "users.yaml" file will be used.


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
