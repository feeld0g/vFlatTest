from appium.webdriver.common.appiumby import AppiumBy
from pages.base import BaseFunction


class CameraPage(BaseFunction):
    shutter_button = (AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="vFlat Scan"]/XCUIElementTypeWindow[1]/\
    XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/\
    XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]')
    recent_image = (AppiumBy.CLASS_NAME, "XCUIElementTypeImage")
    setting_button = (AppiumBy.ACCESSIBILITY_ID, "더 보기")

    def click_shutter_button(self):
        self.click_by_locator(self.shutter_button)

    def click_recent_image(self):
        self.click_by_locator(self.recent_image)

    def click_setting_button(self):
        self.click_by_locator(self.setting_button)