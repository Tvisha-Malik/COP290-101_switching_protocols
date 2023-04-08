#"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0VXNlciIsInNjb3BlIjpbImxvZ2luOnVzZXIiXX0.ryzQH_7QE2-iH6qqQME-tz9eG4CQvJLfLD3ME1nTz0g"
from typing import Optional
import datetime
import pymysql
import six
from swagger_server.models import *

connection = pymysql.connect(host='10.17.51.143',
                             user='switching_protocols',
                             password='cs1210085',
                             database='cop3',
                             cursorclass=pymysql.cursors.DictCursor)

def get_user_by_name_db(name) -> Optional[User]:
  with connection.cursor() as cursor:
    sql = 'SELECT * FROM `users` WHERE `username`=%s'
    cursor.execute(sql, (name))
    r = cursor.fetchone()
    if r is None:
      return None
    return User.from_dict(r)
  
# print((get_user_from_name("Tvisha")))

def create_user_db(user: User):
  assert user.user_id is None # if tag.id is none then only we proceed 
  t = get_user_by_name_db(user.username) # we get the tag from the tag.name 
  if t is not None: # if we already have that tag in our dataset then set the id of tag and exit
    user.user_id=t.user_id
    return t

  with connection.cursor() as cursor: # if the tag name is not in data base then we insert it 
    sql_str="INSERT INTO users ("
    for key,value in six.iteritems(user.attribute_map):
      if value!="UserID":
        sql_str+=value+","
    sql_str=sql_str[:-1]
    sql_str+=") VALUES ("

    for key in user.attribute_map:
      if key!="user_id":
        if eval('user.'+ key)==None:
          sql_str+="Null"+","
        elif user.swagger_types[key]==str or user.swagger_types[key]==datetime.datetime:
          sql_str+="'"+str(eval('user.'+ key))+"'"+","
        elif user.swagger_types[key]==bool:
          sql_str+=str(int(eval('user.'+ key)))+","
        else:
          sql_str+=str(eval('user.'+ key))+","

    sql_str=sql_str[:-1]
    sql_str+=");"
    cursor.execute(sql_str)
    connection.commit()
    user.user_id = cursor.lastrowid
    return get_user_by_name_db(user.username)

# print(create_user_db(User(None,"testUser2","test2Email@iitd.ac.in","test2Password",datetime.datetime(2004,7,8,3,4,2),datetime.datetime(2019,7,8,3,4,2),0,None,89,80)))

def delete_user_db(username)-> None:
  assert username is not None # if tag.id is none then only we proceed 
  with connection.cursor() as cursor:
    cursor.execute("DELETE FROM users WHERE username = %s",username)
    connection.commit()
# delete_user_db("Tvisha")
def get_user_notifications_db(username)-> Optional[list[Notifications]]:
  with connection.cursor() as cursor:
    sql = 'SELECT * FROM `users` WHERE `username`=%s'
    cursor.execute(sql, (username))
    r = cursor.fetchone()
    if r is None:
      return None
    sql = 'SELECT * FROM `notifications` WHERE `UserID`=%s'
    cursor.execute(sql, (r['UserID']))
    r = cursor.fetchall()
    if r is None:
      return None
    l=[]
    for i in r:
      l.append(Notifications.from_dict(i))
    return l
# print(get_user_notifications_db("Sofi_A"))
def get_user_preferences_db(username)-> Optional[Preferences]:
  with connection.cursor() as cursor:
    sql = 'SELECT * FROM `users` WHERE `username`=%s'
    cursor.execute(sql, (username))
    r = cursor.fetchone()
    if r is None:
      return None
    sql = 'SELECT * FROM `preferences` WHERE `preferenceID`=%s'
    cursor.execute(sql, (r['userPreferences']))
    r = cursor.fetchone()
    if r is None:
      return None
    return Preferences.from_dict(r)

