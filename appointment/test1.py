import requests
from getpass import getpass

# By using a context manager, you can ensure the resources used by
# the session will be released after use
with requests.Session() as session:
    session.post('http://127.0.0.1:8000/api/v1/dj-rest-auth/login/', {"username": "admin","email": "","password": "admin"})

    # Instead of requests.get(), you'll use session.get()
    response = session.get('http://127.0.0.1:8000/api/v1/')
    data = response.json()
# You can inspect the response just like you did before
#print(response.headers)
print(response.json())


