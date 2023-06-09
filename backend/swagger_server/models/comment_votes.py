# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CommentVotes(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, comment_vote_id: int=None, user_id: int=None, comment_id: int=None, upvote: bool=None, time: datetime=None):  # noqa: E501
        """CommentVotes - a model defined in Swagger

        :param comment_vote_id: The comment_vote_id of this CommentVotes.  # noqa: E501
        :type comment_vote_id: int
        :param user_id: The user_id of this CommentVotes.  # noqa: E501
        :type user_id: int
        :param comment_id: The comment_id of this CommentVotes.  # noqa: E501
        :type comment_id: int
        :param upvote: The upvote of this CommentVotes.  # noqa: E501
        :type upvote: bool
        :param time: The time of this CommentVotes.  # noqa: E501
        :type time: datetime
        """
        self.swagger_types = {
            'comment_vote_id': int,
            'user_id': int,
            'comment_id': int,
            'upvote': bool,
            'time': datetime
        }

        self.attribute_map = {
            'comment_vote_id': 'commentVoteID',
            'user_id': 'userID',
            'comment_id': 'commentID',
            'upvote': 'upvote',
            'time': 'time'
        }
        self._comment_vote_id = comment_vote_id
        self._user_id = user_id
        self._comment_id = comment_id
        self._upvote = upvote
        self._time = time

    @classmethod
    def from_dict(cls, dikt) -> 'CommentVotes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CommentVotes of this CommentVotes.  # noqa: E501
        :rtype: CommentVotes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def comment_vote_id(self) -> int:
        """Gets the comment_vote_id of this CommentVotes.


        :return: The comment_vote_id of this CommentVotes.
        :rtype: int
        """
        return self._comment_vote_id

    @comment_vote_id.setter
    def comment_vote_id(self, comment_vote_id: int):
        """Sets the comment_vote_id of this CommentVotes.


        :param comment_vote_id: The comment_vote_id of this CommentVotes.
        :type comment_vote_id: int
        """

        self._comment_vote_id = comment_vote_id

    @property
    def user_id(self) -> int:
        """Gets the user_id of this CommentVotes.


        :return: The user_id of this CommentVotes.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this CommentVotes.


        :param user_id: The user_id of this CommentVotes.
        :type user_id: int
        """

        self._user_id = user_id

    @property
    def comment_id(self) -> int:
        """Gets the comment_id of this CommentVotes.


        :return: The comment_id of this CommentVotes.
        :rtype: int
        """
        return self._comment_id

    @comment_id.setter
    def comment_id(self, comment_id: int):
        """Sets the comment_id of this CommentVotes.


        :param comment_id: The comment_id of this CommentVotes.
        :type comment_id: int
        """

        self._comment_id = comment_id

    @property
    def upvote(self) -> bool:
        """Gets the upvote of this CommentVotes.


        :return: The upvote of this CommentVotes.
        :rtype: bool
        """
        return self._upvote

    @upvote.setter
    def upvote(self, upvote: bool):
        """Sets the upvote of this CommentVotes.


        :param upvote: The upvote of this CommentVotes.
        :type upvote: bool
        """

        self._upvote = upvote

    @property
    def time(self) -> datetime:
        """Gets the time of this CommentVotes.


        :return: The time of this CommentVotes.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time: datetime):
        """Sets the time of this CommentVotes.


        :param time: The time of this CommentVotes.
        :type time: datetime
        """

        self._time = time
