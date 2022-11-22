#import time
#
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#
#link = "http://suninjuly.github.io/simple_form_find_task.html"
#
#try:
#    browser = webdriver.Chrome()
#    browser.get(link)
#
#    input1 = browser.find_element("name", "first_name")
#    input1.send_keys("Ivan")
#    input2 = browser.find_element("name", "last_name")
#    input2.send_keys("Petrov")
#    input3 = browser.find_element("name", "firstname")
#    input3.send_keys("Smolensk")
#    input4 = browser.find_element("id", "country")
#    input4.send_keys("Russia")
#    button = browser.find_element("id", "submit_button")
#   button.click()
#
#finally:
#    time.sleep(30)
#    browser.quit()
#
#import time
#import math
#
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#
#link = "http://suninjuly.github.io/find_link_text"
#
#try:
#    browser = webdriver.Chrome()
#    browser.get(link)
#
#    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
#
#    link.click()
#
#    input1 = browser.find_element("name", "first_name")
#    input1.send_keys("Ivan")
#    input2 = browser.find_element("name", "last_name")
#    input2.send_keys("Petrov")
#    input3 = browser.find_element("name", "firstname")
#    input3.send_keys("Smolensk")
#    input4 = browser.find_element("id", "country")
#    input4.send_keys("Russia")
#    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#   button.click()
#
#finally:
#   time.sleep(15)
#   browser.quit()
#
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#
#try:
#    browser = webdriver.Chrome()
#    browser.get("http://suninjuly.github.io/huge_form.html")
#    elements = browser.find_elements(By.CSS_SELECTOR, "input")
#    for element in elements:
#            element.send_keys("Мой ответ")
#
#    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#    button.click()
#
#finally:
#    time.sleep(30)
#    browser.quit()
#
#
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#
#link = "http://suninjuly.github.io/find_xpath_form"
#
#try:
#    browser = webdriver.Chrome()
#    browser.get(link)
#
#    input1 = browser.find_element("name", "first_name")
#    input1.send_keys("1")
#    input2 = browser.find_element("name", "last_name")
#    input2.send_keys("2")
#    input3 = browser.find_element("name", "firstname")
#    input3.send_keys("3")
#    input4 = browser.find_element("id", "country")
#    input4.send_keys("4")
#
#    button = browser.find_element(By.XPATH, "/html/body/div/form/div[6]/button[3]")
#    button.click()
#
#finally:
#    time.sleep(30)
#    browser.quit()
#
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#
#try:
#    link = "http://suninjuly.github.io/registration2.html"
#    browser = webdriver.Chrome()
#    browser.get(link)
#
#    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
#    input1.send_keys("1")
#    input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
#    input2.send_keys("2")
#    input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
#    input3.send_keys("3")
#
#    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#    button.click()
#
#    time.sleep(1)
#
#    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#    welcome_text = welcome_text_elt.text
#
#    assert "Congratulations! You have successfully registered!" == welcome_text
#
#finally:
#    time.sleep(10)
#    browser.quit()
#
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#import math
#
#try:
#    link = "https://suninjuly.github.io/math.html"
#    browser = webdriver.Chrome()
#    browser.get(link)
#    def calc(x):
#        return str(math.log(abs(12*math.sin(int(x)))))
#    x_element = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/label/span[2]")
#    x = x_element.text
#    y = calc(x)
#    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/input")
#    input1.send_keys(y)
#    option1 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/input")
#    option1.click()
#    option2 = browser.find_element(By.XPATH, "/html/body/div/form/div[4]/input")
#    option2.click()
#    input2 = browser.find_element(By.XPATH, "/html/body/div/form/button")
#    input2.click()
#finally:
#    time.sleep(30)
#    browser.quit()
#
#from selenium import webdriver
#rom selenium.webdriver.common.by import By
#import math
#import time
#
#link = "http://suninjuly.github.io/get_attribute.html"
#
#try:
#    browser = webdriver.Chrome()
#    browser.get(link)
#    def calc(x):
#        return str(math.log(abs(12*math.sin(int(x)))))
#    treasure = browser.find_element(By.ID, "treasure")
#    treasure_checked = treasure.get_attribute("valuex")
#    x = treasure_checked
#    y = calc(x)
#    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div/div/input")
#    input1.send_keys(y)
#    option1 = browser.find_element(By.XPATH, "/html/body/div/form/div/div/div[2]/input[1]")
#    option1.click()
#    option2 = browser.find_element(By.XPATH, "/html/body/div/form/div/div/div[2]/input[3]")
#    option2.click()
#    input2 = browser.find_element(By.XPATH, "/html/body/div/form/div/div/button")
#    input2.click()
#finally:
#    time.sleep(30)
#    browser.quit()
#
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
#import time
#
#link = "http://suninjuly.github.io/selects1.html"
#
#try:
#    browser = webdriver.Chrome()
#    browser.get(link)
#    num1 = browser.find_element(By.XPATH, "/html/body/div/form/h2/span[2]").text
#    num2 = browser.find_element(By.XPATH, "/html/body/div/form/h2/span[4]").text
#    sum = (int(num1) + int(num2))
#    select = Select(browser.find_element(By.TAG_NAME, "select"))
#    select.select_by_visible_text(str(sum))
#    input = browser.find_element(By.XPATH, "/html/body/div/form/button").click()
#finally:
#   time.sleep(30)
#    browser.quit()
#
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#import math
#
#link = "http://suninjuly.github.io/execute_script.html"
#
#try:
#    browser = webdriver.Chrome()
#    browser.get(link)
#    x_element = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/label/span[2]")
#    x = x_element.text
#    def calc(x):
#        return str(math.log(abs(12*math.sin(int(x)))))
#    y = calc(x)
#    browser.execute_script("window.scrollBy(0, 100);")
#    input = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/input")
#    input.send_keys(y)
#    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/input").click()
#    input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[4]/input").click()
#    button = browser.find_element(By.XPATH, "/html/body/div/form/button").click()
#finally:
#    time.sleep(10)
#    browser.quit()
#
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#import os
#
#link = "http://suninjuly.github.io/file_input.html"
#
#try:
#    browser = webdriver.Chrome()
#    browser.get(link)
#    input1 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div/input[1]")
#    input1.send_keys(1)
#    input2 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div/input[2]")
#    input2.send_keys(2)
#    input3 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div/input[3]")
#    input3.send_keys(3)
#    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
#    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
#    element = browser.find_element(By.XPATH, "/html/body/div[1]/form/input")
#    element.send_keys(file_path)
#    time.sleep(1)
#    button = browser.find_element(By.XPATH, "/html/body/div[1]/form/button").click()
#finally:
#    time.sleep(10)
#    browser.quit()
#
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#import math
#
#link = "http://suninjuly.github.io/alert_accept.html"
#
#try:
#    browser = webdriver.Chrome()
#    browser.get(link)
#    button = browser.find_element(By.XPATH, "/html/body/form/div/div/button").click()
#    confirm = browser.switch_to.alert
#    confirm.accept()
#    def calc(x):
#        return str(math.log(abs(12*math.sin(int(x)))))
#    x_element = browser.find_element(By.XPATH, "/html/body/form/div/div/div/label/span[2]")
#    x = x_element.text
#    y = calc(x)
#    input = browser.find_element(By.XPATH, "/html/body/form/div/div/div/input")
#    input.send_keys(y)
#    button = browser.find_element(By.XPATH, "/html/body/form/div/div/button").click()
#finally:
#    time.sleep(10)
#    browser.quit()
#
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#import math
#
#link = "http://suninjuly.github.io/redirect_accept.html"
#
#try:
#    browser = webdriver.Chrome()
#    browser.get(link)
#    first_window = browser.window_handles[0]
#    button = browser.find_element(By.XPATH, "/html/body/form/div/div/button").click()
#    new_window = browser.window_handles[1]
#    browser.switch_to.window(new_window)
#    def calc(x):
#        return str(math.log(abs(12*math.sin(int(x)))))
#    x_element = browser.find_element(By.XPATH, "/html/body/form/div/div/div/label/span[2]")
#    x = x_element.text
#    y = calc(x)
#    input = browser.find_element(By.XPATH, "/html/body/form/div/div/div/input")
#    input.send_keys(y)
#    button = browser.find_element(By.XPATH, "/html/body/form/div/div/button").click()
#finally:
#    time.sleep(10)
#    browser.quit()
#
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium import webdriver
#import math
#import time
#
#link = "http://suninjuly.github.io/explicit_wait2.html"
#
#try:
#
#    browser = webdriver.Chrome()
#    browser.get(link)
#
#    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
#    browser.find_element(By.XPATH, "/html/body/div/div/div/button").click()
#    browser.execute_script("window.scrollBy(0, 400);")
#    def calc(x):
#        return str(math.log(abs(12*math.sin(int(x)))))
#    x_element = browser.find_element(By.XPATH, "/html/body/form/div/div/div/label/span[2]")
#    x = x_element.text
#    y = calc(x)
#    browser.find_element(By.XPATH, "/html/body/form/div/div/div/input").send_keys(y)
#    browser.find_element(By.XPATH, "/html/body/form/div/div/button").click()
#finally:
#    time.sleep(15)
#    browser.quit()
#
