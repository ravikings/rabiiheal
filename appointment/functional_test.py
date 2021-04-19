import unittest
import sqlite3
from unittest import result, mock
import requests
from getpass import getpass



# class DjangoTest(unittest.TestCase):

#     def test_handing_page_for_unatorized_user(self):
#         url = requests.get('http://127.0.0.1:8000/api/v1/')
#         response = url.status_code
#         self.assertEqual(response, 403)


class DjangoTestLogin(unittest.TestCase):

    # def test_handing_page_for_unatorized_user(self):
    #     url = requests.post('http://127.0.0.1:8000/api/v1/dj-rest-auth/login/', {"username": "admin","email": "","password": "admin"})
    #     response = url.status_code
    #     head = url.headers['content-type']
    #     data = url.json()
    #     self.assertEqual(response, 200)
    #     self.assertEqual(head, 'application/json')

    #     self.assertEqual(data, {'key': 'f55e39b05eb017bb880d4617355b5f784b53859d'})


    def session(self):
        with requests.Session() as session:
            session.auth = ('admin', getpass())
            response = session.get('http://127.0.0.1:8000/api/v1/')
            self.assertEqual(response.headers, 'application')




if __name__ == '__main__':
    unittest.main()
