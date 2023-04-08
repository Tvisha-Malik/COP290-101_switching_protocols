# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Messages(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, message_id: int=None, content: str=None, from_user_id: int=None, to_user_id: int=None, time_sent: datetime=None):  # noqa: E501
        """Messages - a model defined in Swagger

        :param message_id: The message_id of this Messages.  # noqa: E501
        :type message_id: int
        :param content: The content of this Messages.  # noqa: E501
        :type content: str
        :param from_user_id: The from_user_id of this Messages.  # noqa: E501
        :type from_user_id: int
        :param to_user_id: The to_user_id of this Messages.  # noqa: E501
        :type to_user_id: int
        :param time_sent: The time_sent of this Messages.  # noqa: E501
        :type time_sent: datetime
        """
        self.swagger_types = {
            'message_id': int,
            'content': str,
            'from_user_id': int,
            'to_user_id': int,
            'time_sent': datetime
        }

        self.attribute_map = {
            'message_id': 'messageID',
            'content': 'content',
            'from_user_id': 'fromUserID',
            'to_user_id': 'toUserID',
            'time_sent': 'timeSent'
        }
        self._message_id = message_id
        self._content = content
        self._from_user_id = from_user_id
        self._to_user_id = to_user_id
        self._time_sent = time_sent

    @classmethod
    def from_dict(cls, dikt) -> 'Messages':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Messages of this Messages.  # noqa: E501
        :rtype: Messages
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message_id(self) -> int:
        """Gets the message_id of this Messages.


        :return: The message_id of this Messages.
        :rtype: int
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id: int):
        """Sets the message_id of this Messages.


        :param message_id: The message_id of this Messages.
        :type message_id: int
        """

        self._message_id = message_id

    @property
    def content(self) -> str:
        """Gets the content of this Messages.


        :return: The content of this Messages.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content: str):
        """Sets the content of this Messages.


        :param content: The content of this Messages.
        :type content: str
        """

        self._content = content

    @property
    def from_user_id(self) -> int:
        """Gets the from_user_id of this Messages.


        :return: The from_user_id of this Messages.
        :rtype: int
        """
        return self._from_user_id

    @from_user_id.setter
    def from_user_id(self, from_user_id: int):
        """Sets the from_user_id of this Messages.


        :param from_user_id: The from_user_id of this Messages.
        :type from_user_id: int
        """

        self._from_user_id = from_user_id

    @property
    def to_user_id(self) -> int:
        """Gets the to_user_id of this Messages.


        :return: The to_user_id of this Messages.
        :rtype: int
        """
        return self._to_user_id

    @to_user_id.setter
    def to_user_id(self, to_user_id: int):
        """Sets the to_user_id of this Messages.


        :param to_user_id: The to_user_id of this Messages.
        :type to_user_id: int
        """

        self._to_user_id = to_user_id

    @property
    def time_sent(self) -> datetime:
        """Gets the time_sent of this Messages.


        :return: The time_sent of this Messages.
        :rtype: datetime
        """
        return self._time_sent

    @time_sent.setter
    def time_sent(self, time_sent: datetime):
        """Sets the time_sent of this Messages.


        :param time_sent: The time_sent of this Messages.
        :type time_sent: datetime
        """

        self._time_sent = time_sent
