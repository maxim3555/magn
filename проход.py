import os
import threading
import time
from selenium.webdriver.firefox.service import Service

from webdriver_manager.firefox import GeckoDriverManager

import threading
import openpyxl
import requests
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
schet =1
schet1 = 1

book = openpyxl.open(r"telegramm_eвропром.xlsx")
list2 = book.active
print('начал')
def searh_po_slovo(driver, slovo, timeout):
    elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{slovo}')]")
    if elements:
        last_element = elements[-1]
        try:
            # Ждем, пока элемент станет кликабельным
            WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(last_element))
            driver.execute_script("arguments[0].click();", last_element)
        except Exception as e:
            print(f"Ошибка при клике на элемент: {e}")


def search_element_Xpath(driver, element, timeout):
    try:
        button = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, element)))
        driver.execute_script("arguments[0].scrollIntoView();", button)
        driver.execute_script("arguments[0].click();", button)
    except TimeoutException:
        print("Ошибка: Время ожидания загрузки элемента истекло.")


def search_element_Ypath_and_vsravka_text(driver, element, timeout, text):
    try:
        button = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, element)))
        button.click()
        button.send_keys(text)
        button.send_keys(Keys.RETURN)
    except Exception as e:
        print(f"An error occurred: {e}")


def poisk_elementov_click111(driver, element, t):
    TIME_TO_LOOP = t
    start = time.time()
    schetchik = 0
    spisok_element = element
    print(spisok_element)
    while time.time() < start + TIME_TO_LOOP:
        try:
            for i in spisok_element:
                print(i)
                elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{i}')]")
                # last_element = element[-1]
                if elements:
                    for g in elements:
                        print(f"Элемент найден в {i}")
                        # WebDriverWait(driver, 0.1).until(EC.element_to_be_clickable(last_element))
                        # driver.execute_script("arguments[0].scrollIntoView();", elements)
                        driver.execute_script("arguments[0].click();", g)
                        # r.click()
                        # driver.execute_script("arguments[0].scrollIntoView();", elements)
                        # driver.execute_script("arguments[0].click();", elements)
                        time.sleep(2)
                        schetchik += 1
                        # spisok_element.remove(i)

                        # continue
                if len(spisok_element) == 0:
                    break
        except Exception as e:
            print(f"Жду: {e}")


def poisk_elementov_click(driver, element, t):
    TIME_TO_LOOP = t
    start = time.time()
    schetchik = 0
    spisok_element = element
    print(spisok_element)
    while time.time() < start + TIME_TO_LOOP:
        try:
            for i in spisok_element:
                #print(i)
                elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{i}')]")
                # last_element = element[-1]
                if elements:
                    for g in elements:
                        print(f"Элемент найден в {i}")
                        # WebDriverWait(driver, 0.1).until(EC.element_to_be_clickable(last_element))
                        driver.execute_script("arguments[0].scrollIntoView();", g)
                        driver.execute_script("arguments[0].click();", g)
                        # r.click()
                        # driver.execute_script("arguments[0].scrollIntoView();", elements)
                        # driver.execute_script("arguments[0].click();", elements)
                        time.sleep(2)
                        schetchik += 1
                        spisok_element.remove(i)

                        # continue
                if len(element) == 0:
                    break
        except Exception as e:
            print(f"Жду: {e}")


def searh_po_slovo(driver, slovo, timeout):
    elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{slovo}')]")
    if elements:
        last_element = elements[-1]
        try:
            # Ждем, пока элемент станет кликабельным
            WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(last_element))
            driver.execute_script("arguments[0].click();", last_element)
        except Exception as e:
            print(f"Ошибка при клике на элемент: {e}")
def send_msg(photo):
    token = "5976486278:AAHql7K0uYyIUu6wfbSwPvI6J4LUJf_2AjE"
    chat_id = "1979830722"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + photo
    results = requests.get(url_req)

def magnit_kupon(photo):
    chat_id = "1979830722"
    token = "5976486278:AAHql7K0uYyIUu6wfbSwPvI6J4LUJf_2AjE"
    #image = pyautogui.screenshot(r'kuponchik.jpg', region=(664, 46, 589, 941))
    files = {'photo': open(photo, 'rb')}
    url_req = requests.post('https://api.telegram.org/bot5976486278:AAHql7K0uYyIUu6wfbSwPvI6J4LUJf_2AjE/sendPhoto?chat_id=1979830722',files=files)

