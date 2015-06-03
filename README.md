# multiple
Django multiple database switching tests

# Setup

First, you need to clone this repo:

~~~
git clone http://github.com/MikeVelazcoMtz/multiple.git
~~~

And then, install the requirements:

~~~
pip install -r requirements.txt
~~~

After that, you need to run the `makemigrations` and `migrate` for each database alias:

~~~
# this is for the project (not for the database)
python manage.py makemigrations
.
.
.
.
.
.
python manage.py migrate --database default
.
.
.
.
.
.
python manage.py migrate --database eureka
.
.
.
.
.
.
~~~

And finally, run your server:

~~~
python manage.py runserver
~~~
