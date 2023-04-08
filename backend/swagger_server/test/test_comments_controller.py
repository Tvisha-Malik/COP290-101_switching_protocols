# coding: utf-8

from __future__ import absolute_import
import datetime
from flask import json
from six import BytesIO

from swagger_server.models.comments import Comments  # noqa: E501
from swagger_server.test import BaseTestCase

headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJLMXJBX2FBIiwic2NvcGUiOlsibG9naW46dXNlciJdfQ.xQ3oME5q2gQxEMmKnLJv9cvondmZ05UxuB7mN0Z0Syk'}


class TestCommentsController(BaseTestCase):
    """CommentsController integration test stubs"""

    def test_create_comment(self):
        """Test case for create_comment

        Add comment
        """
        body = Comments(205,None,"this",29,0,None,7,9)
 
        response = self.client.open(
            '/api/v3/comments',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_comment(self):
        """Test case for delete_comment

        Delete user
        """
        response = self.client.open(
            '/api/v3/comments/{commentID}'.format(commentID=70),
            method='DELETE',headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_comment_by_id(self):
        """Test case for get_comment_by_id

        Get comment by comment id
        """
        response = self.client.open(
            '/api/v3/comments/{commentID}'.format(commentID=79),
            method='GET',headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        print(response.data.decode('utf-8'))

    def test_update_comment(self):
        """Test case for update_comment

        Update cooment
        """
        body = Comments(205,None,"this",29,0,datetime.datetime(2006,7,9,8,20,10),7,9)
        
        response = self.client.open(
            '/api/v3/comments/{commentID}'.format(commentID=89),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
