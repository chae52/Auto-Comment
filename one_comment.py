from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip

id=[['id','pw']] # custom

driver = webdriver.Chrome("./chromedriver")

options=webdriver.ChromeOptions()
options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36')

driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com") # custom
driver.implicitly_wait(1)
i=0

def clipboard_input(user_xpath, user_input):
        temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장

        pyperclip.copy(user_input)
        driver.find_element(By.XPATH,user_xpath).click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴
        time.sleep(1)

clipboard_input('//*[@id="id"]', id[i][0])
clipboard_input('//*[@id="pw"]', id[i][1])
driver.find_element(By.ID, "log.login").click()
time.sleep(1)
urls=['https://cafe.naver.com/'] # custom
driver.get(urls[0])
driver.switch_to.frame('cafe_main') # ★
time.sleep(3)

message = '잘 보고 갑니다.' # custom
input = driver.find_element(By.CSS_SELECTOR, '#app > div > div > div.ArticleContentBox > div.article_container > div.CommentBox > div.CommentWriter > div.comment_inbox > textarea')
input.send_keys(message)
reg_button=driver.find_element(By.CLASS_NAME,'btn_register')
reg_button.click()