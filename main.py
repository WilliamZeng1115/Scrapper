from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import requests
import json


import time

driver = webdriver.PhantomJS()



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
counter = 0
for link in parsed_link:
    href = link.get('href')
    id = href.replace('#', '')

    answer = driver.find_element_by_id(id).get_attribute('innerHTML')
    parsed_answer = BeautifulSoup(answer)
    
    answer_paragraph = cleanhtml(str(parsed_answer.find('p')))
    question = id.replace('-', ' ')

    counter = counter + 1

#    text_file = open("./Output.txt", "a")
#    text_file.write("{Question: " + question + "} , " + "{Answer:" + answer_paragraph + "}" + "\n\n")
#    text_file.close()

    d = json.dumps({
                   "contexts": [],
                   "events": [],
                   "fallbackIntent": False,
                   "name": "question number " + str(counter),
                   "priority": 500000,
                   "responses": [
                                 {
                                 "action": "add.list",
                                 "affectedContexts": [],
                                 "defaultResponsePlatforms": {
                                 "google": True
                                 },
                                 "messages": [
                                              {
                                              "platform": "google",
                                              "textToSpeech": answer_paragraph,
                                              "type": "simple_response"
                                              },
                                              {
                                              "speech": answer_paragraph,
                                              "type": 0
                                              }
                                              ],
                                 "parameters": [],
                                 "resetContexts": False
                                 }
                                 ],
                   "templates": [],
                   "userSays": [
                                {
                                "count": 0,
                                "data": [
                                         {
                                         "text": question,
                                         "userDefined": True
                                         }
                                         ]
                                }
                                ],
                   "webhookForSlotFilling": False,
                   "webhookUsed": False
                   })
    r = requests.post('https://api.dialogflow.com/v1/intents?v=20150910', data=d, headers={'content-type': 'application/json', 'Authorization':'Bearer '})
    print (r.content.decode())
#    id = links.getHref # "#i-just-graduated-can-i-still-come-to-an-event"
#    id.removePound # "i-just-graduated-can-i-still-come-to-an-event"
#    answer = driver.find_element_by_id(id) # how to get paragraph in a div
#    question = id.remove #remove line and replace with space
#    # google how to save paragraph to text file in format of "Question: question, Answer: answer"
#    print ('ITEM NUMBER ' + str(COUNT) + str(links))


