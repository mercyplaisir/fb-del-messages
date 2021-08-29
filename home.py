import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains



x = ['Tif Laflame']




PATH = '/home/mercy/chrome driver/chromedriver'
browser = webdriver.Chrome(PATH)#ouvrir le navigateur
browser.get("https://www.facebook.com/")#aller sur facebook

#entrez l'email
email_field = browser.find_element_by_id("email")
email_field.send_keys("76796958")

#entrez le mot de passe
passwd_field = browser.find_element_by_id("pass")
passwd_field.send_keys("sindarubaza6")

#hit ENTER button to connect
connectButton = browser.find_elements_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")[0]
print(connectButton)

connectButton.click()
print("connected")
time.sleep(5)

browser.get("https://www.facebook.com/messages/t/")
print("got in messenger")
print(datetime.datetime.now())



div_element = WebDriverWait(browser, 60).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_yZ"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div[1]/div[1]/div/a/div/div[2]/div[1]/div/div')))
hover = ActionChains(driver).move_to_element(div_element)
hover.perform()

print(div_element)

delButtonContainer= WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='mount_0_0_yZ']/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div[1]/div[2]/div/div/div")))
hover = ActionChains(driver).move_to_element(button)
hover.perform()

print(delButtonContainer)

if isinstance(delButtonContainer,list):
    delButtonContainer[0].click()
else:
    delButtonContainer.click()

"""

#print(browser.find_elements_by_css_selector("div."+delButtonClass.replace(" ",".")))
print(delButton)
#delButton.click()

a=1
for i in b:
    print(a)
    i.click()
    a+=1

confirmDelButton = browser.find_elements_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[1]/div[1]/div/div[1]/div/span/span")[0]

time.sleep(20)

browser.quit()
"""