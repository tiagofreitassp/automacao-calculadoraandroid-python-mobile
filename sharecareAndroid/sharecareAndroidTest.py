import unittest
from sharecareAndroid import sharecareAndroidPage, baseTest

p = sharecareAndroidPage
b = baseTest

class sharecareAndroidTest(unittest.TestCase):
    def setUp(self):
        b.criarDriver(self)

    def tearDown(self):
        b.fecharDriver(self)

    def test1_registreSe(self):
        p.registreSe(self,"Chapolin","Colorado","ch.col@gmail.com","18/07/1980","M","01451001","123@Sharecare")

    def test2_login(self):
        p.login(self,"user.zero@outlook.com","Sharecare@2018")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(sharecareAndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)