from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re

import time

driver = webdriver.Chrome()



driver.get("https://mlh.io/faq")

summary = driver.find_element_by_xpath("//*[@id='hackers']/div/div[1]/ul")
b = summary.get_attribute('innerHTML')

#print(b)

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

html = b
parsed_html = BeautifulSoup(html)
parsed_link = parsed_html.find_all("a")
for link in parsed_link:
    href = link.get('href')
    id = href.replace('#', '')

    answer = driver.find_element_by_id(id).get_attribute('innerHTML')
    parsed_answer = BeautifulSoup(answer)
    
    answer_paragraph = cleanhtml(str(parsed_answer.find('p')))
    question = id.replace('-', ' ')


    text_file = open("./Output.txt", "a")
    text_file.write("{Question: " + question + "} , " + "{Answer:" + answer_paragraph + "}" + "\n\n")
    text_file.close()

#    id = links.getHref # "#i-just-graduated-can-i-still-come-to-an-event"
#    id.removePound # "i-just-graduated-can-i-still-come-to-an-event"
#    answer = driver.find_element_by_id(id) # how to get paragraph in a div
#    question = id.remove #remove line and replace with space
#    # google how to save paragraph to text file in format of "Question: question, Answer: answer"
#    print ('ITEM NUMBER ' + str(COUNT) + str(links))


#search_bar = driver.find_element_by_id("lst-ib")
#search_bar.send_keys("Nasa Vans Hoodie Canada")
#search_bar.send_keys(Keys.ENTER)
#
#
#driver.get("https://www.facebook.com")
#
#time.sleep(1)
#user_name = driver.find_element_by_xpath('//*[@id="email"]')
#
#user_name.click()
#user_name.send_keys('alvin kwan')
#
#driver.find_element_by_id('email')
