from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# ブラウザのドライバーを取得する
driver = webdriver.Chrome("/home/Amamiya/.local/lib/python3.6/site-packages/chromedriver_binary//chromedriver")

# youtubeにアクセスする​
driver.get("https://www.youtube.com/")

# 検索ボックスに検索ワード(Keys)を入力しEnterキーを押す​
elem = driver.find_element_by_name("search_query")
elem.clear()
elem.send_keys("米津玄師 lemon")
elem.send_keys(Keys.RETURN)

# 出力された結果から対象の文字を含むリンクをクリックする​
click = driver.find_element_by_partial_link_text("「Lemon」")
click.click()
