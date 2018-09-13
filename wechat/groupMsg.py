# coding: utf-8
"""
@project = pythontest
@file = groupMsg
@author = liu_bo
@create_time = 2018/9/13 15:00
@describe = 群发助手
"""
import itchat
import time

itchat.auto_login(True)

SINCERE_WISH = u'祝%s中秋节快乐！\n%s'

message = []
friendList = itchat.get_friends(update=True)[1:]
for friend in friendList:
    # 如果是演示目的，把下面的方法改为print即可
    print(friend)
    str_msg = (SINCERE_WISH % (friend['DisplayName'] or friend['NickName'], friend['Signature']))
    print(str_msg)
    message.append(str_msg)
    # 如果是演示目的，把下面的方法改为print即可
    # itchat.send(REAL_SINCERE_WISH % (friend['DisplayName']
    #                                  or friend['NickName']), friend['UserName'])

    # time.sleep(.1)

itchat.send(str(message), 'filehelper')



# REAL_SINCERE_WISH = u'祝%s中秋节快乐！！'
#
# chatroomName = '继续一起聊bug'
# itchat.get_chatrooms(update=True)
# chatrooms = itchat.search_chatrooms(name=chatroomName)
# if chatrooms is None:
#     print(u'没有找到群聊：' + chatroomName)
# else:
#     chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
#     for friend in chatroom['MemberList']:
#         friend = itchat.search_friends(userName=friend['UserName'])
#         if friend is not None:
#             # 如果是演示目的，把下面的方法改为print即可
#             print(REAL_SINCERE_WISH % (friend['DisplayName']
#                                        or friend['NickName']), friend['UserName'])
#             time.sleep(.5)

