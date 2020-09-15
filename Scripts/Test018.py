import allure
from selenium import webdriver
import time


class Test18:


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step('第一步')
    def test_001(self):
        print('\n 测试方法一')

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step('第二步')
    def test_002(self):
        print('\n 测试方法二')

    @allure.severity(allure.severity_level.NORMAL)
    @allure.step('第三步')
    def test_003(self):
        print('\n 测试方法三')
        assert False

    @allure.severity(allure.severity_level.MINOR)
    @allure.step('第四步')
    def test_004(self):
        print('\n 测试方法四')

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.step('第五步')
    def test_005(self):
        print('\n 测试方法五')



