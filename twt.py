import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

ids = ["jasonduv69", "pregadesh"]
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://x.com/login")

wait = WebDriverWait(driver, 15)

#Login
log_in_email = wait.until(EC.element_to_be_clickable((By.NAME, "text")))
log_in_email.send_keys("prega907@gmail.com")
log_in_email.send_keys(Keys.ENTER)

log_in_password = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
log_in_password.send_keys("Pregxdesh#10")
log_in_password.send_keys(Keys.ENTER)
time.sleep(5)

for user_id in ids:
    profile_url = f"https://x.com/{user_id}"
    driver.get(profile_url)

    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='UserName']")))
        print(f"User_found: {user_id}")
        time.sleep(3)


    except TimeoutException:
        alert_s = f"alert('User not found: {user_id}');"
        driver.execute_script(alert_s)
        print(f"User_not_found: {user_id}")
        time.sleep(2)
        driver.switch_to.alert.accept()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    driver.quit()
