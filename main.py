import time

from pip._vendor.distlib.compat import raw_input
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

print(str("  __  __           _             ____ _           __ "))
print(str(" |  \/  | __ _ ___| |_ ___ _ __ / ___| |__   ___ / _|"))
print(str(" | |\/| |/ _` / __| __/ _ \ '__| |   | '_ \ / _ \ |_ "))
print(str(" | |  | | (_| \__ \ ||  __/ |  | |___| | | |  __/  _|"))
print(str(" |_|  |_|\__,_|___/\__\___|_|   \____|_| |_|\___|_|  "))
print(str("                                                     "))
print(str("Footsite Edition"))
print("")
time.sleep(5)
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")

site = input("What website? (FTL,FA,EB,CHAMPS): ")
url = input("Early link (just put the end after .com/): ")
size = input("Shoe Size: ")
prox = input("Proxies? (Y/N): ")

#if ("Y" or "N") != prox:
    #print("FUCK OUTTA HERE WITH YO BITCH ASS")

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ( "Mozilla-5.0 (Windows NT 6.3; WOW64) AppleWebKit-537.36 (KHTML, like Gecko) Chrome-34.0.1847.137 Safari-537.36")

driver = webdriver.PhantomJS(desired_capabilities=dcap)
driver.set_window_size(1024, 768)


if site == str("FTL"):
    ftl = driver.get("http://footlocker.com/" + url + "?cm=&size=" + size + "%2E0&id=840941364&lineItemQty=1%27)/")
    print("ON PRODUCT PAGE")
    #driver.find_element_by_xpath('//*[@id="pdp_size_select_mask"]').click()
    #time.sleep(3)
    #driver.find_element_by_("Size " + size)
    #driver.click()
    time.sleep(3)
    #driver.find_element_
    driver.save_screenshot("test.png")
