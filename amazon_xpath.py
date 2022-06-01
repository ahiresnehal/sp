import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="/home/snehal/Downloads/chromedriver_linux64/chromedriver")

driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fcart%2Fview.html%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

driver.maximize_window()
driver.implicitly_wait(5)

# Login to amazon
driver.find_element_by_id("ap_email").send_keys("snehalahire107@gmail.com")
driver.find_element_by_class_name('a-button-input').click()
driver.find_element_by_id('ap_password').send_keys('snehal1993')
driver.find_element_by_id('signInSubmit').click()

# Go to home page
driver.find_element_by_id('nav-logo-sprites').click()
driver.implicitly_wait(10)

# navigating home page till end
driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
driver.implicitly_wait(10)

# Search an item
driver.find_element_by_id('twotabsearchtextbox').send_keys('word power made easy by norman lewis')
driver.find_element_by_id('nav-search-submit-button').click()

# Choose the item in the list
driver.find_element_by_xpath('//span[@class="a-size-medium a-color-base a-text-normal" and text()="Word Power Made Easy [Paperback] NORMAN LEWIS"]').click()

# Add to cart that item
handles=driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
driver.find_element_by_xpath('//*[@id="add-to-cart-button"]').click()