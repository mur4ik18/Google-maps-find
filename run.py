from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#Simple assignment
from selenium.webdriver import Chrome


# you have to use remote, otherwise you'll have to code it yourself in python to 
window = Chrome(executable_path='./chromedriver') 

window.set_window_position(900, 0)
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

lens = [[]]

for i in range(0, 10):
    p = window.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "section-result-title", " " ))]//span')
    for r in range(0 , len(p)):
        titles = window.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "section-result-title", " " ))]//span')
        titles[r].click()
        sl(4)
        subtitle = window.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[2]/div/div[2]/span[1]/span[1]/button')
        sl(0)
        window.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/button').click()
        sl(1)
        print(r)
        
    window.find_element_by_xpath('//*[@id="n7lv7yjyC35__section-pagination-button-next"]').click()
    sl(4)








sl(15)
window.close()