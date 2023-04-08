# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO
import datetime
from swagger_server.models.notifications import Notifications  # noqa: E501
from swagger_server.models.preferences import Preferences  # noqa: E501
from swagger_server.models.u_login_body import ULoginBody  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_create_user(self):
        """Test case for create_user

        Create user
        """
        body = User(None,"testUser2","test2Email@iitd.ac.in","test2Password",datetime.datetime(2004,7,8,3,4,2),datetime.datetime(2019,7,8,3,4,2),0,None,89,80)
        response = self.client.open(
            '/api/v3/u/create',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user(self):
        """Test case for delete_user

        Delete user
        """
        headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0VXNlciIsInNjb3BlIjpbImxvZ2luOnVzZXIiXX0.ryzQH_7QE2-iH6qqQME-tz9eG4CQvJLfLD3ME1nTz0g'
}
        response = self.client.open(
            '/api/v3/u/{username}'.format(username='testUser2'),
            method='DELETE',headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    # def test_forgot_password(self):
    #     """Test case for forgot_password

    #     Sends recovery email
    #     """
    #     query_string = [('username', 'username_example'),
    #                     ('email', 'email_example')]
    #     response = self.client.open(
    #         '/api/v3/u/login/forgotPassword',
    #         method='GET',
    #         query_string=query_string)
    #     self.assert200(response,
    #                    'Response body is : ' + response.data.decode('utf-8'))
        

    def test_get_user_by_name(self):
        """Test case for get_user_by_name

        Get user by user name
        """
        response = self.client.open(
            '/api/v3/u/{username}'.format(username='visha'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_notifications(self):
        """Test case for get_user_notifications

        Get user notifications
        """
        headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0VXNlciIsInNjb3BlIjpbImxvZ2luOnVzZXIiXX0.ryzQH_7QE2-iH6qqQME-tz9eG4CQvJLfLD3ME1nTz0g'
}
        response = self.client.open(
            '/api/v3/u/{username}/notif'.format(username='testUser'),
            method='GET',headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_preferences(self):
        """Test case for get_user_preferences

        Get user preferences
        """
        headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0VXNlciIsInNjb3BlIjpbImxvZ2luOnVzZXIiXX0.ryzQH_7QE2-iH6qqQME-tz9eG4CQvJLfLD3ME1nTz0g'
}
        response = self.client.open(
            '/api/v3/u/{username}/pref'.format(username='visha'),
            method='GET',headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_login_user(self):
        """Test case for login_user

        Logs user into the system
        """
        body = ULoginBody("K1rA_aA","9420pq6q")
        response = self.client.open(
            '/api/v3/u/login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        print('response'+response.data.decode('utf-8'))

    def test_update_user(self):
        """Test case for update_user

        Update user
        """
        body = User(None,"testUser","testEmailupdate@iitd.ac.in","testPassword",datetime.datetime(2004,7,8,3,4,2),datetime.datetime(2019,7,8,3,4,2),1,None,89,80)
        headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0VXNlciIsInNjb3BlIjpbImxvZ2luOnVzZXIiXX0.ryzQH_7QE2-iH6qqQME-tz9eG4CQvJLfLD3ME1nTz0g'
}
        response = self.client.open(
            '/api/v3/u/{username}'.format(username='testUser'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user_preferences(self):
        """Test case for update_user_preferences

        Update user preferences
        """
        body = Preferences(None,"Old",datetime.datetime(2000,5,14,13,20,50),"New","Old","English")
        headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0VXNlciIsInNjb3BlIjpbImxvZ2luOnVzZXIiXX0.ryzQH_7QE2-iH6qqQME-tz9eG4CQvJLfLD3ME1nTz0g'
}
        response = self.client.open(
            '/api/v3/u/{username}/pref'.format(username='testUser'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    test_cases=["test_login_user"]
    suite = unittest.TestSuite(map(TestUserController, test_cases))
    unittest.TextTestRunner().run(suite)
    # unittest.main()
