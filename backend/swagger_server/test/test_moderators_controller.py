# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestModeratorsController(BaseTestCase):
    """ModeratorsController integration test stubs"""

    def test_add_mod(self):
        """Test case for add_mod

        Add a new Moderator
        """
        headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhRGFtZXJvbjg5Iiwic2NvcGUiOlsibG9naW46dXNlciJdfQ.fvv3vL1d7I0KlL4jOkrtnIwOFoW9qaS6iy_pcEospZc'
}
        response = self.client.open(
            '/api/v3/c/{community_name}/mod/{username}'.format(community_name='funny', username='tv'),
            method='POST',headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_moderators_by_community_name(self):
        """Test case for get_moderators_by_community_name

        Get mods by community
        """
        response = self.client.open(
            '/api/v3/c/{community_name}/mod'.format(community_name='funny'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remove_mod(self):
        """Test case for remove_mod

        Remove as Moderator
        """
        headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhRGFtZXJvbjg5Iiwic2NvcGUiOlsibG9naW46dXNlciJdfQ.fvv3vL1d7I0KlL4jOkrtnIwOFoW9qaS6iy_pcEospZc'
    }
        response = self.client.open(
            '/api/v3/c/{community_name}/mod/{username}'.format(community_name='funny',username='tv'),
            method='DELETE',headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    # unittest.main()
    test_cases=["test_add_mod","test_get_moderators_by_community_name","test_remove_mod"]
    suite = unittest.TestSuite(map(TestModeratorsController, test_cases))
    unittest.TextTestRunner().run(suite)
