from pageObjects.LoginPage import LoginPage


class Test_001_Login:
    base_url = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homepage_title(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        expected_title = "Your store. Login"
        if actual_title == expected_title:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/test_homepage_title.png")
            self.driver.close()
            assert False


    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        actual_title = self.driver.title
        expected_title = "Dashboard / nopCommerce administration"
        if actual_title == expected_title:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/test_login.png")
            self.driver.close()
            assert False
