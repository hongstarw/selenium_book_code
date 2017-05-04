# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class LoginDashboardAndCheckBalance(unittest.TestCase):
   def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.pingxx.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_dashboard_and_check_balance(self):
        driver = self.driver
        # open | / | 
        driver.get(self.base_url + "/")
        # assertTitle | Ping++ 聚合支付系统 | 支付宝 微信支付 分期 Apple Pay | 
        self.assertEqual(u"Ping++ 聚合支付系统 | 支付宝 微信支付 分期 Apple Pay", driver.title)
        # click | link=登入 | 
        driver.find_element_by_link_text(u"登入").click()
        # waitForTitle | 管理平台 | Ping++ | 
        for i in range(60):
            try:
                if u"管理平台 | Ping++" == driver.title: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        # store | ********** | username
        username = "**********"
        # store | ******** | password
        password = "********"
        # type | id=username | ${username}
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(username)
        # type | id=password | ${password}
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        # click | id=loginBtn | 
        driver.find_element_by_id("loginBtn").click()
        # 等待账户入口出现
        # waitForElementPresent | id=accountMenu | 
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "accountMenu"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        # verifyVisible | id=accountMenu | 
        try: self.assertTrue(driver.find_element_by_id("accountMenu").is_displayed())
        except AssertionError as e: self.verificationErrors.append(str(e))
        # click | //div[@id='accountMenu']/span | 
        driver.find_element_by_xpath("//div[@id='accountMenu']/span").click()
        # click | link=企业账户 | 
        driver.find_element_by_link_text(u"企业账户").click()
        # waitForVisible | class=text-blue balance_charge | 
        # ERROR: Caught exception [Error: unknown strategy [class] for locator [class=text-blue balance_charge]]
        # waitForElementPresent | css=a.active | 
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "a.active"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        # click | css=a.active | 
        driver.find_element_by_css_selector("a.active").click()
        # waitForVisible | css=span.text-blue.balance_details | 
        for i in range(60):
            try:
                if driver.find_element_by_css_selector("span.text-blue.balance_details").is_displayed(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        # click | css=span.text-blue.balance_details | 
        driver.find_element_by_css_selector("span.text-blue.balance_details").click()
        # 等待余额明细可见
        # waitForElementPresent | id=balance_details | 
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "balance_details"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