def update_user_db(username, body=None)-> None:# exact update, set to null if not present
  assert body.user_id is None
  t = get_user_by_name_db(username)
  assert t is not None
  assert t.user_status == 1
  with connection.cursor() as cursor:
    sql="UPDATE users SET "
    for key in body.attribute_map:
      if key!="user_id":
        if eval('body.'+ key)==None:
          sql+=body.attribute_map[key]+"="+"Null"+","
        elif body.swagger_types[key]==str or body.swagger_types[key]==datetime.datetime:
          sql+=body.attribute_map[key]+"="+"'"+str(eval('body.'+ key))+"'"+","
        elif body.swagger_types[key]==bool:
          sql+=body.attribute_map[key]+"="+str(int(eval('body.'+ key)))+","
        else:
          sql+=body.attribute_map[key]+"="+str(eval('body.'+ key))+","
    sql=sql[:-1]
    sql+=" WHERE UserID ="+str(t.user_id)
    cursor.execute(sql)
    connection.commit()
    body.id = cursor.lastrowid

def update_user_preferences_db(username, body=None)-> None:# ignores null
  assert body.preference_id is None
  t = get_user_by_name_db(username)
  assert t is not None
  assert t.user_status == 1
  with connection.cursor() as cursor:
    sql="UPDATE preferences SET "
    for key in body.attribute_map:
      if key!="preference_id":
        if eval('body.'+ key)==None:
          sql+=body.attribute_map[key]+"="+"Null"+","
        elif body.swagger_types[key]==str or body.swagger_types[key]==datetime.datetime:
          sql+=body.attribute_map[key]+"="+"'"+str(eval('body.'+ key))+"'"+","
        elif body.swagger_types[key]==bool:
          sql+=body.attribute_map[key]+"="+str(int(eval('body.'+ key)))+","
        else:
          sql+=body.attribute_map[key]+"="+str(eval('body.'+ key))+","
    sql=sql[:-1]
    sql+=" WHERE preferenceID ="+str(t.user_preferences)
    # print(sql)
    cursor.execute(sql)
    connection.commit()
    body.id = cursor.lastrowid

# def login_user(body)-> None:




# update_user_preferences_db("Tvisha",Preferences(None,"Old"))
# print(get_user_preferences_db("A_b_a"))
def get_community_by_name_db(name) -> Optional[Communities]:
  with connection.cursor() as cursor:
    sql = 'SELECT * FROM `communities` WHERE `name`=%s'
    cursor.execute(sql, (name))
    r = cursor.fetchone()
    if r is None:
      return None
    return Communities.from_dict(r)
# print(get_community_by_name_db("newCommunty?"))

def create_community_db(body)-> Communities:
  assert body.community_id is None # if tag.id is none then only we proceed 
  assert body.name is not None
  t = get_community_by_name_db(body.name) # we get the tag from the tag.name 
  if t is not None: # if we already have that tag in our dataset then set the id of tag and exit
    body.community_id=t.community_id
    return t

  with connection.cursor() as cursor: # if the tag name is not in data base then we insert it 
    sql_str="INSERT INTO communities ("
    for key,value in six.iteritems(body.attribute_map):
      if value!="communityID":
        sql_str+=value+","
    sql_str=sql_str[:-1]
    sql_str+=") VALUES ("

    for key in body.attribute_map:
      if key!="community_id":
        if eval('body.'+ key)==None:
          sql_str+="Null"+","
        elif body.swagger_types[key]==str or body.swagger_types[key]==datetime.datetime:
          sql_str+="'"+str(eval('body.'+ key))+"'"+","
        elif body.swagger_types[key]==bool:
          sql_str+=str(int(eval('body.'+ key)))+","
        else:
          sql_str+=str(eval('body.'+ key))+","

    sql_str=sql_str[:-1]
    sql_str+=");"
    cursor.execute(sql_str)
    connection.commit()
    body.id = cursor.lastrowid
    return get_community_by_name_db(body.name)

