import connexion
import six
from flask import abort
from swagger_server.models.communities import Communities  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.controllers.moderators_controller import *
from swagger_server.controllers.user_controller import *
from swagger_server import util
from ..db import *

def create_community(body):  # noqa: E501
    """Create community

    This can only be done by the logged in user. # noqa: E501

    :param body: Created community object
    :type body: dict | bytes

    :rtype: Communities
    """
    if connexion.request.is_json:
        body = Communities.from_dict(connexion.request.get_json())  # noqa: E501
        try :
            return create_community_db(body)
        except :
            abort(400, 'Invalid input')
    abort(400, 'Invalid input')

def delete_community(community_name, user):  # noqa: E501
    """Delete community

    This can only be done by the logged in user who is the admin of the community. # noqa: E501

    :param community_name: The name of the community. Use askMosaic for testing. 
    :type community_name: str

    :rtype: None
    """
    community = get_community_by_name_db(community_name)
    if community is None:
        abort(404, 'Community not found')
    mods = get_moderators_by_community_name(community_name)
    userID = get_user_by_name(user).userID
    found = community.admin == userID
    for mod in mods:
        if mod == user:
            found = True
            break
    if not found:
        abort(401, 'User is not authorized to update this community')
    
    else:
        delete_community_db(community_name)
        return 'Community deleted'


def get_community_by_name(community_name):  # noqa: E501
    """Get community by name

     # noqa: E501

    :param community_name: The name of the community. Use askMosaic for testing. 
    :type community_name: str

    :rtype: Communities
    """
    
    community = get_community_by_name_db(community_name)
    if community is None:
        abort(404, 'Community not found')
    else:
        dc = community.to_dict()
        posts = [i.post_id for i in get_community_post_by_name_db(community_name)]
        dc['posts'] = posts
        return dc

def update_community(community_name, user, body=None):  # noqa: E501
    """Update community

    This can only be done by the logged in user who is either an admin or moderator of the community. # noqa: E501

    :param community_name: The name of the community. Use askMosaic for testing. 
    :type community_name: str
    :param body: Update an existent community
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Communities.from_dict(connexion.request.get_json())  # noqa: E501
        mods = get_moderators_by_community_name(community_name)
        userID = get_user_by_name(user).userID
        found = body.admin == userID
        for mod in mods:
            if mod == user:
                found = True
                break
        if not found:
            abort(401, 'User is not authorized to update this community')
        try :
            update_community_db(community_name, body)
            return 'Community updated'
        except :
            abort(400, 'Invalid input')
    abort(400, 'Invalid input')
