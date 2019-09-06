from Libs.Tools import HttpClass
#爸爸类（登录），继承http请求类
class LoginClass(HttpClass):
    #在登录这里就先拿到cookies
    #定义一个空的字典以备存放更新的cookies
    phpid = {
        'PHPSESSID': ''
    }

    def loginApi(self):
        #登录接口
        lgn_path='/index.php?ctl=user&act=dologin'
        #登录数据
        lgn_data={
            'email': 'admin01',
            'user_pwd':'R2hrTG5hQ1hEa0VUZ1lIYUJ3RlFURldyclRuSlF0QlVBeVluY0lkSGh2TXBvb3pnZ1YlMjV1NjVCOSUyNXU3RUY0MTIzNDU2YSUyNXU4RjZGJTI1dTRFRjY',
            'ajax': '1',
        }
        #登录
        lgn_result=self.sendHttp(path=lgn_path,data=lgn_data)
        #获取到cookies
        cookies = lgn_result.cookies['PHPSESSID']
        #更新定义的字典，把更新后的PHPSESSID的值传给cookies
        self.phpid['PHPSESSID'] = cookies