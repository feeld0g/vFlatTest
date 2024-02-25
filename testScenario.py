import unittest
import time

from appium import webdriver
from appium.options.common import AppiumOptions

from pages.image import ImagePage
from pages.camera import CameraPage
from pages.setting import SettingPage


class TestDecreaseTextRecognitionToken(unittest.TestCase):
    def setUp(self):
        appium_server_url = "http://localhost:4724"
        capabilities = AppiumOptions().load_capabilities({
        'platformName': 'iOS',
        'appium:platformVersion': '17.3',
        'automationName': 'XCUITest',
        'appium:udid': '00008120-000144262E40C01E',
        'noReset': True
    })
        self.driver = webdriver.Remote(appium_server_url, options=capabilities)
        self.image_page = ImagePage(self.driver)
        self.camera_page = CameraPage(self.driver)
        self.setting_page = SettingPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_decrease_text_recognition_token(self):
        self.camera_page.click_setting_button()
        tokens1 = self.setting_page.get_text_recognition_token_count()  # 기존의 텍스트 인식권 수 확인
        self.setting_page.click_complete_button()
        self.camera_page.click_shutter_button()  # 이미지 촬영
        time.sleep(2)
        self.camera_page.click_recent_image()
        self.image_page.click_recognize_text_button()  # 텍스트 인식
        self.image_page.check_text_recognition_complete()
        self.image_page.click_camera_button()
        self.camera_page.click_setting_button()
        tokens2 = self.setting_page.get_text_recognition_token_count()  # 현재의 텍스트 인식권 수 확인
        self.setting_page.check_text_recognition_token_decreased(tokens1, tokens2)  # 텍스트 인식권 수 감소 확인
        self.setting_page.click_complete_button()
