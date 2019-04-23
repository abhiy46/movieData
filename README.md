Movie API

An API interface to search and find movies by names, directors and genres.

It uses data from imdb.json

## Setting up project and initializing data
```
# create a virtualenv 
virtualenv env_movie
sourcepath>env_movie\scritps\activate
pip install -r reuqirements.txt
./manage.py migrate
./manage.py runserver
./manage.py populate_movies
```


API request examples

base API url
https://secure-woodland-10945.herokuapp.com/api/movies

header : user base authentication - user name and password

filter by name (full text search)
https://secure-woodland-10945.herokuapp.com/api/movies?name=wizard

filter by movie name and director name
https://secure-woodland-10945.herokuapp.com/api/movies?name=wizard&director=victor

filter by genre name
https://secure-woodland-10945.herokuapp.com/api/movies?genre=family
