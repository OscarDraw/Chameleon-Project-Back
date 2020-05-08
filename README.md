# Chameleon Project

This if the backend of the chameleon project, based on Python (django+djangorestframework)

### How to use

* Clone the repo
* Install in your machine the pipenv package
* execute the following line in the terminal
~~~
pipenv install
~~~

And there you are, the project is installed.

## How to Run

Execute 
~~~
pipenv run python manage.py runserver
~~~

or execute
~~~
pipenv shell
~~~
and then 
~~~
python manage.py runserver
~~~

Personally I recommend the first way, because it charges all the environment each time you execute the command.


## Files

Django creates some files:
* **chamaleon/** Here are all the main files of the django project
* **manage.py** This is one of the main files of the django project, without this file we could run or execute any django command.

Another files:
* **Pipfile** is a Yaml like file, where are listed (human readable) the required packages to run the project and make it work
* **Pipfile.lock** Here are listed the dependencies of each package listed in the *Pipfile*, but here the lines has got the hashes and all that stuff. THIS FILE IS AUTOGENERATED DON'T TOO MUCH WORRY ABOUT IT