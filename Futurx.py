from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager
import tempfile

options = Options()
# options.add_argument('--headless')  
options.add_argument('--enable-unsafe-swiftshader')
options.add_argument('--disable-gpu')
options.add_argument('--private')  
user_data_dir = tempfile.mkdtemp()

options.add_argument(f"user-data-dir={user_data_dir}") 

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 30)

url="https://app.staging.futurx.in/"
driver.get(url)


#Test Case-1(Login-Button)
print("\nTesting-1 : Login-Button")
try:
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "banner-image-container")))
    login = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'login-btn')]")))
    login.click()
    print("Success : Login Button Worked")

except:
    print("Error : Login Button Not Worked")    

#Test Case-2(Email-Tests && Google-Button-Check)
print("\nTesting-2 : Email and Google-Button")
try:
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "auth0-lock-header")))
    google = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-provider='google-oauth2']")))
    google.click()
    print("Success : Google Button Worked")
    email1=""
    email2="jeeva@gmail.com"
    email3="221da026@drngpasc.ac.in"
    email = driver.find_element(By.NAME, "identifier")
    email.send_keys("")
    email.send_keys(Keys.RETURN)
    time.sleep(2)
    email.clear()
    msg=driver.find_element(By.CLASS_NAME,"Ekjuhf.Jj6Lae").text.strip()
    print("Msg for Blank-mail:",msg)
    email.send_keys(email2)
    email.send_keys(Keys.RETURN)
    time.sleep(2)
    email.clear()
    msg=driver.find_element(By.CLASS_NAME,"Ekjuhf.Jj6Lae").text.strip()
    print("Msg for invalid-mail:",msg)
    email.send_keys(email3)
    email.send_keys(Keys.RETURN)
    time.sleep(2)
    print("Email-Verified")
except:
    print("Error : Google Button Not Worked")

#Test Case-3(Password-Tests)
print("\nTesting-3 : Passwords")
try:
    pas=" "
    pass1="123456"
    pass2="jEEVA@9965"
    password=driver.find_element(By.NAME,"Passwd")
    password.send_keys(pas)
    password.send_keys(Keys.RETURN)
    time.sleep(2)
    password.clear()
    msg=driver.find_element(By.CLASS_NAME,"Ly8vae.uSvLId").text.strip()
    print("Error : ",msg)
    password.send_keys(pass1)
    password.send_keys(Keys.RETURN)
    msg=driver.find_element(By.CLASS_NAME,"Ly8vae.uSvLId").text.strip()
    print("Error : ",msg)
    time.sleep(2)
    password.clear()
   
    password.send_keys(pass2)
    password.send_keys(Keys.RETURN)
    driver.back()
    driver.back()
    print("Success : Login-Successfully")
except:
    print("Error : Login-Failed")

#Test Case-4(FaceBook-Button-Check)
print("\nTesting-4 : FaceBook-Button")
try:
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "auth0-lock-header")))
    facebook = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-provider='facebook']")))
    facebook.click()
    print("Success : FaceBook Button Worked")
    driver.back()
except:
    print("Error : FaceBook Button Not Worked")

#Test Case-5(Don't Remember-Check)
print("Testing-5 : Don't Remember Password")
try:
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "auth0-lock-alternative-link")) )
    link.click()
    
except:
    print("Error : Don't Remember Button not working")

#Test Case-6(Don't-Remember-Values-Test)
print("\nTesting-6 : Don't-Remember-Values-Test")
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

