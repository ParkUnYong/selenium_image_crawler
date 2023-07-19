from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q")
#elem = driver.find_element_by_class_name("gLFyf gsfi")
elem.send_keys("dumpling")
elem.send_keys(Keys.RETURN) ##엔터

SCROLL_PAUSE_TIME = 1

# Get scroll height 스크롤의 높이를 가져 옴.
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break;    
    last_height = new_height
    
   
images = driver.find_elements_by_css_selector(".bRMDJf.islir")
count = 1;
for image in images :
    try:
        image.click()
        time.sleep(2)
        #img_url = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
        img_url=  driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute("src")
        urllib.request.urlretrieve(img_url, "test"+str(count)+".jpg")
        count = count +1
        if count >= 100:
            break;
    except:
        pass
          
driver.close()