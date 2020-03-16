from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

window = webdriver.Chrome(executable_path='chromedriver')
window.set_window_position(0, 0)
window.set_window_size(1024, 768)
url = 'https://www.google.com/maps/'
window.get(url)

# what we find an where
what = 'Park'
where = ',CA ,USA'


window.find_element_by_xpath('//*[(@id = "searchboxinput")]').click()
time.sleep(3)
window.find_element_by_xpath('//*[(@id = "searchboxinput")]').send_keys(what + ' ' + where)
time.sleep(3)
window.find_element_by_xpath('//*[(@id = "searchbox-searchbutton")]').click()






#def find_el(x):
    #return window.find_element_by_xpath(x)








time.sleep(15)
window.close()