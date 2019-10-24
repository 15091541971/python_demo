
# coding: utf-8
'''
Created on 2019

@author: WangWei
'''
from tornado.httpclient import HTTPClient

def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response
if '__main__'==__name__:
    response=synchronous_fetch("http://www.tornadoweb.org/en/stable/guide/async.html")
    print(response.headers['Server'])
    print(response.body)