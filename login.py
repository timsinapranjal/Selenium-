import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait #for explicit wait
from selenium.webdriver.support import expected_conditions as EC  #import expected conditions for explicit waits
from selenium.common.exceptions import StaleElementReferenceException #imported exceptions for fluent wait
from selenium.webdriver import ActionChains #use mouse actions
from selenium.webdriver.common.by import By #to use By class
#import HtmlTestRunner

class Dashboard(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=(ChromeDriverManager().install())) #used to directly install the latest version
        #self.driver = webdriver.Chrome(executable_path="E:\Office\chromedriver.exe") #--depricated code
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH,"//input[@name='username']").send_keys('Admin') # xpath - //tag[@attribute='value']
        self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys('admin123')
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()

    def test_addEmployee(self):
        #self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH,"//a[@href='/web/index.php/pim/viewPimModule']").click()
        self.driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
        wait= WebDriverWait(self.driver,5)
        wait.until(EC.presence_of_element_located((By.XPATH,"//button[@type='submit']"))).click() #explicit_wait

    def test_fluent(self):
       # self.driver.implicitly_wait(4)
        self.driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-stopwatch']").click()
        self.driver.find_element(By.XPATH,"//textarea[@placeholder='Type here']").send_keys('Pranjal Timsina')
        wait= WebDriverWait(self.driver,4,2, ignored_exceptions=[StaleElementReferenceException])
        wait.until(EC.presence_of_element_located((By.XPATH,"//i[@class='oxd-icon bi-calendar oxd-date-input-icon']"))).click()

       # self.driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-calendar oxd-date-input-icon']").click()
        self.driver.find_element(By.XPATH,"//p[text()='November']").click()


    def test_mouseActions(self):
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH,"//a[@href='/web/index.php/pim/viewPimModule']").click()
        self.driver.find_element(By.XPATH,"//span[text()='Configuration ']").click()
        self.hover1= self.driver.find_element(By.XPATH,"//a[text()='Optional Fields']")
        self.hover2= self.driver.find_element(By.XPATH,"//a[text()='Data Import']")
        self.Actions=ActionChains(self.driver)
        self.Actions.move_to_element(self.hover1).move_to_element(self.hover2).click().perform() #context_click() for right click
        self.driver.implicitly_wait(4)



   # def test_dropdown(self):
   #     self.driver.implicitly_wait(5000)
   #     self.dropdown=self.driver.find_element(By.XPATH,"//select[@data-test='product_sort_container']")
   #     self.dropdown=Select(self.dropdown)
   #     self.dropdown.select_by_value("za")
   #     self.dropdown_title =self.driver.find_element(By.CLASS_NAME, "active_option")
   #     self.assertEqual(self.dropdown_title.text,"NAME (Z TO A)","Dropdown text matched")

    #def test_added_to_cart(self):
    #    self.driver.implicitly_wait(5000)
    #    self.cart= self.driver.find_element(By.XPATH,"//button[@data-test='add-to-cart-sauce-labs-backpack']")
    #    self.cart.click()
    #    self.driver.implicitly_wait(40)
    #    self.added_cart = self.driver.find_element(By.XPATH, "//button[@data-test='remove-sauce-labs-backpack']")
    #    self.assertEqual(self.added_cart.text,"REMOVE")
    #    self.cart_count= self.driver.find_element(By.CLASS_NAME,'shopping_cart_badge')
    #    self.assertEqual(self.cart_count.text,"1")

    #@classmethod
    #def tearDown(self):
        #self.driver.close()
if __name__=="__main__":
    unittest.main()