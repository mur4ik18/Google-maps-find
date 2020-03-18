from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl
import main
import datetime
from main import sl ,writeExc ,error ,speed
from selenium.webdriver.common.by import By 

# what we find an where
InternetSpeed = input("Your internet speed (bad/normal/good) -")
what = input('what you find? ')
where = input('where you find this? ')
pages = int(input('How much pages you need? '))
sp = speed(InternetSpeed)

# add chromdriver
window = webdriver.Chrome(executable_path='./chromedriver.exe') 
# window setings
window.set_window_position(900, 0)
window.set_window_size(1024, 768)
# main url
url = 'https://www.google.com/maps/'
window.get(url)

# log document
f = open('log.txt', 'w')
f.write(str(datetime.datetime.now())+ '  \|/  '+ 'Start programm')

# excel open
wb = openpyxl.Workbook()
ws = wb.active
# excel setings
main.colWidth(ws,'B',50)
main.colWidth(ws,'C',50)
main.colWidth(ws,'D',10)
main.colWidth(ws,'E',50)
main.colWidth(ws,'F',50)
main.colWidth(ws,'G',50)
main.colWidth(ws,'H',50)

# sleep fucntion
sl(25/sp)
window.find_element_by_xpath('//*[(@id = "searchboxinput")]').click()
sl(25/sp)
window.find_element_by_xpath('//*[(@id = "searchboxinput")]').send_keys(what + ' ' + where)
sl(25/sp)
window.find_element_by_xpath('//*[(@id = "searchbox-searchbutton")]').click()
sl(100/sp)

t = 1
for i in range(0, pages):
    p = window.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "section-result-title", " " ))]//span')
    for c in range(0 , len(p)):
        sl(50/sp)
        titles = window.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "section-result-title", " " ))]//span')
        titles[c].click()
        sl(100/sp)
        t+=1
        print(t)
            # information
        # numbers
        writeExc(ws,'A',t, t-1)
        
        # title
        try:
            title = window.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/h1').text
            #print(title)
            writeExc(ws,'B',t, title)
        except:
            #print('Title = None')
            error(f, 'not find', str(t-1), 'Title not find')
        
        # subtitle, what is it (national park,park, shop etc)
        try:
            subtitle = window.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[2]/div/div[2]/span[1]/span[1]/button').text
        except: 
            #print('Subtitle = None')
            subtitle = ''
            error(f, 'not find', str(t-1), 'Subtitle not find')
        writeExc(ws,'C',t, subtitle)
        
        # rating
        try:
            rateNum = window.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/span[1]/span/span').text
            writeExc(ws,'D',t, rateNum)
        except: 
            #print('Rate = None')
            rateNum = 0
            writeExc(ws,'D',t, rateNum)
            error(f, 'not find', str(t-1), 'Rate not find')
        
        # position
        try:
            position = window.find_element(By.XPATH, '//*[@data-section-id="ad"]/div/div/*[@class="section-info-text"]/span[@class="widget-pane-link"]').text
        except:
            #print("Position = None")
            position = ''
            error(f, 'not find', str(t-1), 'Position not find')
        writeExc(ws,'E',t, position)
        
        # map positon
        try:
            MapPos = window.find_element(By.XPATH, '//*[@data-section-id="ol"]/div/div/*[@class="section-info-text"]/span[@class="widget-pane-link"]').text
        except:
            #print("Map position = None")
            MapPos = ''
            error(f, 'not find', str(t-1), 'Map position not find')
        writeExc(ws,'F',t, MapPos)
        
        # website
        try:
            website = window.find_element(By.XPATH, '//*[@data-section-id="ap"]/div/div/*[@class="section-info-text"]/span[@class="widget-pane-link"]').text
        except:
            #print("website = None")
            website = ''
            error(f, 'not find', str(t-1), 'Website link not find')
        writeExc(ws,'G',t, website)
        
        # phone number
        try:
            phone = window.find_element(By.XPATH, '//*[@data-section-id="pn0"]/div/div/*[@class="section-info-text"]/span[@class="widget-pane-link"]').text
        except:
           # print("phone number = None")
            phone = ''
            error(f, 'not find', str(t-1), 'Phone number not find')
        ws['H'+str(t)]= phone
        

        sl(25/sp)
        window.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/button').click()
        sl(25/sp)
        print("------------------")



    try:    
        window.find_element_by_xpath('//*[@id="n7lv7yjyC35__section-pagination-button-next"]').click()
        sl(100/sp)
    except:
        print("end")
        error(f, 'Havent next button', str(t-1), 'next butt not find')
        break

f.write(str(datetime.datetime.now())+ '  \|/  '+ 'Stop programm')
f.close()
wb.save("output/"+what + " " + where + ".xlsx")
sl(50/sp)
window.close()