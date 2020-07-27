from selenium import webdriver
from selenium.webdriver.support.ui import Select
import csv
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import requests
import json

copt = webdriver.ChromeOptions()
copt.add_argument("headless");
#copt.add_argument('--user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36"')

driver = webdriver.Chrome(options=copt, executable_path="c:/chrome_driver/chromedriver.exe")
def fetchmrk(roll):

    year = 1;
    driver.get('https://govexams.com/knit/searchresult.aspx')
    driver.find_element_by_id('txtrollno').send_keys(roll)
    driver.find_element_by_id('btnSearch').click()
    sl = driver.find_element_by_id('ddlResult')
    sl = Select(sl)
    opt = len(sl.options)
    try:
        sl.select_by_visible_text('REGULAR (2017-18) Semester 3-4')
        #sl.select_by_index(2)
        driver.find_element_by_id('btnGo').click()
        mrk = driver.find_element_by_id('lbltotlmarksDisp').text
        fnd = mrk.find('/')
        obtmrk = mrk[0:fnd]
        obtmrk = obtmrk.strip()
        sem = driver.find_element_by_id('lblsem').text
        print(sem)
        studnm = driver.find_element_by_id('lblname').text
        sendarr = []
        sendarr.append(obtmrk)
        sendarr.append(studnm)
        print(sendarr)
        return sendarr
    except:
        print("Roll number ", roll, ' not available')
        return -1

def main():
    year = 1;
    finalar = []
    for i in range(16101, 16160):
        obtmrk = fetchmrk(i)
        if obtmrk == -1:
            continue
        singdct = {}
        singdct.update({"Semester": "Sem3&4", "Name": obtmrk[1], "Marks": obtmrk[0], "Roll No": i})
        finalar.append(singdct)
        #print(singdct)
    print(finalar)
    f = csv.writer(open("CL_year17-18.csv", "a", newline=''))
    f.writerow(["Semester", "Name", "Marks", "Roll No"])
    for i in finalar:
        f.writerow([i['Semester'], i['Name'], i['Marks'], i['Roll No']])

if __name__ == "__main__":
    main()
#fetchmrk(1,'16230')
