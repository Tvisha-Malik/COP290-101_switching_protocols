import connexion
import six
from flask import abort
from swagger_server.models.comment_votes import CommentVotes  # noqa: E501
from swagger_server.models.votes import Votes  # noqa: E501
from swagger_server import util
from ..db import *

def delete_comment_vote(commentID, username):  # noqa: E501
    """Delete Comment vote

    This can only be done by the logged in user. # noqa: E501

    :param comment_id: The ID of the comment
    :type comment_id: int
    :param username: The name of the user. Use reaper_113 for testing.
    :type username: str

    :rtype: None
    """
    comment = get_comment_by_id_db(commentID)
    if comment is None:
        abort(404, 'Comment not found')
    else:
        try :
            vote = get_vote_by_comment_id_db(commentID, username)
            delete_comment_vote_db(commentID, username)
            vote_comment_change_db(commentID, vote.upvote, -1)
            return 'Comment vote deleted'
        except :
            abort(400, 'Invalid input')
    


def delete_post_vote(postID, username):  # noqa: E501
    """Delete post vote

    This can only be done by the logged in user. # noqa: E501

    :param postID: The ID of the post
    :type postID: int
    :param username: The name of the user. Use reaper_113 for testing.
    :type username: str

    :rtype: None
    """
    post = get_post_by_id_db(postID)
    if post is None:
        abort(404, 'Post not found')
    else:
        try :
            vote = get_vote_by_id_db(postID, username)
            delete_post_vote_db(postID, username)
            vote_post_change_db(postID, vote.voted, -1)
            return 'Post vote deleted'
        except :
            abort(400, 'Invalid input')


def get_vote_by_comment_id(commentID, username):  # noqa: E501
    """Get comment vote by id

     # noqa: E501

    :param comment_id: The ID of the comment
    :type comment_id: int
    :param username: The name of the user. Use reaper_113 for testing.
    :type username: str

    :rtype: CommentVotes
    """
    try :
        return get_vote_by_comment_id_db(commentID, username)
    except :
        abort(400, 'Invalid input')
    


def get_vote_by_id(postID, username):  # noqa: E501
    """Get post vote by id

     # noqa: E501

    :param postID: The ID of the post
    :type postID: int
    :param username: The name of the user. Use reaper_113 for testing.
    :type username: str

    :rtype: Votes
    """
    try :
        return get_vote_by_id_db(postID, username)
    except :
        abort(400, 'Invalid input')


def update_comment_vote_by_id(commentID, username, body=None):  # noqa: E501
    """Create vote

    This can only be done by the logged in user. # noqa: E501

    :param comment_id: The ID of the comment
    :type comment_id: int
    :param username: The name of the user. Use reaper_113 for testing.
    :type username: str
    :param body: Create an new vote
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = CommentVotes.from_dict(connexion.request.get_json())  # noqa: E501
        try :
            update_comment_vote_by_id_db(commentID, username, body)
            return 200
        except :
            abort(400, 'Invalid input')
    abort(400, 'Invalid input')


def update_post_vote_by_id(postID, username, body=None):  # noqa: E501
    """Update vote

    This can only be done by the logged in user. # noqa: E501

    :param postID: The ID of the post
    :type postID: int
    :param username: The name of the user. Use reaper_113 for testing.
    :type username: str
    :param body: Update an existent vote
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Votes.from_dict(connexion.request.get_json())  # noqa: E501
        try :
            update_post_vote_by_id_db(postID, username, body)
            return 200
        except :
            abort(400, 'Invalid input')
    abort(400, 'Invalid input')