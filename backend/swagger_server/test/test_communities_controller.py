# coding: utf-8

from __future__ import absolute_import
import datetime
from flask import json
from six import BytesIO

from swagger_server.models.communities import Communities  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase

headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJLMXJBX2FBIiwic2NvcGUiOlsibG9naW46dXNlciJdfQ.xQ3oME5q2gQxEMmKnLJv9cvondmZ05UxuB7mN0Z0Syk'}


class TestCommunitiesController(BaseTestCase):
    """CommunitiesController integration test stubs"""

    def test_create_community(self):
        """Test case for create_community

        Create community
        """
        body = Communities(None,"newCommunty?","for testing",datetime.datetime(2000,5,14,13,20,50))
        response = self.client.open(
            '/api/v3/c/create',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))



    def test_get_community_by_name(self):
        """Test case for get_community_by_name

        Get community by name
        """
        
        response = self.client.open(
            '/api/v3/c/{community_name}'.format(community_name='newCommunty%3F'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        print(response.data.decode('utf-8'))
        
# email is required
#     def test_update_community(self):
#         """Test case for update_community

#         Update community
#         """
#         body = Communities(None,"newCommunty?","for testing22",datetime.datetime(2000,5,14,13,20,50))
#         headers = {
#     'Authorization': 'Bearer <your_access_token_here>'
# }
#         response = self.client.open(
#             '/api/v3/c/{community_name}'.format(community_name='newCommunty%3F'),
#             method='PUT',
#             data=json.dumps(body),
#             content_type='application/json',headers=headers)
#         self.assert200(response,
#                        'Response body is : ' + response.data.decode('utf-8'))


# user not found
#     def test_delete_community(self):
#         """Test case for delete_community

#         Delete community
#         """
#         headers = {
#     'Authorization': 'Bearer <your_access_token_here>'
# }
#         response = self.client.open(
#             '/api/v3/c/{community_name}'.format(community_name='newCommunty%3F'),
#             method='DELETE',headers=headers)
#         self.assert200(response,
#                        'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
