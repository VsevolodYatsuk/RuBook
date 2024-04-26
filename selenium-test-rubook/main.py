import time
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class StorePage:
    def __init__(self, browser):
        self.browser = browser

    def navigate_to(self):
        self.browser.get('http://localhost:3000/')
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Магазин')]"))).click()

    def sort_by_price_desc(self):
        sort_label = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(),'Сортировать по:')]")))
        sort_label.click()
        price_option = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//option[@value='price']")))
        price_option.click()
        direction_label = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(),'Направление:')]")))
        direction_label.click()
        desc_option = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//option[@value='desc']")))
        desc_option.click()

    def open_book_detail(self, book_name):
        book_element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, f"//h2[contains(text(),'{book_name}')]")))
        book_element.click()

class AdminPanel:
    def __init__(self, browser):
        self.browser = browser

    def navigate_to(self):
        self.browser.get('http://localhost:3000/admin')

    def add_book(self, title, description, author, genre, year, price, photo_url):
        add_book_button = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Добавить книгу')]")))
        add_book_button.click()

        title_input = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='title']")))
        title_input.send_keys(title)

        description_input = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='description']")))
        description_input.send_keys(description)

        author_input = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='author']")))
        author_input.send_keys(author)

        genre_input = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='genre']")))
        genre_input.send_keys(genre)

        year_input = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='year']")))
        year_input.send_keys(year)

        price_input = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='price']")))
        price_input.send_keys(price)

        photo_url_input = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='protoUrl']")))
        photo_url_input.send_keys(photo_url)

        add_button = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Добавить книгу')]")))
        add_button.click()

    def edit_book(self, search_term, new_title):
        edit_button = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Изменить книгу')]")))
        edit_button.click()

        search_input = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Поиск по названию или автору']")))
        search_input.send_keys(search_term)

        edit_button = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Изменить')]")))
        edit_button.click()

        title_input = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='title']")))
        title_input.send_keys(new_title)

        save_button = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Сохранить изменения')]")))
        save_button.click()

    def delete_book(self, search_term):
        delete_button = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Удалить книгу')]")))
        delete_button.click()

        search_input = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Поиск по названию или автору']")))
        search_input.send_keys(search_term)

        delete_button = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Удалить')]")))
        delete_button.click()

@pytest.mark.test
def test_store_page():
    firefox_option = webdriver.FirefoxOptions()
    firefox_option.add_argument('--start-maximized')
    browser = webdriver.Firefox(options=firefox_option)

    store_page = StorePage(browser)
    store_page.navigate_to()
    store_page.sort_by_price_desc()
    store_page.open_book_detail('Война и мир')

    browser.quit()

@pytest.mark.test
def test_admin_panel():
    firefox_option = webdriver.FirefoxOptions()
    firefox_option.add_argument('--start-maximized')
    browser = webdriver.Firefox(options=firefox_option)

    admin_panel = AdminPanel(browser)
    admin_panel.navigate_to()
    admin_panel.add_book("Горе от ума", "Про горе от ума", "Александер Грибоедов", "Комедия", "1824", "3000", "https://content.img-gorod.ru/nomenclature/29/849/2984998-2.jpg")
    WebDriverWait(browser, 10).until(EC.alert_is_present()).dismiss()

    admin_panel.edit_book("Горе от", "Горе от ума 2")
    WebDriverWait(browser, 10).until(EC.alert_is_present()).dismiss()

    admin_panel.delete_book("Горе от")
    WebDriverWait(browser, 10).until(EC.alert_is_present()).dismiss()

    browser.quit()

if __name__ == "__main__":
    pytest.main(["-s", "--alluredir=allure-results"])
