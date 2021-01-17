from selenium.webdriver import ActionChains
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = Chrome()

Chrome(executable_path='/usr/local/bin/chromedriver')
def site_login(username,pwd,line) :

    number1 = line + 3
    number1 = str(number1)

    number2 = line + 1 
    number2 = str(number2)

    number3 = line + 2
    number3 = str(number3)

    driver.get('https://accounts.hetzner.com/login')
    driver.find_element_by_id('_username').send_keys(username)
    driver.find_element_by_id('_password').send_keys(pwd)
    driver.find_element_by_id('submit-login').click()
    driver.get('https://robot.your-server.de/server')
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div[2]/div/div[2]/div/div["+number1+"]/table")))
        
    finally:
        driver.find_element_by_xpath('/html/body/main/section/div[2]/div/div[2]/div/div['+number1+']/table').click()
    
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div[2]/div/div[2]/div/div["+number1+"]/div/div[1]/ul/li[2]")))
        
    finally:
        driver.find_element_by_xpath('/html/body/main/section/div[2]/div/div[2]/div/div['+number1+']/div/div[1]/ul/li[2]').click()
    
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div[2]/div/div[2]/div/div["+number1+"]/div/div[3]/form/table/tbody/tr["+number2+"]/td[2]/ul/li[2]/input")))
       
    finally:
        driver.find_element_by_xpath('/html/body/main/section/div[2]/div/div[2]/div/div['+number1+']/div/div[3]/form/table/tbody/tr['+number2+']/td[2]/ul/li[2]/input').click()
    
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div[2]/div/div[2]/div/div["+number1+"]/div/div[3]/form/table/tbody/tr["+number3+"]/td/input[3]")))
    finally:
        driver.find_element_by_xpath('/html/body/main/section/div[2]/div/div[2]/div/div['+number1+']/div/div[3]/form/table/tbody/tr['+number3+']/td/input[3]').click()
      
    
    driver.get('https://accounts.hetzner.com/logout')
    driver.quit()


site_login('example@yahoo.com','12345',2)








