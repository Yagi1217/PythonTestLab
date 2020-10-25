from selenium import webdriver

# ChromeDriverのパスを引数に指定しChromeを起動
driver = webdriver.Chrome("C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\Lib\\site-packages\\chromedriver_binary\\chromedriver")

# 指定したURLに遷移
driver.get("https://account.nicovideo.jp/login")

# この時点の取得したクッキーを表示
text = str(driver.get_cookies()).replace("}, {", "}\n{")
print(text)

# サイトにログインしてみる
login_id_form = driver.find_element_by_id("input__mailtel")
password_form = driver.find_element_by_id("input__password")
submit_button = driver.find_element_by_id("login__submit")
login_id_form.send_keys ("{ID入力箇所}") 
password_form.send_keys (“{パスワード入力箇所}")
submit_button.submit()

# もう一度、取得したクッキーを表示
text = str(driver.get_cookies()).replace('}, {', '}\n{')
print("\n",text)

driver.quit()