def update_community_db(community_name, body=None)-> None:# exact update, set to null if not present
  assert body.community_id is None
  t = get_community_by_name_db(community_name)
  assert t is not None
  with connection.cursor() as cursor:
    sql="UPDATE communities SET "
    for key in body.attribute_map:
      if key!="community_id":
        if eval('body.'+ key)==None:
          sql+=body.attribute_map[key]+"="+"Null"+","
        elif body.swagger_types[key]==str or body.swagger_types[key]==datetime.datetime:
          sql+=body.attribute_map[key]+"="+"'"+str(eval('body.'+ key))+"'"+","
        elif body.swagger_types[key]==bool:
          sql+=body.attribute_map[key]+"="+str(int(eval('body.'+ key)))+","
        else:
          sql+=body.attribute_map[key]+"="+str(eval('body.'+ key))+","
    sql=sql[:-1]
    sql+=" WHERE communityID ="+str(t.community_id)
    # print(sql)
    cursor.execute(sql)
    connection.commit()
    body.id = cursor.lastrowid


def delete_community_db(community_name)-> None:
  assert community_name is not None # if tag.id is none then only we proceed 
  with connection.cursor() as cursor:
    cursor.execute("DELETE FROM communities WHERE name = %s",community_name)
    connection.commit()
# delete_community_db("test2")
# update_community_db("test",Communities(None,"test2","this has to be deleted2,"))

def get_post_by_id_db(post_id)-> PostsDb :
  with connection.cursor() as cursor:
    sql = 'SELECT * FROM `posts` WHERE `postID`=%s'
    cursor.execute(sql, (post_id))
    r = cursor.fetchone()
    if r is None:
      return None
    return PostsDb.from_dict(r)
# print(get_post_by_id(200))

def get_comment_by_id_db(id:int) -> Optional[Comments]:
  if id==None:
    return None
  with connection.cursor() as cursor:
    sql = 'SELECT * FROM `comments` WHERE `commentID`=%s'
    cursor.execute(sql, (id))
    r = cursor.fetchone()
    if r is None:
      return None
    return Comments.from_dict(r)
  

  
# print(get_comment_by_id_db(7))

def create_comment_db(comment: Comments):
  assert comment.comment_id is None # if tag.id is none then only we proceed 
  t = get_comment_by_id_db(comment.comment_id) # we get the tag from the tag.name 
  if t is not None: # if we already have that tag in our dataset then set the id of tag and exit
    comment.comment_id=t.comment_id
    return t

  with connection.cursor() as cursor: # if the tag name is not in data base then we insert it 
    sql_str="INSERT INTO comments ("
    for key,value in six.iteritems(comment.attribute_map):
      if value!="commentID":
        sql_str+=value+","
    sql_str=sql_str[:-1]
    sql_str+=") VALUES ("

    for key in comment.attribute_map:
      if key!="comment_id":
        if eval('comment.'+ key)==None:
          sql_str+="Null"+","
        elif comment.swagger_types[key]==str or comment.swagger_types[key]==datetime.datetime:
          sql_str+="'"+str(eval('comment.'+ key))+"'"+","
        else:
          sql_str+=str(eval('comment.'+ key))+","

    sql_str=sql_str[:-1]
    sql_str+=");"
    cursor.execute(sql_str)
    connection.commit()
    comment.comment_id = cursor.lastrowid
    return get_comment_by_id_db(comment.comment_id)
# print(create_comment_db(Comments(206,None,"this",29,None,None,7,9)))

def update_comment_db(comment_id, body:Comments=None)-> None:# ignores null
  assert body.comment_id is None
  t = get_comment_by_id_db(comment_id)
  assert t is not None
  with connection.cursor() as cursor:
    sql="UPDATE comments SET "
    for key in body.attribute_map:
      if key!="comment_id":
        if eval('body.'+ key)==None:
          sql+=body.attribute_map[key]+"="+"Null"+","
        elif body.swagger_types[key]==str or body.swagger_types[key]==datetime.datetime:
          sql+=body.attribute_map[key]+"="+"'"+str(eval('body.'+ key))+"'"+","
        else:
          sql+=body.attribute_map[key]+"="+str(eval('body.'+ key))+","
    sql=sql[:-1]
    sql+=" WHERE commentID ="+str(t.comment_id)
    cursor.execute(sql)
    connection.commit()
    body.comment_id = cursor.lastrowid
# update_comment_db(228,Comments(224,None,"this is updated",90,8))

