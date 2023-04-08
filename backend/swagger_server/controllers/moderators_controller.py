import connexion
import six
from flask import abort
from swagger_server import util
from ..db import *

def add_mod(community_name, username, user):  # noqa: E501
    """Add a new Moderator

    This can only be done by the logged in user who is the Admin of the Community. # noqa: E501

    :param community_name: The name of the community. Use askMosaic for testing. 
    :type community_name: str
    :param username: The name of the user. Use reaper_113 for testing.
    :type username: str

    :rtype: None
    """
    community  = get_community_by_name_db(community_name)
    if community is None:
        abort(404, 'Community not found')
    if community.admin != get_user_by_name_db(user).user_id:
        abort(403, 'User not authorized')
    x = get_user_by_name_db(username)
    if x is None:
        abort(404, 'User not found')
    try :
        add_mod_db(community_name, username)
        return 'User added as mod'
    except :
        abort(400, 'Invalid input')


def get_moderators_by_community_name(community_name):  # noqa: E501
    """Get mods by community

     # noqa: E501

    :param community_name: The name of the community. Use askMosaic for testing. 
    :type community_name: str

    :rtype: List[str]
    """
    community  = get_community_by_name_db(community_name)
    if community is None:
        abort(404, 'Community not found')
    m = get_moderators_by_community_name_db(community_name)
    if m is None:
        return []
    return [i.user_id for i in m]


def remove_mod(community_name, username, user):  # noqa: E501
    """Remove as Moderator

    This can only be done by the logged in user who is the Admin of the Community. # noqa: E501

    :param community_name: The name of the community. Use askMosaic for testing. 
    :type community_name: str
    :param username: The name of the user. Use reaper_113 for testing.
    :type username: str

    :rtype: None
    """
    community  = get_community_by_name_db(community_name)
    if community is None:
        abort(404, 'Community not found')
    if community.admin != get_user_by_name_db(user).user_id:
        abort(403, 'User not authorized')
    x = get_user_by_name_db(username)
    if x is None:
        abort(404, 'User not found')
    try :
        remove_mod_db(community_name, username)
        return 'User removed as mod'
    except :
        abort(400, 'Invalid input')
