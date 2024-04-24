import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class StorePage:
    def __init__(self, browser):
        self.browser = browser

    def navigate_to(self):
        self.browser.get('http://localhost:3000/')
        time.sleep(1.5)
        element = self.browser.find_element(By.XPATH, "//a[contains(text(),'Магазин')]")
        element.click()
        time.sleep(1.5)

    def sort_by_price_desc(self):
        element = self.browser.find_element(By.XPATH, "//label[contains(text(),'Сортировать по:')]")
        element.click()
        time.sleep(1.5)
        element = self.browser.find_element(By.XPATH, "//option[@value='price']")
        element.click()
        time.sleep(1.5)
        element = self.browser.find_element(By.XPATH, "//label[contains(text(),'Направление:')]")
        element.click()
        time.sleep(1.5)
        element = self.browser.find_element(By.XPATH, "//option[@value='desc']")
        element.click()
        time.sleep(1.5)

    def open_book_detail(self, book_name):
        element = self.browser.find_element(By.XPATH, f"//h2[contains(text(),'{book_name}')]")
        element.click()
        time.sleep(1.5)

class AdminPanel:
    def __init__(self, browser):
        self.browser = browser

    def navigate_to(self):
        self.browser.get('http://localhost:3000/admin')
        time.sleep(1.5)

    def add_book(self, title, description, author, genre, year, price, photo_url):
        element = self.browser.find_element(By.XPATH, "//a[contains(text(),'Добавить книгу')]")
        element.click()
        time.sleep(1.5)

        self.browser.find_element(By.XPATH, "//input[@id='title']").send_keys(title)
        time.sleep(0.5)
        self.browser.find_element(By.XPATH, "//input[@id='description']").send_keys(description)
        time.sleep(0.5)
        self.browser.find_element(By.XPATH, "//input[@id='author']").send_keys(author)
        time.sleep(0.5)
        self.browser.find_element(By.XPATH, "//input[@id='genre']").send_keys(genre)
        time.sleep(0.5)
        self.browser.find_element(By.XPATH, "//input[@id='year']").send_keys(year)
        time.sleep(0.5)
        self.browser.find_element(By.XPATH, "//input[@id='price']").send_keys(price)
        time.sleep(0.5)
        self.browser.find_element(By.XPATH, "//input[@id='protoUrl']").send_keys(photo_url)
        time.sleep(0.5)
        self.browser.find_element(By.XPATH, "//button[contains(text(),'Добавить книгу')]").click()
        time.sleep(0.5)

    def edit_book(self, search_term, new_title):
        element = self.browser.find_element(By.XPATH, "//a[contains(text(),'Изменить книгу')]")
        element.click()
        time.sleep(0.5)
        element = self.browser.find_element(By.XPATH, "//input[@placeholder='Поиск по названию или автору']")
        element.send_keys(search_term)
        time.sleep(0.5)
        self.browser.find_element(By.XPATH, "//button[contains(text(),'Изменить')]").click()
        time.sleep(0.5)
        self.browser.find_element(By.XPATH, "//input[@id='title']").send_keys(new_title)
        time.sleep(0.5)
        self.browser.find_element(By.XPATH, "//button[contains(text(),'Сохранить изменения')]").click()
        time.sleep(0.5)

    def delete_book(self, search_term):
        element = self.browser.find_element(By.XPATH, "//a[contains(text(),'Удалить книгу')]")
        element.click()
        time.sleep(0.5)
        element = self.browser.find_element(By.XPATH, "//input[@placeholder='Поиск по названию или автору']")
        element.send_keys(search_term)
        time.sleep(0.5)
        self.browser.find_element(By.XPATH, "//button[contains(text(),'Удалить')]").click()
        time.sleep(0.5)


firefox_option = webdriver.FirefoxOptions()
firefox_option.add_argument('--start-maximized')
browser = webdriver.Firefox(options=firefox_option)

store_page = StorePage(browser)
admin_panel = AdminPanel(browser)

store_page.navigate_to()
store_page.sort_by_price_desc()
store_page.open_book_detail('Война и мир')

admin_panel.navigate_to()
admin_panel.add_book("Горе от ума", "Про горе от ума", "Александер Грибоедов", "Комедия", "1824", "3000", "https://content.img-gorod.ru/nomenclature/29/849/2984998-2.jpg")
WebDriverWait(browser, 10).until(EC.alert_is_present())
alert = browser.switch_to.alert
alert.dismiss()

admin_panel.edit_book("Горе от", "Горе от ума 2")
WebDriverWait(browser, 10).until(EC.alert_is_present())
alert = browser.switch_to.alert
alert.dismiss()
admin_panel.delete_book("Горе от")
WebDriverWait(browser, 10).until(EC.alert_is_present())
alert = browser.switch_to.alert
alert.dismiss()
