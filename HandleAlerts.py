from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(7)
driver.get("https://demoqa.com/alerts")
driver.find_element(By.ID,"alertButton").click()
time.sleep(2)
driver.switch_to.alert.accept()

driver.find_element(By.ID,"timerAlertButton").click()
wait= WebDriverWait(driver,6)
wait.until(EC.alert_is_present())
time.sleep(2)
driver.switch_to.alert.accept()

driver.find_element(By.ID,"confirmButton").click()
time.sleep(2)
driver.switch_to.alert.accept()
confirm_message=driver.find_element(By.ID,"confirmResult").text
if confirm_message=="You selected Ok" :
    print("Success")

driver.find_element(By.ID,"confirmButton").click()
time.sleep(2)
driver.switch_to.alert.dismiss()
confirm_message=driver.find_element(By.ID,"confirmResult").text
if confirm_message=="You selected Cancel" :
    print("Cancelled")

driver.find_element(By.ID,"promtButton").click()
time.sleep(2)
user_input="Pranjal"
driver.switch_to.alert.send_keys(user_input)
driver.switch_to.alert.accept()
prompt_message=driver.find_element(By.ID,"promptResult").text
required_length= len(user_input)+1
modified_input= user_input.rjust(required_length)
if prompt_message=="You entered"+modified_input:
    print("Entered message is correct")
time.sleep(3)




