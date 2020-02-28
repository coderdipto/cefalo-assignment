# Python Developer Assignment
### System Info
Python verison : 3.7.4

PIP version : 20.0.2
***
### Instruction to run the program

Install requirements

```python
pip install -r requirements.txt
```

Migrate database

```python
python manage.py migrate
```

Start parsing
```python
python manage.py parse
```
Update average rating and rating givers
```python
python manage.py ratings
```

Start Server
```python
python manage.py runserver
```
***
### API Documentation
LIST API
```text
Request Type: GET
Example URL: http://localhost:8000/movies/?limit=20&offset=0
HEADERS: {"Content-Type": "application/json"}
```
DETAIL API
```text
Request Type: GET
Example URL: http://localhost:8000/movies/1/
HEADERS: {"Content-Type": "application/json"}
```
CREATE API
```text
Request Type: POST
Example URL: http://localhost:8000/movies/
HEADERS: {"Content-Type": "application/json"}
BODY = {
    "title": "Parasite",
    "year": "2019",
    "awards": "4",
    "nominations": "6",
    "average_rating": 1,
    "rating_givers": 2,
    "info":""
}
```
UPDATE API
```text
Request Type: PUT
Example URL: http://localhost:8000/movies/1/
HEADERS: {"Content-Type": "application/json"}
BODY = {
    "title": "Judy Updated"
}
```
DELETE API
```text
Request Type: DELETE
Example URL: http://localhost:8000/movies/1/
HEADERS: {"Content-Type": "application/json"}
```