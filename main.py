

from time import sleep
from selenium import webdriver
import os
from facebook_operations.facebook_login import facebook_login
from interface import get_page_by_interface

from selenium.webdriver.common.by import By
from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.chrome.options import Options
from scroll import scroll


target_page = get_page_by_interface()


options = Options()

options.add_argument('start-maximized')
options.add_argument("")

svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc, options=options)


# if(
#     len(driver.find_elements(By.ID, "email")) > 0
#     and len(driver.find_elements(By.ID, 'pass')) > 0
#     and len(driver.find_elements(By.ID, 'pass')) > 0
# ):
#     facebook_login(driver)

# sleep(5)


os.system('cls' if os.name == 'nt' else 'clear')


driver.get(str(target_page))

sleep(15)
scroll(driver)
sleep(5)

# messages = driver.find_element(
#     By.XPATH, "//div[@class='xeuugli x2lwn1j xuk3077 x78zum5 x1q0g3np x1nhvcw1 x1jchvi3 xlxfd2w x1gslohp x126k92a']")
elements = driver.find_elements(By.XPATH, "//div[@class='x1fqp7bg']")


for i in range(1, len(elements) + 1):
    element = driver.find_element(By.XPATH, f"(//div[@class='x1fqp7bg'])[{i}]")
    hisMessages = element.find_elements(
        By.XPATH, f".//div[@class='xeuugli x2lwn1j x6s0dn4 x78zum5 x1q0g3np x193iq5w xh8yej3']")
    myMessages = element.find_elements(
        By.XPATH, f".//div[@class='xeuugli x2lwn1j x6s0dn4 x78zum5 x15zctf7 x193iq5w xh8yej3']")

    if (len(hisMessages) > 0):
        user = "them"
        messages = hisMessages

    else:
        user = "you"
        messages = myMessages

    for message in messages:

        with open(("res.txt"), "a", encoding='utf-8') as f:
            f.write("\n")
            sleep(1)
            if(len(message.find_elements(By.TAG_NAME, "svg")) == 0 and len(message.find_elements(By.TAG_NAME, "i")) == 0 and len(message.find_elements(By.TAG_NAME, "img")) == 0):
                f.write(f"sent by {user}: " + message.text)

            else:
                f.write(f"sent by {user}: <MEDIA FILE>")


driver.close()
