from appium.webdriver.common.appiumby import AppiumBy
from pages.base import BaseFunction


class SettingPage(BaseFunction):
    complete_button = (AppiumBy.XPATH, '//XCUIElementTypeOther[@name="완료"]')

    def click_complete_button(self):
        self.click_by_locator(self.complete_button)

    def get_text_recognition_token_count(self):
        text_recognition_token = self.find_element_by_locator((AppiumBy.XPATH, '//*[contains(@name, "텍스트 인식권")]'))
        text_recognition_token_count = int(text_recognition_token.text[9:].replace(",", ""))
        print(f"텍스트 인식권 수 : {text_recognition_token_count}")
        return text_recognition_token_count

    # noinspection PyMethodMayBeStatic
    def check_text_recognition_token_decreased(self, tokens1, tokens2):
        assert tokens2 == (tokens1 - 1), "텍스트 인식권 수가 감소하지 않음"
        print(f"텍스트 인식권 수 감소 ({tokens1} --> {tokens2}) 확인")