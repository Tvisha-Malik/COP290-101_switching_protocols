# coding: utf-8

from __future__ import absolute_import
import datetime
from flask import json
from six import BytesIO

from swagger_server.models.comment_votes import CommentVotes  # noqa: E501
from swagger_server.models.votes import Votes  # noqa: E501
from swagger_server.test import BaseTestCase


class TestVotesController(BaseTestCase):
    """VotesController integration test stubs"""

    def test_delete_comment_vote(self):
        """Test case for delete_comment_vote

        Delete Comment vote
        """
        headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0VXNlciIsInNjb3BlIjpbImxvZ2luOnVzZXIiXX0.ryzQH_7QE2-iH6qqQME-tz9eG4CQvJLfLD3ME1nTz0g'
}
        response = self.client.open(
            '/api/v3/vc/{commentID}/{username}'.format(commentID=90, username='tv'),
            method='DELETE',headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_post_vote(self):
        """Test case for delete_post_vote

        Delete post vote
        """
        headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0VXNlciIsInNjb3BlIjpbImxvZ2luOnVzZXIiXX0.ryzQH_7QE2-iH6qqQME-tz9eG4CQvJLfLD3ME1nTz0g'
}
        response = self.client.open(
            '/api/v3/v/{postID}/{username}'.format(postID=200, username='tv'),
            method='DELETE',headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_vote_by_comment_id(self):
        """Test case for get_vote_by_comment_id

        Get comment vote by id
        """
        
        response = self.client.open(
            '/api/v3/vc/{commentID}/{username}'.format(commentID=90, username='K1rA_aA'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_vote_by_id(self):
        """Test case for get_vote_by_id

        Get post vote by id
        """
        response = self.client.open(
            '/api/v3/v/{postID}/{username}'.format(postID=144, username='A_A_RON4'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        

    def test_update_comment_vote_by_id(self):
        """Test case for update_comment_vote_by_id

        Update vote
        """
        headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0VXNlciIsInNjb3BlIjpbImxvZ2luOnVzZXIiXX0.ryzQH_7QE2-iH6qqQME-tz9eG4CQvJLfLD3ME1nTz0g'
}
        body = CommentVotes(None,5,3,True,datetime.datetime(2000,7,8,3,4,5))
        response = self.client.open(
            '/api/v3/vc/{commentID}/{username}'.format(commentID=90, username='tv'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_post_vote_by_id(self):
        """Test case for update_post_vote_by_id

        Update vote
        """
        headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0VXNlciIsInNjb3BlIjpbImxvZ2luOnVzZXIiXX0.ryzQH_7QE2-iH6qqQME-tz9eG4CQvJLfLD3ME1nTz0g'
}
        body = Votes(None,50,200,True,datetime.datetime(2000,7,8,3,4,5))
        response = self.client.open(
            '/api/v3/v/{postID}/{username}'.format(postID=200, username='tv'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    # unittest.main()
    test_cases=["test_get_vote_by_id","test_get_vote_by_comment_id","test_update_post_vote_by_id","test_update_comment_vote_by_id","test_delete_comment_vote","test_delete_post_vote"]
    suite = unittest.TestSuite(map(TestVotesController, test_cases))
    unittest.TextTestRunner().run(suite)

