""" import requests
from bs4 import BeautifulSoup

# URL = 'https://www.wellesleyblue.com/sports/wbkb/2019-20/roster'
# page = requests.get(URL)
# print(page)
# soup = BeautifulSoup(page.content, 'html.parser')

# results = soup.find('div',class_ = 'name') #mainbody
# print(results)
# job_elems = results.find_all(scope="row", class_="name")

# for job_elem in job_elems:
#     print(job_elem, end='\n'*2)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = '/Users/abullensmith/Downloads/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://www.wellesleyblue.com/sports/wbkb/2019-20/roster")
#soup = driver.page_source
soup = BeautifulSoup(driver.page_source, 'html.parser')
#driver.quit()

# h1 = driver.find_element_by_name('h1')
# h1 = driver.find_element_by_class_name('someclass')
# h1 = driver.find_element_by_xpath('//h1')
# h1 = driver.find_element_by_id('greatID')

#print(driver.find_element_by_class_name('roster'))


results = soup.find(id = 'mainbody') #mainbody
#print(results)
job_elems = results.find_all(class_="name")

for job_elem in job_elems:
    print(job_elem, end='\n'*2)

driver.quit()
 """

for i in range(11):
    x = 2010 + i
    y = x + 1
    print("'("+str(x)+"-"+str(y)+")',") 

def makeImportLink(sportAbr):
    for i in range(11):
        x = 2020 - i
        y = x + 1 -2000
        #print("("+str(x)+"-"+str(y)+")")

        print('IMPORTHTML("https://www.wellesleyblue.com/sports/'+sportAbr+'/'+str(x) + '-' + str(y)+ '/roster","table",1);')

#makeImportLink("wvball")