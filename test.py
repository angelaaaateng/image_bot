# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time 
# import random

# driver = webdriver.Chrome('E:\pawel\coding(learning)\discord\chromedriver.exe')
# driver.get('https://www.google.ca/imghp?hl=en&tab=ri&authuser=0&ogbl')

# box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
# box.send_keys("giraffe")
# box.send_keys(Keys.ENTER)


# # If I want to add scrolling
# # last_height = driver.execute_script('return document.body.scrollHeight')
# # for i in range(0, 5):
# #     driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# #     time.sleep(2)
# #     new_height = driver.execute_script('return document.body.scrollHeight')
# #     try:
# #         driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
# #         time.sleep(2)
# #     except Exception:
# #         pass
# #     if new_height == last_height:
# #         break
# #     last_height = new_height
# time.sleep(2)
# images = driver.find_elements_by_css_selector("img")
# srcs = []
# for image in images:
#     srcs.append(image.get_property("src"))

# print(srcs[random.randint(0, len(srcs) - 1)])

# box = driver.find_element_by_xpath('//*[@id="REsRA"]')
# box.clear()
# box.send_keys("Elizabeth")
# box.send_keys(Keys.ENTER)

# driver.close()

import base64
img_data = 'data:image/jpeg;base64,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'
# delete the header
base64_place = img_data.find('base64') + 7
header = img_data[:base64_place]
img_type = header[header.find('image/') + 6: header.find(';')]
img_name = "tmp." + img_type

img_data = img_data[base64_place:]
with open(img_name, "wb") as file:
    img_data = img_data.encode('utf-8')
    img_data = base64.decodebytes(img_data)
    file.write(img_data)