#Test-Case-7(Enter-Values)
print("\nTesting-7 : Enter Values")
try:
    # Both-Blank-Case
    time.sleep(2)
    a = ""
    b = ""
    email = driver.find_element(By.ID, "1-email")
    password = driver.find_element(By.ID, "1-password")
    email.send_keys(a)
    password.send_keys(b)
    login_button = driver.find_element(By.NAME, "submit")
    login_button.click()

    error = driver.find_elements(By.XPATH, "//*[@id='auth0-lock-error-msg-password']/div")
    error1 = driver.find_elements(By.XPATH, "//*[@id='auth0-lock-error-msg-email']/div")
    if error:
        msg = error[0].text.strip()
        print(msg)
    else:
        print("No-Error in the Password")

    if error1:
        msg = error1[0].text.strip()
        print(msg)
    else:
        print("No-Error in the Email")
    time.sleep(2)

    driver.execute_script("arguments[0].value = '';", email)
    driver.execute_script("arguments[0].value = '';", password)

    # Mail-Blank
    time.sleep(2)
    a = ""
    b = "12345"
    email = driver.find_element(By.ID, "1-email")
    password = driver.find_element(By.ID, "1-password")
    email.send_keys(a)
    password.send_keys(b)
    login_button = driver.find_element(By.NAME, "submit")
    login_button.click()

    error = driver.find_elements(By.XPATH, "//*[@id='auth0-lock-error-msg-password']/div")
    error1 = driver.find_elements(By.XPATH, "//*[@id='auth0-lock-error-msg-email']/div")
    if error:
        msg = error[0].text.strip()
        print(msg)
    else:
        print("No-Error in the Password")

    if error1:
        msg = error1[0].text.strip()
        print(msg)
    else:
        print("No-Error in the Email")
    time.sleep(2)

    driver.execute_script("arguments[0].value = '';", email)
    driver.execute_script("arguments[0].value = '';", password)

    # Password-Blank
    time.sleep(2)
    a = "jeevavadivel01@gmail.com"
    b = ""
    email = driver.find_element(By.ID, "1-email")
    password = driver.find_element(By.ID, "1-password")
    email.send_keys(a)
    password.send_keys(b)
    login_button = driver.find_element(By.NAME, "submit")
    login_button.click()

    error = driver.find_elements(By.XPATH, "//*[@id='auth0-lock-error-msg-password']/div")
    error1 = driver.find_elements(By.XPATH, "//*[@id='auth0-lock-error-msg-email']/div")
    if error:
        msg = error[0].text.strip()
        print(msg)
    else:
        print("No-Error in the Password")

    if error1:
        msg = error1[0].text.strip()
        print(msg)
    else:
        print("No-Error in the Email")
    time.sleep(2)

    driver.execute_script("arguments[0].value = '';", email)
    driver.execute_script("arguments[0].value = '';", password)

    #Valid Case (for email and password)
    time.sleep(2)
    a = "jeevavadivel01@gmail.com"
    b = "jeeva5657"
    email = driver.find_element(By.ID, "1-email")
    password = driver.find_element(By.ID, "1-password")
    email.send_keys(a)
    password.send_keys(b)
    login_button = driver.find_element(By.NAME, "submit")
    login_button.click()
    driver.save_screenshot("valid")
    error = driver.find_elements(By.XPATH, "//*[@id='auth0-lock-error-msg-password']/div")
    error1 = driver.find_elements(By.XPATH, "//*[@id='auth0-lock-error-msg-email']/div")
    if error:
        msg = error[0].text.strip()
        print(msg)
    else:
        print("Login successful - No error in the Password")

    if error1:
        msg = error1[0].text.strip()
        print(msg)
    else:
        print("Login successful - No error in the Email")
    time.sleep(2)

except Exception as e:
    print(f"Error: Cant Login => ")

#Test Case-8(Back-Home)
print("\nTesting-8 : Back-Home")
try:
        back=driver.find_element(By.XPATH,"//*[@id='auth0-lock-container-1']/div/div[2]/form/div/div/div/div[2]")
        home=back.find_element(By.XPATH,"//*[@id='auth0-lock-container-1']/div/div[2]/form/div/div/div/div[2]/div[2]/a")
        home.click()
        print("Success : HomePage")
except:
        print("Error : Can't go to HomePage")

time.sleep(10)
driver.quit()

#Login
#Google-Email-Passwords
#Facebook
#Dont remember-Values
#Login-Values
#back-Home
