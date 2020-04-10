# -*- coding=utf-8 -*-

import itchat
import net
from itchat.content import TEXT, PICTURE, ATTACHMENT, RECORDING, SHARING


@itchat.msg_register(
    [TEXT, PICTURE, ATTACHMENT, RECORDING, SHARING], isGroupChat=True)
def text_handler(msg):
    name = msg.actualNickName,
    print("From:%s" % name)  # 打印收到的群消息的来源的识别码
    if name != group_id:
        return
    if msg.type == TEXT:
        net.SendtoQQ(msg.actualNickName, msg['Text'])
    elif msg.type == SHARING:
        net.SendtoQQ(msg.actualNickName, msg['Text']+msg.url)
    else:
        return


@itchat.msg_register([PICTURE, ATTACHMENT], isGroupChat=True)
def sharing_handler(msg):
    name = msg.user.userName
    print("From:%s" % name)  # 打印收到的群消息的来源的识别码
    if name != group_id:
        return
    path = "./files/"+msg.fileName
    msg.download(path)
    if msg.type == PICTURE:
        respone = net.Upload_image(path)
        data = respone.json()
        if respone.status_code == 200:
            if data['code'] == 'image_repeated':
                net.SendtoQQ(name, '[图片]\n'+net.SuoURL(data['images']))
            else:
                net.SendtoQQ(name, '[图片]\n'+net.SuoURL(data['data']['url']))
        print(data['code'])
        respone.close()
    elif msg.type == ATTACHMENT:
        url = net.Upload_file(path)
        net.SendtoQQ(name, '[文件]\n'+msg.fileName+'\n'+net.SuoURL(url))
        return


itchat.auto_login(enableCmdQR=2, hotReload=True)
chatroom_list = itchat.search_chatrooms(name="高二")
# 家长群识别码
group_id = chatroom_list[0].UserName
print("groupid:%s" % group_id)
itchat.run()
