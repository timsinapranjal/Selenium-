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

driver.find_element(By.XPATH,"//span[@class='pr-1']").click()
time.sleep(3)
driver.execute_script("window.scrollTo(0,500)") #scroll to specific height
time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #scroll to Bottom
time.sleep(3)