def delete_comment_db(comment_id)-> None:
  assert comment_id is not None # if tag.id is none then only we proceed 
  with connection.cursor() as cursor:
    cursor.execute("DELETE FROM comments WHERE commentID = %s",comment_id)
    connection.commit()
# delete_comment_db(229)

def login_user_db(body:ULoginBody):
  assert body is not None
  assert body.username is not None
  assert body.password is not None
  print(body.username)
  print(body.password)
  t = get_user_by_name_db(body.username)
  if (t is not None and t.password!=body.password):
    return False
  with connection.cursor() as cursor:
    cursor.execute("UPDATE users SET userStatus = 1 where username = %s",(body.username))
    connection.commit()
    return True
# print(login_user_db(ULoginBody("A_b_a","1mlv8")))

def delete_comment_vote_db(comment_id,username)-> None:
  assert comment_id is not None # if tag.id is none then only we proceed
  assert username is not None  
  t = get_user_by_name_db(username)
  with connection.cursor() as cursor:
    cursor.execute("DELETE FROM commentvotes WHERE commentID = "+str(comment_id)+" and userID="+str(t.user_id))
    connection.commit()

def vote_comment_change_db(comment_id,up,n):
  t = get_comment_by_id_db(comment_id)
  with connection.cursor() as cursor:
    if up:
      cursor.execute("UPDATE comments SET upvotes ="+str(t.upvotes+n)+" where commentID = %s",(comment_id))
    else:
      cursor.execute("UPDATE comments SET downvotes ="+str(t.downvotes+n)+" where commentID = %s",(comment_id))
    connection.commit()
def delete_post_vote_db(post_id,username)-> None:
  assert post_id is not None # if tag.id is none then only we proceed
  assert username is not None  
  t = get_user_by_name_db(username)
  with connection.cursor() as cursor:
    cursor.execute("DELETE FROM postvotes WHERE postID = "+str(post_id)+" and userID="+str(t.user_id))
    connection.commit()
def vote_post_change_db(post_id,up,n):
  t = get_post_by_id_db(post_id)
  with connection.cursor() as cursor:
    if up:
      cursor.execute("UPDATE posts SET upvotes ="+str(t.upvotes+n)+" where postID = %s",(post_id))
    else:
      cursor.execute("UPDATE posts SET downvotes ="+str(t.downvotes+n)+" where postID = %s",(post_id))
    connection.commit()

def get_vote_by_comment_id_db(comment_id,username)->Optional[CommentVotes]:
  
  assert comment_id is not None # if tag.id is none then only we proceed
  assert username is not None  
  t = get_user_by_name_db(username)
  if t is None:
    return None
  with connection.cursor() as cursor:
    sql = "SELECT * FROM commentvotes WHERE commentID = "+str(comment_id)+" and userID="+str(t.user_id)
    cursor.execute(sql)
    r = cursor.fetchone()
    if r is None:
      return None
    return CommentVotes.from_dict(r)
  

def get_vote_by_id_db(post_id,username)->Optional[Votes]:
    assert post_id is not None
    assert username is not None
    t=get_user_by_name_db(username)
    if t is None:
      return None
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM postvotes WHERE postID= '+str(post_id)+" and userID="+str(t.user_id)
        cursor.execute(sql)
        r = cursor.fetchone()
        if r is None:
            return None
        return Votes.from_dict(r)
# print(get_vote_by_id_db(170))

# def update_comment_vote_by_id(comment_id, body=None):
# delete_comment_vote_db(43,"F-A-F-A")

def update_comment_vote_by_id_db(comment_id, username, body:CommentVotes=None):
  assert body.comment_vote_id is None
  t = get_user_by_name_db(username)
  assert t is not None
  
  with connection.cursor() as cursor:
    sql="insert into commentvotes (commentID,time,userID,upvote) values ("+str(comment_id)+",'"+str(body.time)+"',"+str(t.user_id)+","+str(int(body.upvote))+")"
    cursor.execute(sql)
    connection.commit()
    body.id = cursor.lastrowid

# update_comment_vote_by_id_db(92,"a-c-p-a",CommentVotes(None,3,90,False,datetime.datetime(2005,6,7,12,50,30)))

