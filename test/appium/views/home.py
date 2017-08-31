from views.base_view import BaseViewObject
from views.base_element import *


class ContinueButton(BaseButton):

    def __init__(self, driver):
        super(ContinueButton, self).__init__(driver)
        self.locator = self.Locator.xpath_selector("//*[@text='Continue']")


class OkButton(BaseButton):

    def __init__(self, driver):
        super(OkButton, self).__init__(driver)
        self.locator = self.Locator.xpath_selector("//*[@text='OK']")


class TypeMessageEditBox(BaseEditBox):

    def __init__(self, driver):
        super(TypeMessageEditBox, self).__init__(driver)
        self.locator = \
            self.Locator.xpath_selector("//android.widget.EditText[@content-desc!='chat-message-input']")


class RequestPasswordIcon(BaseButton):

    def __init__(self, driver):
        super(RequestPasswordIcon, self).__init__(driver)
        self.locator = self.Locator.xpath_selector("//*[@content-desc='request-password']")


class HomeView(BaseViewObject):

    def __init__(self, driver):
        super(HomeView, self).__init__(driver)
        self.continue_button = ContinueButton(driver)
        self.ok_button = OkButton(driver)

        for i in self.ok_button, self.continue_button:
            try:
                i.click()
            except (NoSuchElementException, TimeoutException):
                pass

        self.type_message_edit_box = TypeMessageEditBox(driver)
        self.request_password_icon = RequestPasswordIcon(driver)
