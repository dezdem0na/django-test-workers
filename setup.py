import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-test-workers',
    version='0.1',
    packages=['workers'],
    include_package_data=True,
    license='GNU License',  
    description='A simple Django test app.',
    long_description=README,
    author='Natalia Reshetnikova',
    author_email='natalie.reshetnikova@gmail.com',
    url='github.com/dezdem0na/n_application',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: GNU License', 
        'Operating System :: OS Linux/Ubuntu',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
	'django-datetime-widget<=0.9.3',
	'PyYAML<=3.11',
	'django<=1.6.8',
    ],
)
