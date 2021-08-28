import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
passwd_field.send_keys(Keys.RETURN)

time.sleep(30)

browser.get("https://www.facebook.com/messages/t/")


delButtonContainer = browser.find_elements_by_xpath("//*[@id='mount_0_0_oh']/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div[1]/div[2]/div/div/div/i")
delButtonContainer.click()

#delButton = browser.fin("qzhwtbm6 knvmm38d")
#print(delButton)


# confirmDelButton = browser.find_elements_by_class_name("a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5")