def update_post_vote_by_id_db(post_id, username, body:Votes=None):
  assert body.post_vote_id is None
  t = get_user_by_name_db(username)
  assert t is not None
  
  with connection.cursor() as cursor:
    sql="insert into postvotes (postID,time,userID,voted) values ("+str(post_id)+",'"+str(body.time)+"',"+str(t.user_id)+","+str(int(body.voted))+");"
    cursor.execute(sql)
    connection.commit()
    body.post_vote_id = cursor.lastrowid
def block_user_db(blockedBy,blockedUser):
    assert blockedBy is not None
    assert blockedUser is not None
    t1=get_user_by_name_db(blockedBy)
    if t1 is None:
      return None
    t2=get_user_by_name_db(blockedUser)
    if t2 is None:
      return None
    with connection.cursor() as cursor:
        sql="INSERT INTO blocks (blockedBy,blockedUser) VALUES ("+str(t1.user_id)+","+str(t2.user_id)+");"
        print(sql)
        cursor.execute(sql)
        connection.commit()

def unblock_user_db(blockedBy,blockedUser):
    assert blockedBy is not None
    assert blockedUser is not None
    t1=get_user_by_name_db(blockedBy)
    if t1 is None:
      return None
    t2=get_user_by_name_db(blockedUser)
    if t2 is None:
      return None
    with connection.cursor() as cursor:
        sql="DELETE FROM blocks WHERE blockedBy = "+str(t1.user_id)+" and blockedUser="+str(t2.user_id)
        cursor.execute(sql)
        connection.commit()
        
def clear_history_db(username) :
    assert username is not None
    userID = get_user_by_name_db(username).user_id
    with connection.cursor() as cursor:
        sql="DELETE FROM history WHERE userID = %s"
        cursor.execute(sql,(userID))
        connection.commit()

def follow_user_db(follower,following):
    assert follower is not None
    assert following is not None
    t1=get_user_by_name_db(follower)
    if t1 is None:
      return None
    t2=get_user_by_name_db(following)
    if t2 is None:
      return None
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with connection.cursor() as cursor:
        sql="INSERT INTO follows (follower,following,time) VALUES ("+str(t1.user_id)+","+str(t2.user_id)+",'"+str(time)+"')"
        cursor.execute(sql)
        connection.commit()
    print(time)

def delete_follow_user_db(follower,following):
    assert follower is not None
    assert following is not None
    t1=get_user_by_name_db(follower)
    if t1 is None:
      return None
    t2=get_user_by_name_db(following)
    if t2 is None:
      return None
    with connection.cursor() as cursor:
        sql="DELETE FROM follows WHERE follower = "+str(t1.user_id)+" and following="+str(t2.user_id)+" ;"
        cursor.execute(sql)
        connection.commit()

def get_blocked_list_db(username)->Optional[list[BlockUsers]]:
    assert username is not None
    userID = get_user_by_name_db(username)
    if userID is None:
      return None
    userID=userID.user_id
    with connection.cursor() as cursor:
        sql="SELECT * FROM blocks WHERE blockedBy = %s"
        cursor.execute(sql,(userID))
        r = cursor.fetchall()
        if r is None:
            return None
        return [BlockUsers.from_dict(i) for i in r]
    
    
def get_following_list_db(username)->Optional[list[FollowUsers]]:
    assert username is not None
    userID = get_user_by_name_db(username)
    if userID is None:
      return None
    userID=userID.user_id
    with connection.cursor() as cursor:
        sql="SELECT * FROM follows WHERE follower = %s"
        cursor.execute(sql,(userID))
        r = cursor.fetchall()
        if r is None:
            return None
        return [FollowUsers.from_dict(i) for i in r]
    
def get_history_db(username)->Optional[list[History]]:
    assert username is not None
    userID = get_user_by_name_db(username)
    if userID is None:
      return None
    userID=userID.user_id
    with connection.cursor() as cursor:
        sql="SELECT * FROM history WHERE userID = %s"
        cursor.execute(sql,(userID))
        r = cursor.fetchall()
        if r is None:
            return None
        return [History.from_dict(i) for i in r]
    
