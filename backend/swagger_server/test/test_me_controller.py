# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase

token = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJLMXJBX2FBIiwic2NvcGUiOlsibG9naW46dXNlciJdfQ.xQ3oME5q2gQxEMmKnLJv9cvondmZ05UxuB7mN0Z0Syk'}

class TestMeController(BaseTestCase):
    """MeController integration test stubs"""

    def test_block_user(self):
        """Test case for block_user

        Block a user
        """
        response = self.client.open(
            '/api/v3/me/block/{username}'.format(username='tv'),
            method='POST',headers=token)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_clear_history(self):
        """Test case for clear_history

        Clear history
        """
        response = self.client.open(
            '/api/v3/me/history/clear', 
            method='GET',headers = token,)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_follow_user(self):
        """Test case for delete_follow_user

        Delete a followed user
        """
        response = self.client.open(
            '/api/v3/me/follow/{username}'.format(username='reaper_113'), headers = token,
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_follow_user(self):
        """Test case for follow_user

        Follow a user
        """
        response = self.client.open(
            '/api/v3/me/follow/{username}'.format(username='reaper_113'), headers = token,
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_blocked_list(self):
        """Test case for get_blocked_list

        Get blocked list
        """
        response = self.client.open(
            '/api/v3/me/block', headers = token,
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_following_list(self):
        """Test case for get_following_list

        Get following list
        """
        response = self.client.open(
            '/api/v3/me/follow', headers = token,
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_history(self):
        """Test case for get_history

        Get history
        """
        response = self.client.open(
            '/api/v3/me/history', headers = token,
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_saved_comments_list(self):
        """Test case for get_saved_comments_list

        Get saved comments list
        """
        response = self.client.open(
            '/api/v3/me/savedComments', headers = token,
            method='GET')
        self.assert200(response, 
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_saved_posts_list(self):
        """Test case for get_saved_posts_list

        Get saved posts list
        """
        response = self.client.open(
            '/api/v3/me/savedPosts', headers = token,
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_subscribed_communities(self):
        """Test case for get_subscribed_communities

        Get subscribed communities
        """
        response = self.client.open(
            '/api/v3/me/subscribedCommunities', headers = token,
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_save_comment(self):
        """Test case for save_comment

        Saves the comment
        """
        response = self.client.open(
            '/api/v3/me/savedComments/{commentID}'.format(commentID=34), headers = token,
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_save_post(self):
        """Test case for save_post

        Saves the post
        """
        response = self.client.open(
            '/api/v3/me/savedPosts/{postID}'.format(postID=200), headers = token,
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_unblock_user(self):
        """Test case for unblock_user

        Unblock a user
        """
        response = self.client.open(
            '/api/v3/me/block/{username}'.format(username='reaper_113'), headers = token,
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_unsave_comment(self):
        """Test case for unsave_comment

        Unsaves the comment
        """
        response = self.client.open(
            '/api/v3/me/savedComments/{commentID}'.format(commentID=34), headers = token,
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_unsave_post(self):
        """Test case for unsave_post

        Unsaves the post
        """
        response = self.client.open(
            '/api/v3/me/savedPosts/{postID}'.format(postID=200), headers = token,
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    # test_cases=["test_unsave_post"]
    # suite = unittest.TestSuite(map(TestMeController, test_cases))
    # unittest.TextTestRunner().run(suite)
    unittest.main()