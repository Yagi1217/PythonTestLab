import os
import requests
from selenium import webdriver
driver = webdriver.Chrome("C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\Lib\\site-packages\\chromedriver_binary\\chromedriver")

# 指定したURLに遷移してログイン
driver.get("https://account.nicovideo.jp/login")
login_id_form = driver.find_element_by_id("input__mailtel")
password_form = driver.find_element_by_id("input__password")
submit_button = driver.find_element_by_id("login__submit")
login_id_form.send_keys ("{ID入力箇所}") 
password_form.send_keys (“{パスワード入力箇所}")
submit_button.submit()

# cookieの受け渡し
session = requests.session()
for cookie in driver.get_cookies():
  session.cookies.set(cookie["name"], cookie["value"])

# requestsで取得
mylist_url = "http://www.nicovideo.jp/api/deflist/list"
response = session.get(mylist_url)
responsetext = response.text.encode().decode('unicode-escape').replace('},{', '}\n{‘)
print(responsetext)
driver.close