def get_saved_comments_list_db(username)->Optional[list[SavedComments]]:
    assert username is not None
    userID = get_user_by_name_db(username)
    if userID is None:
      return None
    userID=userID.user_id
    with connection.cursor() as cursor:
        sql="SELECT * FROM savedcomments WHERE userID = %s"
        cursor.execute(sql,(userID))
        r = cursor.fetchall()
        if r is None:
            return None
        return [SavedComments.from_dict(i) for i in r]

def get_saved_posts_list_db(username)->Optional[list[SavedPosts]]:
    assert username is not None
    userID = get_user_by_name_db(username)
    if userID is None:
      return None
    userID=userID.user_id
    with connection.cursor() as cursor:
        sql="SELECT * FROM savedposts WHERE userID = %s"
        cursor.execute(sql,(userID))
        r = cursor.fetchall()
        if r is None:
            return None
        return [SavedPosts.from_dict(i) for i in r]
    
def get_subscriptions_db(username)->Optional[list[SubscribedCommunities]]:
    assert username is not None
    userID = get_user_by_name_db(username)
    if userID is None:
      return None
    userID=userID.user_id
    with connection.cursor() as cursor:
        sql="SELECT * FROM subscriptions WHERE userID = %s"
        cursor.execute(sql,(userID))
        r = cursor.fetchall()
        if r is None:
            return None
        return [SubscribedCommunities.from_dict(i) for i in r]
    
def save_comment_db(username,comment_id):
    assert username is not None
    assert comment_id is not None
    userID = get_user_by_name_db(username).user_id
    timeSaved = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with connection.cursor() as cursor:
        sql="INSERT INTO savedcomments (userID,commentID,timeSaved) VALUES ("+str(userID)+","+str(comment_id)+",'"+str(timeSaved)+"')"
        cursor.execute(sql)
        connection.commit()

def save_post_db(username,post_id):
    assert username is not None
    assert post_id is not None
    userID = get_user_by_name_db(username).user_id
    timeSaved = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with connection.cursor() as cursor:
        sql="INSERT INTO savedposts (userID,postID,timeSaved) VALUES ("+str(userID)+","+str(post_id)+",'"+str(timeSaved)+"')"
        cursor.execute(sql)
        connection.commit()

def unsave_comment_db(username,comment_id):
    assert username is not None
    assert comment_id is not None
    userID = get_user_by_name_db(username).user_id
    with connection.cursor() as cursor:
        sql="DELETE FROM savedcomments WHERE userID = "+str(userID)+" and commentID="+str(comment_id)
        cursor.execute(sql)
        connection.commit()

def unsave_post_db(username,post_id):
    assert username is not None
    assert post_id is not None
    userID = get_user_by_name_db(username).user_id
    with connection.cursor() as cursor:
        sql="DELETE FROM savedposts WHERE userID = "+str(userID)+" and postID="+str(post_id)
        cursor.execute(sql)
        connection.commit()


def add_mod_db(community_name, username):
  assert community_name is not None
  assert username is not None
  c=get_community_by_name_db(community_name)
  t= get_user_by_name_db(username)
  with connection.cursor() as cursor:
    cursor.execute("select * from moderators where userID = "+str(t.user_id))
    r= cursor.fetchone()
    if r is None:
      return
    cursor.execute("Insert into moderators (communityID,timeAdded,UserID) values ("+str(c.community_id)+",'"+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"',"+str(t.user_id)+")")
    connection.commit()

# add_mod_db("funny","sei_a")
def get_moderators_by_community_name_db(community_name):
  assert community_name is not None
  c=get_community_by_name_db(community_name)
  if c is None:
    return None
  with connection.cursor() as cursor:
    cursor.execute("select * from moderators where communityID = "+str(c.community_id))
    r=cursor.fetchall()
    if r is None:
      return None
    return [Moderators.from_dict(i) for i in r]

# print(get_moderators_by_community_name("funny"))
def remove_mod_db(community_name, username):
  assert community_name is not None
  assert username is not None
  c=get_community_by_name_db(community_name)
  t= get_user_by_name_db(username)
  with connection.cursor() as cursor:
    cursor.execute("DELETE FROM moderators WHERE communityID = "+str(c.community_id)+" and userID="+str(t.user_id))
    connection.commit()