def regictracia(driver):
    global schet

    # Открываем файл и считываем его содержимое

    link1='https://anketolog.ru/s/899517/YtsX5Ktp'


    try:
        driver.get(link1)
        time.sleep(2)
#начать
        search_element_Xpath(driver, '//*[@id="survey"]/div/div/form/div[2]/button', 5)
#1
        time.sleep(1.5)

        search_element_Xpath(driver, '//*[@id="survey"]/div/div/form/div[1]/div/div[2]/div/div[1]/label[1]/span', 5)
        search_element_Xpath(driver, '//*[@id="survey"]/div/div/form/div[2]/button[2]', 5)
#2
        time.sleep(1.5)
        search_element_Xpath(driver, '//*[@id="survey"]/div/div/form/div[1]/div/div[2]/div/div[1]/label[4]/span', 5)
        search_element_Xpath(driver, '//*[@id="survey"]/div/div/form/div[2]/button[2]', 5)
#3
        time.sleep(1.5)
        search_element_Xpath(driver, '//*[@id="survey"]/div/div/form/div[1]/div/div[2]/div/div[1]/label[2]/span', 5)
        search_element_Xpath(driver, '//*[@id="survey"]/div/div/form/div[2]/button[2]', 5)
#4
        time.sleep(1.5)
        search_element_Xpath(driver, '//*[@id="survey"]/div/div/form/div[1]/div/div[2]/div/div[1]/label[2]/span', 5)
        search_element_Xpath(driver, '//*[@id="survey"]/div/div/form/div[2]/button[2]', 5)
#5
        time.sleep(1.5)
        search_element_Xpath(driver, '//*[@id="survey"]/div/div/form/div[1]/div/div[2]/div/div[1]/label[4]/span', 5)
        search_element_Xpath(driver, '//*[@id="survey"]/div/div/form/div[2]/button[2]', 5)
#ЗАВЕРШИТЬ НОМЕР
        #search_element_Xpath(driver, '//*[@id="form-control-phone-12223455"]', 5)
        text_number = str(list2['A'][schet].value)
        text_number = f'+{text_number}'
        print(text_number)
        search_element_Ypath_and_vsravka_text(driver, '//*[@id="form-control-phone-12223455"]', 5, text_number)


        search_element_Xpath(driver, '//*[@id="survey"]/div/div/form/div[2]/button[2]', 5)
        time.sleep(5)
    except Exception as e:
        print(f"An error occurred: {e}")
        # schet -= 1


def upload_process():
    try:
        from selenium import webdriver
        from selenium.webdriver.firefox.options import Options
        from fake_useragent import UserAgent

        ua = UserAgent()
        random_user_agent = ua.random
        options = Options()

        # Опции для ускорения загрузки
        options.set_preference("permissions.default.image", 2)  # Отключение загрузки изображений
        # options.set_preference("javascript.enabled", False)  # Отключение JavaScript (если это возможно)
        # options.set_preference("network.http.use-cache", True)  # Использовать кэш
        options.set_preference("general.useragent.override", random_user_agent)  # Устанавливаем случайный User-Agent
        #options.set_preference("dom.webdriver.enabled", False)
        # options.set_preference("platform.override", "android")
        #options.add_argument("--headless")  # Запуск в безголовом режиме
        #options.profile = profile_path
        service = Service(GeckoDriverManager().install())

        # driver = webdriver.Firefox(service=service)
        driver = webdriver.Firefox(service=service, options=options)


        # driver.maximize_window()
        # time.sleep(20000)

        print('игра и взять ссылку')
        regictracia(driver)
        # time.sleep(5)



    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


while True:
    num_threads = 10  # Количество потоков, которые вы хотите запустить одновременно

    threads = []  # Список для хранения потоков
    try:

        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            # Запускаем 10 потоков
            for _ in range(num_threads):
                executor.submit(upload_process)  # Добавляем задачу в пул потоков

        schet += 1

        time.sleep(0.1)  # Небольшая задержка, чтобы не нагружать процессор
    except KeyboardInterrupt:

         print("Скрипт был остановлен. Закрываю потоки...")

    if schet ==13:
        schet=1