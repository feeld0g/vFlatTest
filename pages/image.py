from appium.webdriver.common.appiumby import AppiumBy
from pages.base import BaseFunction


class ImagePage(BaseFunction):
    recognize_text_button = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="텍스트 인식하기"]')
    camera_button = (AppiumBy.ACCESSIBILITY_ID, "카메라")
    recognized_text_tab_button = (AppiumBy.ACCESSIBILITY_ID, "텍스트")

    def click_recognize_text_button(self):
        self.click_by_locator(self.recognize_text_button)

    def click_camera_button(self):
        self.click_by_locator(self.camera_button)

    def check_text_recognition_complete(self):
        if self.find_element_by_locator(self.recognized_text_tab_button) is not None:
            print("텍스트 인식 완료")