from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.XPATH,"//input[@name='username']").send_keys('Admin')
driver.find_element(By.XPATH,"//input[@name='password']").send_keys('admin123')
driver.find_element(By.XPATH,"//button[@type='submit']").click()
print(driver.window_handles)
driver.execute_script("window.open ('https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveModule','new window')")
handles = driver.window_handles
size = len(handles)
print(handles)
page1_handle = driver.current_window_handle #assigning running tab
for x in range(size):
  if handles[x] != page1_handle:
    driver.switch_to.window(handles[x])
    print(driver.current_url) #fetching current URL
    driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys("Pranjal")
    time.sleep(3)
    break


time.sleep(3)