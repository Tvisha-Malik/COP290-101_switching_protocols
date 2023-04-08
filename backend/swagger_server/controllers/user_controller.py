import connexion
import six
from flask import abort
from swagger_server.models.notifications import Notifications  # noqa: E501
from swagger_server.models.preferences import Preferences  # noqa: E501
from swagger_server.models.u_login_body import ULoginBody  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util
from ..db import *
import jwt

secretkey = '101_Switching_Protocols'

def create_user(body):  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
        try :
            return create_user_db(body)
        except :
            abort(400, 'Invalid input')
    else :
        abort(400, 'Invalid input')


def delete_user(username):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param username: The name of the user. Use reaper_113 for testing.
    :type username: str

    :rtype: None
    """
    user = get_user_by_name_db(username)
    if user is None:
        abort(404, 'User not found')
    else:
        delete_user_db(username)
        return 'User deleted'


def forgot_password(username=None, email=None):  # noqa: E501
    """Sends recovery email

     # noqa: E501

    :param username: The user name for login
    :type username: str
    :param email: The email for login
    :type email: str

    :rtype: str
    """
    return 'do some magic!'


def get_user_by_name(username):  # noqa: E501
    """Get user by user name

     # noqa: E501

    :param username: The name of the user. Use reaper_113 for testing.
    :type username: str

    :rtype: User
    """
    user = get_user_by_name_db(username)
    if user is None:
        abort(404, 'User not found')
    else:
        return user


def get_user_notifications(username):  # noqa: E501
    """Get user notifications

     # noqa: E501

    :param username: The name of the user. Use reaper_113 for testing.
    :type username: str

    :rtype: Notifications
    """
    notif = get_user_notifications_db(username)
    if notif is None:
        return []
    else:
        return notif


def get_user_preferences(username):  # noqa: E501
    """Get user preferences

     # noqa: E501

    :param username: The name of the user. Use reaper_113 for testing.
    :type username: str

    :rtype: Preferences
    """
    pref = get_user_preferences_db(username)
    if pref is None:
        abort(404, 'User not found')
    else:
        return pref


def login_user(body):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = ULoginBody.from_dict(connexion.request.get_json())  # noqa: E501
        print(body)
        try :
            if (login_user_db(body)) :
                return jwt.encode({'sub': body.username, 'scope': ['login:user']}, secretkey, algorithm='HS256')
            else :
                abort(401, 'Invalid credentials')
        except Exception as e:
            abort(400, str(e))
    abort(400, 'Invalid input')


def update_user(username, body=None):  # noqa: E501
    """Update user

    This can only be done by the logged in user. # noqa: E501

    :param username: The name of the user. Use reaper_113 for testing.
    :type username: str
    :param body: Update an existent user in the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
        try :
            update_user_db(username, body)
            return 'User updated'
        except Exception as e:
            abort(400, str(e))
    abort(400, 'Invalid input')

def update_user_preferences(username, body=None):  # noqa: E501
    """Update user preferences

    This can only be done by the logged in user. # noqa: E501

    :param username: The name of the user. Use reaper_113 for testing.
    :type username: str
    :param body: Update prefrences of a user
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Preferences.from_dict(connexion.request.get_json())  # noqa: E501
        try :
            update_user_preferences_db(username, body)
            return 'User preferences updated'
        except Exception as e:
            abort(400, str(e))
    abort(400, 'Invalid input')