#welcome to Windows 10 ISO links generator
#Please setup dependencies first
#Made by Shivang


from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

def getfreshlnk():

    copt = webdriver.ChromeOptions()
    copt.add_argument("headless");
    copt.add_argument('--user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36"')

    driver = webdriver.Chrome(options=copt, executable_path="c:/chrome_driver/chromedriver.exe")

    driver.get('https://www.microsoft.com/en-in/software-download/windows10ISO')
    clc1 = driver.find_element_by_id('product-edition')
    sel = Select(clc1)
    sel.select_by_visible_text('Windows 10')

    driver.find_element_by_id('submit-product-edition').click()

    driver.implicitly_wait(5)

    clc1 = driver.find_element_by_id('product-languages')
    sel = Select(clc1)
    sel.select_by_visible_text('English International')

    driver.find_element_by_id('submit-sku').click()
    driver.implicitly_wait(5)

    liststr = {}
    txt = driver.find_element_by_id('card-info-content').get_attribute('innerHTML')
    soup = BeautifulSoup(txt, 'html.parser')
    for a in soup.find_all('a', href=True):
        temp = a['href']
        print("Found the URL:", temp)
        if temp.find('x32') != -1:
            liststr.update({'32bit': temp})
        elif temp.find('x64') != -1:
            liststr.update({'64bit': temp})

    print(liststr)
    val = driver.find_element_by_id('expiration-time').text
    print(val)


getfreshlnk()