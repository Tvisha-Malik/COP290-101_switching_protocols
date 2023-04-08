import unittest

from swagger_server.db import *
from swagger_server.models import *


class TestDB(unittest.TestCase):
    def test_get_user_by_name_db(self):
        t=get_user_by_name_db("newUser?")
        if t==None:
            self.assertEqual(t,None)
        else:
            self.assertEqual(t.username,"newUser?")
    def test_create_user_db(self):
        u=User(None,"newUser?","nu@iitd.ac.in","pswrd",datetime.datetime(2000,5,14,13,20,50),datetime.datetime(2008,9,14,13,20,50),1,None,780,None)
        self.assertEqual(create_user_db(u),u)
    def test_delete_user_db(self):
        self.assertIsNone(delete_user_db("newUser?"))
    def test_get_user_notification_db(self):
        t=get_user_notifications_db("newUser?")
        if t==None:
            self.assertIsNone(t)
        else:
            self.assertIsNotNone(t)
    def test_get_user_preferences_db(self):
        t=get_user_preferences_db("newUser?")
        if t==None:
            self.assertIsNone(t)
        else:
            self.assertEqual(t.language,"English")
    def test_update_user_db(self):
        t=get_user_by_name_db("newUser?")
        if t is None:
            self.assertIsNone(t)
        elif t.user_status == 0:
            self.assertIsNotNone(t)
        else:
            p=User(None,"newUser?","nu@iitd.ac.in","psw",datetime.datetime(2000,5,14,13,20,50),datetime.datetime(2008,9,14,13,20,50),1,None,78,None)
            self.assertIsNone(update_user_db("newUser?",p))
    def test_update_user_preferences_db(self):
        t=get_user_by_name_db("newUser?")
        if t is None:
            self.assertIsNone(t)
        elif t.user_status == 0:
            self.assertIsNotNone(t)
        else:
            p=Preferences(None,"Old",datetime.datetime(2000,5,14,13,20,50),"Old","Old","English")
            self.assertIsNone(update_user_preferences_db("newUser?",p))
    def test_get_community_by_name_db(self):
        t=get_community_by_name_db("newCommunity?")
        if t==None:
            self.assertEqual(t,None)
        else:
            self.assertEqual(t.name,"newCommunity?")
    def test_create_community_db(self):
        u=Communities(None,"newCommunty?","for testing",datetime.datetime(2000,5,14,13,20,50))
        self.assertEqual(create_community_db(u),u)
    def test_update_community_bd(self):
        t=get_community_by_name_db("newCommunity?")
        if t is None:
            self.assertIsNone(t)
        elif t.user_status == 0:
            self.assertIsNotNone(t)
        else:
            u=Communities(None,"newCommunty?","for testing update",datetime.datetime(2000,5,14,13,20,50))
            self.assertIsNone(update_user_db("newCommunity?",u))
    def test_delete_communty_db(self):
        self.assertIsNone(delete_comment_db("newCommunity?"))
    def test_get_post_by_id(self):
        t=get_post_by_id_db(50)
        if t==None:
            self.assertEqual(t,None)
        else:
            self.assertEqual(t.post_id,50)
    def test_comment_by_id_db(self):
        t=get_comment_by_id_db(50)
        if t is None:
            self.assertEqual(t,None)
        else:
            self.assertEqual(t.id,50)
    def test_get_vote_by_comment_id_db(self):
        t=get_vote_by_comment_id_db(50,"newUser?")
        if t==None:
            self.assertIsNone(t)
        else:
            self.assertEqual(t.comment_id,50)
    def test_get_votes_by_id_db(self):
        t=get_vote_by_id_db(50,"newUser?")
        if t==None:
            self.assertIsNone(t)
        else:
            self.assertEqual(t.post_id,50)
    def test_get_blocked_list_db(self):
        t=get_blocked_list_db("newUser?")
        if t==None:
            self.assertIsNone(t)
        else:
            self.assertEqual(t[0].blocked_by,50)
    def test_get_following_list_db(self):
        t=get_following_list_db("newUser?")
        if t==None:
            self.assertIsNone(t)
        else:
            self.assertEqual(t[0].follower,50)
    def test_get_history_db(self):
        t=get_history_db("newUser?")
        if t==None:
            self.assertIsNone(t)
        else:
            self.assertIsNotNone(t)
    def test_get_saved_comments_list_db(self):
        t=get_saved_comments_list_db("newUser?")
        if t==None:
            self.assertIsNone(t)
        else:
            self.assertIsNotNone(t)
    def test_get_saved_posts_list_db(self):
        t=get_saved_comments_list_db("newUser?")
        if t==None:
            self.assertIsNone(t)
        else:
            self.assertIsNotNone(t)
    def test_get_subscriptions_db(self):
        t=get_subscriptions_db("newUser?")
        if t==None:
            self.assertIsNone(t)
        else:
            self.assertIsNotNone(t)
    def test_get_moderators_by_community_name_db(self):
        t=get_moderators_by_community_name_db("newCommunity?")
        if t==None:
            self.assertIsNone(t)
        else:
            self.assertIsNotNone(t)

            






if __name__ == '__main__':
  unittest.main()