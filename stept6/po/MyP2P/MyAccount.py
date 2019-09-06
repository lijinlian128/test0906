from Libs.Common import LoginClass

class MyAccountClsaa(LoginClass):
    def creditApi(self):
        # 申请信用额度
        credit_path = '/member.php?ctl=uc_deal_quota&act=do_add_quota'
        credit_data = {
            'name': '申请额度',
            'borrow_amount': '1000',
            'description': '申请1000',
            'file_upload_count': '3',
        }
        self.loginApi()
        credit_result = self.sendHttp(path=credit_path, data=credit_data, cookies=self.phpid)
        return credit_result