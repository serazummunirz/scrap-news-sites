import SetEnviron
import os, time
SetEnviron.SetEnviron()

proxy_host = os.environ['PROXY_HOST']
proxy_port = os.environ['PROXY_PORT']
proxy_user = os.environ['PROXY_USER']
proxy_pass = os.environ['PROXY_pass']


def setup_proxy(driver, By):

    first_window = driver.current_window_handle
    time.sleep(3)

    all_windows = driver.window_handles

    for window in all_windows:
        if window != first_window:
            proxy_window = driver.current_window_handle
            driver.switch_to.window(window)
            time.sleep(2)
            driver.find_elements(By.XPATH, '//button[@class="btn btn-default ng-binding"]')[1].click()
            driver.find_element(By.XPATH, '//span[@omega-profile-inline="profile"]').click()
            driver.find_element(By.XPATH, '//option[@label="HTTP"]').click()
            driver.find_element(By.XPATH, '//input[@type="text"]').clear()
            driver.find_element(By.XPATH, '//input[@type="text"]').send_keys(proxy_host)
            driver.find_element(By.XPATH, '//input[@type="number"]').clear()
            driver.find_element(By.XPATH, '//input[@type="number"]').send_keys(proxy_port)
            driver.find_element(By.XPATH, '//span[@class="glyphicon glyphicon-lock"]').click()
            driver.find_element(By.XPATH, '//input[@placeholder="Username"]').clear()
            driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys(proxy_user)
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//input[@type="password"]').clear()
            driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(proxy_pass)
            driver.find_element(By.XPATH, '//button[@type="submit"]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//a[@ng-click="applyOptions()"]').click()
            time.sleep(0.5)
            driver.get("chrome-extension://padekgcemlokbadohgkifijomclgjgif/popup/index.html#")
            time.sleep(3)
            try:
                driver.find_element(By.XPATH, '//a[@id="js-profile-1"]').click()
            except:
                pass
            main_window = driver.window_handles
            driver.switch_to.window(first_window)
