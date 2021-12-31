import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from support.Browser import Browser
from support.Credentials import Credentials
from selenium.webdriver.common.by import By


class Functions(Browser):
    def __init__(self):
        super().__init__()
        self.wait = None
        self.credentials = None

    def access_page(self):
        self.get_chrome()
        self.driver.get('https://mercadolivre.com.br')
        self.credentials = Credentials()
        self.wait = WebDriverWait(self.driver, 10)

    def access_login(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a[data-link-id="login"]').click()

    def click_btn_continuar(self):
        self.driver.find_element(By.CSS_SELECTOR,
                                 'button[class="andes-button andes-button--large andes-button--loud andes-button--full-width"]').click()

    def click_btn_entrar(self):
        self.driver.find_element(By.ID, 'action-complete').click()

    def click_zipcode(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a[class="nav-menu-cp nav-menu-cp-logged"]').click()

    def get_title_page(self, title_expected):
        self.wait.until(EC.title_is(title_expected))
        title = self.driver.title
        self.driver.quit()
        return title

    def mouse_over_menu(self, menu_name):
        try:
            element = self.driver.find_element(By.LINK_TEXT, menu_name)
            action = ActionChains(self.driver).move_to_element(element)
            action.perform()
        except Exception as e:
            print(e)
            raise

    def select_option_menu(self, name_option):
        try:
            element = self.driver.find_element(By.LINK_TEXT, name_option)
            self.wait.until(EC.element_to_be_clickable(element))
            action = ActionChains(self.driver).move_to_element(element)
            action.click()
            action.perform()
        except Exception as e:
            print(e)
            raise

    def set_user_login(self):
        try:
            self.driver.find_element(By.ID, 'user_id').send_keys(self.credentials.user)
        except Exception as e:
            print(e)
            raise

    def set_password_login(self):
        try:
            self.driver.find_element(By.ID, 'password').send_keys(self.credentials.password)
        except Exception as e:
            print(e)
            raise
