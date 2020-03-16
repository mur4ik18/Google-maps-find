from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#Simple assignment
from selenium.webdriver import Chrome

window = Chrome(executable_path='./chromedriver')
window.set_window_position(0, 0)
window.set_window_size(1024, 768)
url = 'https://www.google.com/maps/'
window.get(url)

# what we find an where
what = 'Park'
where = ',CA ,USA'

# sleep fucntion
def sl(x):
    time.sleep(x)

window.find_element_by_xpath('//*[(@id = "searchboxinput")]').click()
sl(3)
window.find_element_by_xpath('//*[(@id = "searchboxinput")]').send_keys(what + ' ' + where)
sl(3)
window.find_element_by_xpath('//*[(@id = "searchbox-searchbutton")]').click()
sl(3)
window.find_elements_by_xpath('')




#def find_el(x):
    #return window.find_element_by_xpath(x)








sl(15)
window.close()