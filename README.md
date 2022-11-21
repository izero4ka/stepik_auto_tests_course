# stepik_auto_tests_course
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
