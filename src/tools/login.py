# -*- coding: utf-8 -*-
#登录模块
import urllib
import urllib2
import sys
sys.path.append("..")
from weibo import APIClient  #可以用pip install sinaweibopy命令，来安装weibo的python SDK
import config.myConfig as con

def login():
    print "logging on..."
    client = APIClient(app_key = con.APP_KEY, app_secret = con.APP_SECRET, redirect_uri = con.CALLBACK_URL)
    referer_url = client.get_authorize_url()
    cookies = urllib2.HTTPCookieProcessor()
    opener = urllib2.build_opener(cookies)
    urllib2.install_opener(opener)

    postdata = {
             "client_id": con.APP_KEY,
             "redirect_uri": con.CALLBACK_URL,
             "userId": con.USERID,
             "passwd": con.PASSWD,
             "isLoginSina": "0",
             "action": "submit",
             "response_type": "code",
             }

    headers = {
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0",
               "Host": "api.weibo.com",
               "Referer": referer_url
               }

    req  = urllib2.Request(
                           url = referer_url,
                           data = urllib.urlencode(postdata),
                           headers = headers
                           )
    try:
        resp = urllib2.urlopen(req)
        #获取最后32个字符
        code=resp.geturl()[-32:]
        #通过该code获取access_token，r是返回的授权结果
        r = client.request_access_token(code)  
        #将access_token和expire_in设置到client对象
        client.set_access_token(r.access_token, r.expires_in)
        print "login success!"
        return client
    except Exception, e:
        print 'login error!'
        print e