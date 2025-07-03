import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if not os.path.exists("day3_report/asse_report"):
    os.makedirs("day3_report/asse_report")

log_file = open("day3_report/asse_report/day3_report.txt", "w")

def log_assertion(message, status = True):
    log_file.write(f"[ASSERTION] {message}: {'PASS'if status else 'FAIL'}\n")
    log_file.flush()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.x.com/login")

wait = WebDriverWait(driver, 10)

time.sleep(5)
def b_alert(message):
    driver.execute_script(f'alert("{message}")')
    time.sleep(2)
    try:
        driver.switch_to.alert.accept()
    except:
        pass
try:
    if "Sign in to X" in driver.page_source:
        b_alert("Page is Correct")
        log_assertion("Page is Correct", True)
    else:
        raise AssertionError("'Sign in to X' not found in the page")
except AssertionError as ae:
    b_alert("Error - page not found")
    log_assertion(str(ae),False)

try:
    log_in_email = wait.until(EC.element_to_be_clickable((By.NAME, "text")))
    log_in_email.send_keys("yourmailid")
    log_in_email.send_keys(Keys.ENTER)

    log_in_username = wait.until(EC.element_to_be_clickable((By.NAME,"text")))
    log_in_username.send_keys("username")
    log_in_username.send_keys(Keys.ENTER)

    log_in_password = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
    log_in_password.send_keys("yourpass")
    log_in_password.send_keys(Keys.ENTER)
    time.sleep(5)

    if "Home" in driver.page_source:
        b_alert("Correct sign in da")
        log_assertion("Sign in successfully", True)
    else:
        raise AssertionError("Log in failed")
except Exception as e :
    b_alert(f'Error while log in - {e}')
    log_assertion(f'Login failed - {e}', False)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    driver.quit()