# remove_mod("funny","sei_a")


def create_post_db(body:PostsDb):
  assert body.post_id is None
  with connection.cursor() as cursor:
    sql_str="INSERT INTO posts ("
    for key,value in six.iteritems(body.attribute_map):
      if value!="postID":
        sql_str+=value+","
    sql_str=sql_str[:-1]
    sql_str+=") VALUES ("

    for key in body.attribute_map:
      if key!="post_id":
        if eval('body.'+ key)==None:
          sql_str+="Null"+","
        elif body.swagger_types[key]==str or body.swagger_types[key]==datetime.datetime:
          sql_str+="'"+str(eval('body.'+ key))+"'"+","
        elif body.swagger_types[key]==bool:
          sql_str+=str(int(eval('body.'+ key)))+","
        else:
          sql_str+=str(eval('body.'+ key))+","

    sql_str=sql_str[:-1]
    sql_str+=");"
    cursor.execute(sql_str)
    connection.commit()
    body.post_id = cursor.lastrowid
    return get_post_by_id_db(body.post_id)

def delete_post_db(post_id)-> None:
  assert post_id is not None # if tag.id is none then only we proceed 
  with connection.cursor() as cursor:
    cursor.execute("DELETE FROM posts WHERE postID = %s",post_id)
    connection.commit()

def update_post_db(post_id, body=None)-> None:# exact update, set to null if not present
  assert body.post_id is None
  t = get_post_by_id_db(post_id)
  assert t is not None
  with connection.cursor() as cursor:
    sql="UPDATE posts SET "
    for key in body.attribute_map:
      if key!="post_id":
        if eval('body.'+ key)==None:
          sql+=body.attribute_map[key]+"="+"Null"+","
        elif body.swagger_types[key]==str or body.swagger_types[key]==datetime.datetime:
          sql+=body.attribute_map[key]+"="+"'"+str(eval('body.'+ key))+"'"+","
        elif body.swagger_types[key]==bool:
          sql+=body.attribute_map[key]+"="+str(int(eval('body.'+ key)))+","
        else:
          sql+=body.attribute_map[key]+"="+str(eval('body.'+ key))+","
    sql=sql[:-1]
    sql+=" WHERE postID ="+str(t.post_id)
    cursor.execute(sql)
    connection.commit()
    body.id = cursor.lastrowid


def tags_from_post_id_db(post_id):
  with connection.cursor() as cursor:
    sql = 'SELECT * FROM tags WHERE postID=%s'
    cursor.execute(sql, (post_id))
    r = cursor.fetchall()
    if r is None:
      return None
    return [Tag.from_dict(i) for i in r]

def comments_from_post_id_db(post_id):
  with connection.cursor() as cursor:
    sql = 'SELECT * FROM comments WHERE postID=%s'
    cursor.execute(sql, (post_id))
    r = cursor.fetchall()
    if r is None:
      return None
    return [Comments.from_dict(i) for i in r]
  
def get_community_by_id_db(id:int) -> Optional[Communities]:
  if id==None:
    return None
  with connection.cursor() as cursor:
    sql = 'SELECT * FROM `communities` WHERE `communityID`=%s'
    cursor.execute(sql, (id))
    r = cursor.fetchone()
    if r is None:
      return None
    return Communities.from_dict(r)

def get_community_post_by_name_db(cn)->Optional[list[PostsDb]]:
  assert cn is not None
  cID = get_community_by_name_db(cn)
  if cID is None:
    return None
  cID=cID.community_id
  with connection.cursor() as cursor:
      sql="SELECT * FROM posts WHERE communityID = %s"
      cursor.execute(sql,(cID))
      r = cursor.fetchall()
      if r is None:
          return None
      return [PostsDb.from_dict(i) for i in r]

def get_user_by_id_db(id:int)->Optional[User]:
  with connection.cursor() as cursor:
      sql="SELECT * FROM users WHERE userID = %s"
      cursor.execute(sql,id)
      r = cursor.fetchone()
      if r is None:
          return None
      return User.from_dict(r)

  

  


