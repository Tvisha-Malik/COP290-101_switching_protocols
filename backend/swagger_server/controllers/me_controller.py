import connexion
import six
from flask import abort
from swagger_server import util
from ..db import *

def block_user(username, user):  # noqa: E501
    """Block a user

    This can only be done by the logged in user. # noqa: E501

    :param username: The name of the user to block. Use reaper_113 for testing.
    :type username: str

    :rtype: None
    """
    x = get_user_by_name_db(username)
    if x is None:
        abort(404, 'User not found')
    try :
        block_user_db(user, username)
        return 'User blocked'
    except :
        abort(400, 'Invalid input ')


def clear_history(user):  # noqa: E501
    """Clear history

     # noqa: E501


    :rtype: None
    """
    try :
        clear_history_db(user)
        return 'History cleared'
    except :
        abort(400, 'Invalid input')


def delete_follow_user(username, user):  # noqa: E501
    """Delete a followed user

    This can only be done by the logged in user. # noqa: E501

    :param username: The name of the user. Use reaper_113 for testing.
    :type username: str

    :rtype: None
    """
    x = get_user_by_name_db(username)
    if x is None:
        abort(404, 'User not found')
    try :
        delete_follow_user_db(user, username)
        return 'User unfollowed'
    except :
        abort(400, 'Invalid input')


def follow_user(username, user):  # noqa: E501
    """Follow a user

    This can only be done by the logged in user. # noqa: E501

    :param username: The name of the user. Use reaper_113 for testing.
    :type username: str

    :rtype: None
    """
    x = get_user_by_name_db(username)
    if x is None:
        abort(404, 'User not found')
    try :
        follow_user_db(user, username)
        return 'User followed'
    except :
        abort(400, 'Invalid input')


def get_blocked_list(user):  # noqa: E501
    """Get blocked list

     # noqa: E501


    :rtype: List[str]
    """
    try :
        return [get_user_by_id_db(i.blocked_user).username for i in get_blocked_list_db(user)]
    except :
        abort(400, 'Invalid input')


def get_following_list(user):  # noqa: E501
    """Get following list

     # noqa: E501


    :rtype: List[str]
    """
    try :
        return [get_user_by_id_db(i.following).username for i in get_following_list_db(user)]
    except :
        abort(400, 'Invalid input')


def get_history(user):  # noqa: E501
    """Get history

     # noqa: E501


    :rtype: List[History]
    """
    try :
        return  get_history_db(user)
    except :
        abort(400, 'Invalid input')


def get_saved_comments_list(user):  # noqa: E501
    """Get saved comments list

     # noqa: E501


    :rtype: List[SavedComments]
    """
    try :
        return  get_saved_comments_list_db(user)
    except :
        abort(400, 'Invalid input')


def get_saved_posts_list(user):  # noqa: E501
    """Get saved posts list

     # noqa: E501


    :rtype: List[SavedPosts]
    """
    try :
        return  get_saved_posts_list_db(user)
    except :
        abort(400, 'Invalid input')


def get_subscribed_communities(user):  # noqa: E501
    """Get subscribed communities

     # noqa: E501


    :rtype: List[str]
    """
    try :
        return [get_community_by_id_db(i.community_id).name for i in get_subscriptions_db(user)]
    except :
        abort(400, 'Invalid input')


def save_comment(commentID, user):  # noqa: E501
    """Saves the comment

    This can only be done by the logged in user. # noqa: E501

    :param comment_id: The ID of the comment
    :type comment_id: int

    :rtype: None
    """
    comment = get_comment_by_id_db(commentID)
    if comment is None:
        abort(404, 'Comment not found')
    try :
        save_comment_db(user, commentID)
        return 'Comment saved'
    except :
        abort(400, 'Invalid input')


def save_post(postID, user):  # noqa: E501
    """Saves the post

    This can only be done by the logged in user. # noqa: E501

    :param post_id: The ID of the post
    :type post_id: int

    :rtype: None
    """
    post = get_post_by_id_db(postID)
    if post is None:
        abort(404, 'Post not found')
    try :
        save_post_db(user, postID)
        return 'Post saved'
    except :
        abort(400, 'Invalid input')


def unblock_user(username, user):  # noqa: E501
    """Unblock a user

    This can only be done by the logged in user. # noqa: E501

    :param username: The name of the user. Use reaper_113 for testing.
    :type username: str

    :rtype: None
    """
    x = get_user_by_name_db(username)
    if x is None:
        abort(404, 'User not found')
    try :
        unblock_user_db(user, username)
        return 'User unblocked'
    except :
        abort(400, 'Invalid input')


def unsave_comment(commentID, user):  # noqa: E501
    """Unsaves the comment

    This can only be done by the logged in user. # noqa: E501

    :param comment_id: The ID of the comment
    :type comment_id: int

    :rtype: None
    """
    try :
        unsave_comment_db(user, commentID)
        return 'Comment unsaved'
    except :
        abort(400, 'Invalid input')


def unsave_post(postID, user):  # noqa: E501
    """Unsaves the post

    This can only be done by the logged in user. # noqa: E501

    :param post_id: The ID of the post
    :type post_id: int

    :rtype: None
    """
    try :
        unsave_post_db(user, postID)
        return 'Post unsaved'
    except :
        abort(400, 'Invalid input')
