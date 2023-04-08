# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BlockUsers(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, block_id: int=None, blocked_user: int=None, blocked_by: int=None, time: datetime=None):  # noqa: E501
        """BlockUsers - a model defined in Swagger

        :param block_id: The block_id of this BlockUsers.  # noqa: E501
        :type block_id: int
        :param blocked_user: The blocked_user of this BlockUsers.  # noqa: E501
        :type blocked_user: int
        :param blocked_by: The blocked_by of this BlockUsers.  # noqa: E501
        :type blocked_by: int
        :param time: The time of this BlockUsers.  # noqa: E501
        :type time: datetime
        """
        self.swagger_types = {
            'block_id': int,
            'blocked_user': int,
            'blocked_by': int,
            'time': datetime
        }

        self.attribute_map = {
            'block_id': 'blockID',
            'blocked_user': 'blockedUser',
            'blocked_by': 'blockedBy',
            'time': 'time'
        }
        self._block_id = block_id
        self._blocked_user = blocked_user
        self._blocked_by = blocked_by
        self._time = time

    @classmethod
    def from_dict(cls, dikt) -> 'BlockUsers':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BlockUsers of this BlockUsers.  # noqa: E501
        :rtype: BlockUsers
        """
        return util.deserialize_model(dikt, cls)

    @property
    def block_id(self) -> int:
        """Gets the block_id of this BlockUsers.


        :return: The block_id of this BlockUsers.
        :rtype: int
        """
        return self._block_id

    @block_id.setter
    def block_id(self, block_id: int):
        """Sets the block_id of this BlockUsers.


        :param block_id: The block_id of this BlockUsers.
        :type block_id: int
        """

        self._block_id = block_id

    @property
    def blocked_user(self) -> int:
        """Gets the blocked_user of this BlockUsers.


        :return: The blocked_user of this BlockUsers.
        :rtype: int
        """
        return self._blocked_user

    @blocked_user.setter
    def blocked_user(self, blocked_user: int):
        """Sets the blocked_user of this BlockUsers.


        :param blocked_user: The blocked_user of this BlockUsers.
        :type blocked_user: int
        """

        self._blocked_user = blocked_user

    @property
    def blocked_by(self) -> int:
        """Gets the blocked_by of this BlockUsers.


        :return: The blocked_by of this BlockUsers.
        :rtype: int
        """
        return self._blocked_by

    @blocked_by.setter
    def blocked_by(self, blocked_by: int):
        """Sets the blocked_by of this BlockUsers.


        :param blocked_by: The blocked_by of this BlockUsers.
        :type blocked_by: int
        """

        self._blocked_by = blocked_by

    @property
    def time(self) -> datetime:
        """Gets the time of this BlockUsers.


        :return: The time of this BlockUsers.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time: datetime):
        """Sets the time of this BlockUsers.


        :param time: The time of this BlockUsers.
        :type time: datetime
        """

        self._time = time
