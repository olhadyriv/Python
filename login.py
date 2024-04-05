import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
#Вводимо логін, пароль та к-сть днів підписки
email = input("Enter your email: ")
password = input("Enter your password: ")
days = input("Enter a number of days of subscription: ")

#Викликаємо драйвер Google Chrome на максимальному розширенні екрана з затримкою в 1 секунду
options = Options()
options.add_argument('--start-maximized')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://freevpnplanet.com/login/")
time.sleep(1)

#Прописується введений юзером аргумент зі змінної "email" у поле "Enter email"
user_mail = (driver.find_element(By.XPATH, '//*[@id="__layout"]/div/main/div[2]/div[1]/div[1]/div[2]/div/label/input')
             .send_keys(email))

#Прописується введений юзером аргумент зі змінної "password" у поле "Enter password"
user_pass = (driver.find_element(By.XPATH,'//*[@id="__layout"]/div/main/div[2]/div[1]/div[1]/div[3]/div/label/input')
             .send_keys(password))

#Клік на кнопку "Login" і затримка в 3 секунди
login_button = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/main/div[2]/div[1]/div[1]/button').click()
time.sleep(3)

#Забираємо текстове значення з поля "Number of days" і затримка 2 секунди перед закриттям браузера
subscription = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/'
                                             'div[2]/div/div[2]/b').text
time.sleep(2)

driver.close()
driver.quit()

#Виводимо текст при умові співпадіння значень аргументу змінної "days" з даними змінної "Subscription"
if days == subscription:
    print("The number of your subscription days is: " + str(days))
# Виводимо текст при умові різних значень аргументу змінної "days" і даних змінної "Subscription"
assert days == subscription, "The correct number of your subscription days is: " + str(subscription)

