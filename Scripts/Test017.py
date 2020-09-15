import allure
from selenium import webdriver


class Test17:

    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.baidu.com')

    @allure.step('输入abc')
    def one(self):
        print('\n abc')

    @allure.step('测试方法')
    def test_001(self):
        self.one()
        allure.attach(self.driver.get_screenshot_as_png(), '百度截图', allure.attachment_type.PNG)
        print('\n---test_001')
        assert True
