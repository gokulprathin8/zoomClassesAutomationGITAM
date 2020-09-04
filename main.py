# Created & Maintained by Gokul Prathin
# Only Tested for GITAM Hyderabad Student Portal & GITAM Zoom Meetings
# Created at 1598865617 (UNIX Timestamp)

import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

##############################################
#
#
student_username = "221710304018"
student_password = "nanbcdib_14thma"
#
#
##############################################

driver = webdriver.Firefox()
profile = FirefoxProfile()
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", 'application/executable')

profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', '/tmp')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')

driver.get("https://login.gitam.edu/Login.aspx")

# Login into account to fetch current day's classes list

username_field = driver.find_element_by_id('txtusername')
password_field = driver.find_element_by_id('password')
login_field = driver.find_element_by_id('Submit')
username_field.clear()
username_field.send_keys(student_username)
password_field.clear()
password_field.send_keys(student_password)
login_field.click()

# End of Login

# Go to G-Learn
sleep(1)
glearn_button = driver.find_element_by_xpath('/html/body/form/div[4]/ul/li[1]/a/h5').click()

_links_unfiltered = []
_list_filtered = []

elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    _links_unfiltered.append(elem.get_attribute("href"))
check = 'https://gitam.zoom.us/'
res = [idx for idx in _links_unfiltered if idx.lower().startswith(check.lower())]

for _l in _links_unfiltered:
    if "https://gitam.zoom.us/" in _l:
        _list_filtered.append(_l)
print(_list_filtered)
print('Found ' + str(len(_list_filtered)) + ' classes today.')
# End of getting Links from GLearn

driver.get(_list_filtered[0])
pd.set_option("display.max_rows", None, "display.max_columns", None)
time_table = pd.read_csv('cs4_timetable.csv', encoding = "ISO-8859-1")
print(time_table)

print('Please specify the time of class by looking into the timetable: ')

