import connexion
import six
from flask import abort
from swagger_server.models.comments import Comments  # noqa: E501
from swagger_server import util
from ..db import *

def create_comment(body):  # noqa: E501
    """Add comment

    This can only be done by the logged in user. # noqa: E501

    :param body: Created commented object
    :type body: dict | bytes

    :rtype: Comments
    """
    if connexion.request.is_json:
        body = Comments.from_dict(connexion.request.get_json())  # noqa: E501
        print(body)
        try :
            return create_comment_db(body)
        except :
            abort(400, 'Invalid input')
    abort(400, 'Invalid input')

def delete_comment(commentID):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param commentID: 
    :type commentID: int

    :rtype: None
    """
    comment = get_comment_by_id_db(commentID)
    if comment is None:
        abort(404, 'Comment not found')
    else:
        delete_comment_db(commentID)
        return 'Comment deleted'


def get_comment_by_id(commentID):  # noqa: E501
    """Get comment by comment id

     # noqa: E501

    :param commentID: 
    :type commentID: int

    :rtype: Comments
    """
    comment = get_comment_by_id_db(commentID)
    if comment is None:
        abort(404, 'Comment not found')
    else:
        return comment


def update_comment(commentID, body=None):  # noqa: E501
    """Update cooment

    This can only be done by the logged in user. # noqa: E501

    :param commentID: 
    :type commentID: int
    :param body: Update an existent comment
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Comments.from_dict(connexion.request.get_json())
          # noqa: E501
        try :
            return update_comment_db(commentID, body),200
        except :
            abort(400, 'Invalid input')
    abort(400, 'Invalid input')
