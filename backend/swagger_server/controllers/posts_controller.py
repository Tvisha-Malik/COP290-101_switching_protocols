import connexion
import six

from flask import abort
from swagger_server.models.posts import Posts  # noqa: E501
from swagger_server import util
from ..db import *


def create_post(body):  # noqa: E501
    """Create Post

    This can only be done by the logged in user. # noqa: E501

    :param body: Created posted object
    :type body: dict | bytes

    :rtype: Posts
    """
    if connexion.request.is_json:
        body = PostsDb.from_dict(connexion.request.get_json())  # noqa: E501
        try :
            return create_post_db(body)
        except :
            abort(400, 'Invalid input')
    abort(400, 'Invalid input')

def delete_post(postID, user):  # noqa: E501
    """Delete post

    This can only be done by the logged in user who created the post or the one who is either a moderator or admin of the community. # noqa: E501

    :param post_id: The ID of the post
    :type post_id: int

    :rtype: None
    """
    post = get_post_by_id_db(postID)
    
    if post is None:
        abort(404, 'Post not found')
    community_id = post.community_id
    community = get_community_by_id_db(community_id)
    mods = get_moderators_by_community_name_db(community.name)
    userID = get_user_by_name_db(user).user_id
    found = (community.admin == userID) or (post.created_by == userID)
    for mod in mods:
        if mod.user_id == userID:
            found = True
            break
    if not found:
        abort(401, 'User is not authorized to delete this post')
    else:
        try :
            delete_post_db(postID)
            return 'Post deleted'
        except :
            abort(400, 'Invalid input')


def get_post_by_id(postID):  # noqa: E501
    """Get post by id

     # noqa: E501

    :param post_id: The ID of the post
    :type post_id: int

    :rtype: Posts
    """
    post_db = get_post_by_id_db(postID)
    if post_db is None:
        abort(404, 'Post not found')
    else:
        tags = [i.name for i in tags_from_post_id_db(postID)]
        comments = [i.comment_id for i in comments_from_post_id_db(postID)]
        post = Posts(id=post_db.post_id, community=post_db.community_id, created_by=post_db.created_by, title=post_db.title, content=post_db.content, tags=tags, comments=comments)
        return post


def update_post(postID, user, body=None):  # noqa: E501
    """Update post

    This can only be done by the logged in user who is the creator of the post. # noqa: E501

    :param post_id: The ID of the post
    :type post_id: int
    :param body: Update an existent post
    :type body: dict | bytes

    :rtype: None
    """
    post = get_post_by_id_db(postID)
    if post is None:
        abort(404, 'Post not found')
    if post.created_by != get_user_by_name_db(user).user_id:
        abort(401, 'User is not authorized to update this post')
    if connexion.request.is_json:
        body = PostsDb.from_dict(connexion.request.get_json())  # noqa: E501
        try :
            update_post_db(postID, body)
            return 'Post updated'
        except :
            abort(400, 'Invalid input')
    abort(400, 'Invalid input')
