from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import openpyxl
#Simple assignment
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By 

# you have to use remote, otherwise you'll have to code it yourself in python to 


window = Chrome(executable_path='./chromedriver') 

window.set_window_position(900, 0)
window.set_window_size(1024, 768)
url = 'https://www.google.com/maps/'
window.get(url)

# what we find an where
what = 'Park'
where = ',CA USA'

# sleep fucntion
def sl(x):
    time.sleep(x)
sl(5)
window.find_element_by_xpath('//*[(@id = "searchboxinput")]').click()
sl(3)
window.find_element_by_xpath('//*[(@id = "searchboxinput")]').send_keys(what + ' ' + where)
sl(3)
window.find_element_by_xpath('//*[(@id = "searchbox-searchbutton")]').click()
sl(3)

lens = [[]]
wb = openpyxl.Workbook()
ws = wb.active
ws.column_dimensions['B'].width = 50
ws.column_dimensions['C'].width = 50
ws.column_dimensions['D'].width = 10
ws.column_dimensions['E'].width = 50
ws.column_dimensions['F'].width = 50
ws.column_dimensions['G'].width = 50
ws.column_dimensions['H'].width = 50
t = 1
for i in range(0, 5):
    p = window.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "section-result-title", " " ))]//span')
    for c in range(0 , len(p)):
        sl(1)
        titles = window.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "section-result-title", " " ))]//span')
        titles[c].click()
        sl(4)
        t+=1
            # information
        ws['A'+str(t)]= t
        # title
        title = window.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/h1')
        print(title.text)
        ws['B'+str(t)]= title.text
        # subtitle, what is it (national park,park, shop etc)
        try:
            subtitle = window.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[2]/div/div[2]/span[1]/span[1]/button')
            print(subtitle.text)
            
        except: 
            print('havent rate')
            subtitle = ''
        ws['C'+str(t)]= subtitle.text
        # rating
        try:
            rateNum = window.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/span[1]/span/span')
            print(rateNum.text)
        except: 
            print('havent rate')
            rateNum = 0
        ws['D'+str(t)]= rateNum.text
        # position
        try:
            position = window.find_element(By.XPATH, '//*[@data-section-id="ad"]/div/div/*[@class="section-info-text"]/span[@class="widget-pane-link"]').text
            print(position)
        except:
            print("Position = None")
            position = ''
        ws['E'+str(t)]= position
        # map positon
        try:
            MapPos = window.find_element(By.XPATH, '//*[@data-section-id="ol"]/div/div/*[@class="section-info-text"]/span[@class="widget-pane-link"]').text
            print(MapPos)
        except:
            print("Map position = None")
            MapPos = ''
        ws['F'+str(t)]= MapPos
        # website
        try:
            website = window.find_element(By.XPATH, '//*[@data-section-id="ap"]/div/div/*[@class="section-info-text"]/span[@class="widget-pane-link"]').text
            print(website)
        except:
            print("website = None")
            website = ''
        ws['G'+str(t)]= website
        # phone number
        try:
            phone = window.find_element(By.XPATH, '//*[@data-section-id="pn0"]/div/div/*[@class="section-info-text"]/span[@class="widget-pane-link"]').text
            print(phone)
        except:
            print("phone number = None")
            phone = ''
        ws['H'+str(t)]= phone
        

        sl(1)
        window.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/button').click()
        sl(1)
        print("------------------")
        
    window.find_element_by_xpath('//*[@id="n7lv7yjyC35__section-pagination-button-next"]').click()
    sl(4)








sl(2)
wb.save("output.xlsx")
window.close()