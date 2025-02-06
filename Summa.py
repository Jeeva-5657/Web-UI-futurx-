from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
# options.add_argument('--headless') 
options.add_argument('--enable-unsafe-swiftshader')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox') 
chrome_driver_path ="C:/Users/JEEVA/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe"

service = Service(chrome_driver_path)  
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 30)

url="https://app.staging.futurx.in/"
driver.get(url)

#Test Case-1
try:
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "banner-image-container")))
    login = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'login-btn')]")))
    login.click()
    print("Success : Login Button Worked")

except:
    print("Error : Login Button Not Worked")  

time.sleep(4)

#Test Case-2
try:
    ul = driver.find_elements(By.CLASS_NAME, "auth0-lock-tabs")
    if ul:
        li_elements = ul[0].find_elements(By.TAG_NAME, "li")
        if len(li_elements) > 1:
            second_li = li_elements[1] 
            second_li.click()
        else:
            print("ERROR")
    else:
        print("Error")
except:
    print("ERROR")
time.sleep(4)

#dont remember
try:
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "auth0-lock-alternative-link")) )
    link.click()

except:
    print("Error")

#Don't Remember-Test
time.sleep(3)
try:
    mail=driver.find_element(By.ID,"1-email")#Blank-Test
    mail.send_keys(Keys.RETURN)
    error= driver.find_elements(By.CLASS_NAME, "auth0-lock-error-invalid-hint")
    if error:
        msg = error[0].text.strip()
        print("Error : ", msg)
    else:
         print("Success : Correct Email")

    time.sleep(2)

    mail=driver.find_element(By.ID,"1-email")#Invalid-Mail-Test
    mail.send_keys("12334")
    mail.send_keys(Keys.RETURN)
    error= driver.find_elements(By.CLASS_NAME, "auth0-lock-error-invalid-hint")
    if error:
        msg = error[0].text.strip()
        print("Error : ", msg)
    else:
        print("Success : Correct Email")

    driver.execute_script("arguments[0].value = '';", mail)
    time.sleep(2)
    
    mail=driver.find_element(By.ID,"1-email")#Valid-Mail-Test
    mail.send_keys("123@gmail.com")
    mail.send_keys(Keys.RETURN)
    error= driver.find_elements(By.CLASS_NAME, "auth0-lock-error-invalid-hint")
    if error:
        msg = error[0].text.strip()
        print("Error : ", msg)
    else:
        print("Success : Correct Email")

except:
    print("Error")

time.sleep(3)
driver.quit()