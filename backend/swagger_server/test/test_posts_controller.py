# coding: utf-8

from __future__ import absolute_import
import datetime
from flask import json
from six import BytesIO

from swagger_server.models.posts_db import PostsDb  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPostsController(BaseTestCase):
    """PostsController integration test stubs"""

    def test_create_post(self):
        """Test case for create_post

        Create Post
        """
        headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0VXNlciIsInNjb3BlIjpbImxvZ2luOnVzZXIiXX0.ryzQH_7QE2-iH6qqQME-tz9eG4CQvJLfLD3ME1nTz0g'
}
        body = PostsDb(None,"testPost3","test content3",3,5,datetime.datetime(2013,4,5,6,21,5),9,0)
        response = self.client.open(
            '/api/v3/p/create',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

#     def test_delete_post(self):
#         """Test case for delete_post

#         Delete post
#         """
#         headers = {
#     'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJLMXJBX2FBIiwic2NvcGUiOlsibG9naW46dXNlciJdfQ.xQ3oME5q2gQxEMmKnLJv9cvondmZ05UxuB7mN0Z0Syk'
# }
#         response = self.client.open(
#             '/api/v3/p/{post_id}'.format(post_id=228),
#             method='DELETE',headers=headers)
#         self.assert200(response,
#                        'Response body is : ' + response.data.decode('utf-8'))

    def test_get_post_by_id(self):
        """Test case for get_post_by_id

        Get post by id
        """
        response = self.client.open(
            '/api/v3/p/{post_id}'.format(post_id=200),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_post(self):
        """Test case for update_post

        Update post
        """
        headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJLMXJBX2FBIiwic2NvcGUiOlsibG9naW46dXNlciJdfQ.xQ3oME5q2gQxEMmKnLJv9cvondmZ05UxuB7mN0Z0Syk'
}
        body = PostsDb(None,"testupdatedPost2","test content2",3,5,datetime.datetime(2013,4,5,6,21,5),9,0)
        response = self.client.open(
            '/api/v3/p/{post_id}'.format(post_id=229),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
    # test_cases=["test_update_post"]
    # suite = unittest.TestSuite(map(TestPostsController, test_cases))
    # unittest.TextTestRunner().run(suite)
    
    
