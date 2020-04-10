# InnerGhostBot
把微信家长群的消息偷到班级群去吧！

### 使用说明

##### 你所需要准备以下内容：

- qq群webhook key（指腾讯官方群WebHook工具，该工具仍在内测中
- smms key（sm.ms图床的key
- 腾讯云cos（由于webhook工具在内测中，微信的文件转发到QQ基于腾讯云cos服务提供的直链

##### 设置环境变量
TX_ID 腾讯云 secret id
TX_Key 腾讯云 secret key
TX_Region 腾讯云cos存储桶地域
Tx_Bucket 腾讯云cos存储通id
QQHook_Key qq群webhook key
smms_Token sm.ms图床 key

`python3 wx2qq.py`