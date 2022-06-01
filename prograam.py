from selenium import webdriver
import sys
sys.path.append('/home/snehal/PycharmProjects/selenium_project/sp')
from login_page import LoginPage



driver=webdriver.Chrome(executable_path="/home/snehal/Downloads/chromedriver_linux64/chromedriver")
o = LoginPage(driver)
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
driver.maximize_window()
driver.implicitly_wait(5)

username = "snehalahire107@gmail.com"
password = "snehal1993"


o.setusername(username)
o.clicklogin()
o.setpassword(password)
o.signin()