import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import TimeoutException

if not os.path.exists("test_report/screenshots"):
    os.makedirs("test_report/screenshots")

log_file = open("test_report/test_log.txt", "w")

def log(message):
    print(message)
    log_file.write(message + "\n")

products = ["Lamp"]

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.ikea.com/in/en/")

wait = WebDriverWait(driver, 10)

time.sleep(2)

for product in products:
    try:
        search_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="What are you looking for?"]')))
        search_box.clear()
        search_box.send_keys(product)
        search_box.send_keys(Keys.ENTER)
        time.sleep(3)

        product_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'pip-product-compact')]")
        driver.execute_script("window.scrollBy(0,300);")
        ss_path = f"test_report/screenshots/{product.replace(' ', '_')}.png"
        driver.save_screenshot(ss_path)
        if len(product_elements):
            log(f'PASS: product_found:{product}')
        else:
            driver.execute_script(f"alert('FAIL: No product found - {product}');")
            log(f"FAIL: No product found - {product}")
            time.sleep(2)
            driver.switch_to.alert.accept()
            assert False, f"Assertion Failed: No product elements found for {product}"
    except AssertionError as ae:
        log(f"ASSERTION ERROR: {str(ae)}")
        ss_path = f"test_report/screenshots/{product.replace(' ', '_')}_assertion_error.png"
        driver.save_screenshot(ss_path)
        driver.get("https://www.ikea.com/in/en/")
        time.sleep(2)


    except Exception as e:
        ss_path = f"test_report/screenshots/{product.replace(' ', '_')}_error.png"
        driver.save_screenshot(ss_path)
        log(f"ERROR: {product} - {str(e)}")
        driver.get("https://www.ikea.com/in/en/")
        time.sleep(2)

log("Test completed")
print("Test completed")
try :
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    driver.quit()


