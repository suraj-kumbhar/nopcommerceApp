from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGenerator


class Test_001_Login:
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGenerator.log_generator()

    def test_homepage_title(self, setup):
        self.logger.info("************* Test_001_Login *********")
        self.logger.info("Verify homepage title test")
        self.driver = setup
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        expected_title = "Your store. Login"
        if actual_title == expected_title:
            self.driver.close()
            self.logger.info("homepage title test successful")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_homepage_title.png")
            self.driver.close()
            self.logger.error("homepage title test unsuccessful")
            assert False


    def test_login(self, setup):
        self.logger.info("Verify login test")
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
            self.logger.info("login test successful")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_login.png")
            self.driver.close()
            self.logger.error("login test unsuccessful")
            assert False
