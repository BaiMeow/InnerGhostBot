# -*- coding=utf-8 -*-

import requests
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import os

webhook_url = "https://app.qun.qq.com/cgi-bin/api/hookrobot_send"
mirror_url = "https://sm.ms/api/v2/upload"
suo_url = "http://m.6du.in/api_mobileweb_json.php"
# qq群webhook key
Key = os.getenv('QQHook_Key')
# smms key
API_token = os.getenv('smms_Token')
# 腾讯云cos
Secret_id = os.getenv('TX_ID')
Secret_key = os.getenv('TX_Key')
Region = os.getenv('TX_Region')
Bucket = os.getenv('Tx_Bucket')

header = {"Authorization": API_token}

config = CosConfig(Region=Region, SecretId=Secret_id, SecretKey=Secret_key)
client = CosS3Client(config)


def SendtoQQ(name, text):
    print("%s:%s" % (name, text))
    json_data = {"content": [{"type": 0, "data": ""}]}
    json_data["content"][0]["data"] = "%s:\n%s" % (
        name, text)
    url_params = {'key': Key}
    with requests.post(
            webhook_url, json=json_data, params=url_params) as respone:
        # 不是很清楚原因但是，目前成功发送的http状态码确实是500，200OK反而是失败
        if respone.status_code != 500:
            print(respone.reason)


def SuoURL(url):
    with requests.get(
            url=suo_url, params={'action': 'Create', 'url': url}) as respone:
        return respone.json()['url']


def Upload_image(path):
    f = open(path, 'rb')
    data = {"smfile": f}
    return requests.post(mirror_url, headers=header, files=data)


def Upload_file(path):
    with open(path, 'rb') as fp:
        response = client.put_object(
            Bucket=Bucket,
            Body=fp,
            Key=path,
            StorageClass='STANDARD',
            EnableMD5=False
        )
    print(response)
    return 'https://'+Bucket+'.cos.'+Region+'.myqcloud.com/'+path
