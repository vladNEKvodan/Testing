import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver = webdriver.Chrome("C:\Users\maksa\PycharmProjects\pythonProject2\venv\Scripts")
driver.get('https://bungiestore.com')
search_box = driver.find_element(By.XPATH,
                                 '//*[@id="chrome-search"]')
search_box.send_keys('shopping bag')
time.sleep(1)
search_button = driver.find_element(By.XPATH,
                                    '//*[@id="chrome-sticky-header"]/div[1]/div/button')
search_button.click()
answer = driver.find_element(By.XPATH,
                             '//*[@id="search-term-banner"]/p[2]')
if answer.text != u'My Bag':
    print(datetime.datetime.now(), "Waited answer  %r" % answer.text)
else:
    print("Waited answer ", answer.text, " not found")
time.sleep(2)
sort_button = driver.find_element(By.XPATH,
                                  '//*[@id="plp"]/div/div[2]div/div[1]/div/button')
time.sleep(1)
sort_button.click()
time.sleep(1)
type_sort = driver.find_element(By.XPATH,
                                '//*[@id="plp"]/div/div/div/div/li/div/label/div')
type_sort.click()
time.sleep(1)
sort_button.click()
print(datetime.datetime.now(), 'Sort was complete')
sell_box = driver.find_element(By.XPATH,
                               '//*[@id="product-412388154"]/a')
sell_box.click()
time.sleep(1)
wish_button = driver.find_element(By.XPATH,
                                  '//*[@id="product-save"]/div/button')
wish_button.click()
time.sleep(1)
wish_list_button = driver.find_element(By.XPATH,
                                       '//*[@id="chrome-sticky-header"]/div[1]/div/ul/li[2]/a')
wish_list_button.click()
print(datetime.datetime.now(), 'Product was pre-purchased')
time.sleep(1)
sell_box2 = driver.find_element(By.XPATH,
                                '//*[@id="saved-lists-app"]/main/div/div[1]/section/ol/li/div/div/div/a')
sell_box2.click()
time.sleep(0.5)
add_bag_button = driver.find_element(By.XPATH,
                                     '//*[@id="product-add-button"]')
add_bag_button.click()
time.sleep(0.5)
bag_button = driver.find_element(By.XPATH,
                                 '//*[@id="chrome-sticky-header"]/div[1]/div/ul/li[3]/a')
bag_button.click()
time.sleep(3)
print(datetime.datetime.now(), 'Product added in bag')
del_button = driver.find_element(By.XPATH,
                                 '//*[@id="bagApp"]/div[1]/bag-group-list/li/bag-item-list/ul/bag-remove/div/button')
del_button.click()
time.sleep(5)
print(datetime.datetime.now(), 'Product deleted from bag')
insta_button = driver.find_element(By.XPATH,
                                   '//*[@id="chrome-footer"]/footer/li[2]/a')
insta_button.click()
print(datetime.datetime.now(), 'Button link correct')
time.sleep(15)
driver.quit()