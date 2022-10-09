from selenium import webdriver
import time
import threading


CHROME_DRIVER_PATH = "C:\\Users\\vmccl\\Downloads\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")
cookie.click()

bot_on = True

cookie_number = int(float(driver.find_element_by_id("money").text))
upgrades = {
    "buyTime machine":123456789,
    "buyPortal":1000000,
    "buyAlchemy lab":50000,
    "buyShipment":7000,
    "buyMine":2000,
    "buyFactory":500,
    "buyGrandma":100,
    "buyCursor":15,
}
cookies_per_second = driver.find_element_by_id("cps").text
def click():
    cookie.click()

def upgrade():
    print("Testing")
    threading.Timer(5.0,upgrade).start()
    cookie_number = int((driver.find_element_by_id("money").text).replace(",",""))
    for upgrade_price in upgrades:

        if cookie_number >= upgrades[upgrade_price]:
            what_to_click = driver.find_element_by_id(upgrade_price)

            try:
                what_to_click.click()
            except:
                pass

upgrade()
timeout = time.time()+300
while bot_on:
    test = 0
    click()
    print(time.time())
    # upgrade()
    if test == 5 or time.time()>timeout:
        bot_on = False
        print(driver.find_element_by_id("cps").text)
    test -=1


