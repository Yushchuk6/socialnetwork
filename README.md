# Social network

### Required dependencies:
```
django
djangorestframework
djangorestframework-simplejwt
pandas
```
### API interface:
```
POST 	api/register/
POST 	api/token/
POST	api/token/refresh/
GET     api/posts/
POST 	api/posts/
PUT 	api/posts/<title>/like
DELETE	api/posts/<title>/like
GET 	api/analytics/
GET     api/<username>/
```