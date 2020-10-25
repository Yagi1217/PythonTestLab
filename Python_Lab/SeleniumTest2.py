from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# ブラウザのドライバーを取得する
driver = webdriver.Chrome("C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\Lib\\site-packages\\chromedriver_binary\\chromedriver")

# Googleへアクセス
driver.get("https://www.google.co.jp/")
 
# 検索開始
elem_search_word = driver.find_element_by_id("lst-ib")
elem_search_word.send_keys("selenium")
elem_search_word.send_keys(Keys.ENTER)
 
# 表示された結果のaタグの情報を取得する
elements_a = driver.find_elements_by_css_selector("#res h3.r a")

# 取得した情報を表示する
for elem in elements_a:
url = elem.get_property("href")
print(url)

# 開いているブラウザソフトの状況のスクショを取ってみる
driver.save_screenshot("c:\\tmp\\screen.png")
