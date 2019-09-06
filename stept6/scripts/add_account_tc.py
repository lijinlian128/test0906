from po.MyP2P.MyAccount import MyAccountClsaa
from Libs.Tools import VerifyClass

class TestClass(VerifyClass):
    def setUp(self):
        self.mc=MyAccountClsaa()

    def test_success001(self):
        result=self.mc.creditApi()
        self.checkTextData(result,'操作成功',200)

if __name__ == '__main__':
        ...