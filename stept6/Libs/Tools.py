import requests
import unittest
#爷爷类
class HttpClass(object):
    #把host抽取出来
    host='http://localhost'
    #统一调用http请求方法
    def sendHttp(self,path,method='post',**kwargs):
        url='{}{}'.format(self.host,path)
        result=requests.request(method,url=url,**kwargs)
        return result

class VerifyClass(unittest.TestCase):

    #校验text值
    def checkTextData(self,result,expectValue,expectCode):
        self.assertEqual(result.status_code,expectCode)
        self.assertIn(expectValue,result.text)

    # 校验Json值
    def checkJsonData(self,result,expectKey,expectValue,expectCode):
        self.assertEqual(result.status_code,expectCode)
        self.assertIn(result.json().get(expectKey),expectValue)