from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

@given('website "{url}"')
def step(context, url):
        driver.get('https://youtube.com')
        assert "RU" in driver.page_source

@then("push button with text '{text}'")
def step(context, text):
        WebDriverWait(driver, 250).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='search']"))).send_keys("Programming")
        seearcbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
        seearcbutton.click()
        WebDriverWait(driver, 250).until(EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string"))).click() 
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[9]/div[2]/ytd-video-secondary-info-renderer/div/div/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string/a"))).click()
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/tp-yt-app-toolbar/div/div/tp-yt-paper-tabs/div/div/tp-yt-paper-tab[2]/div"))).click()
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/tp-yt-app-toolbar/div/div/tp-yt-paper-tabs/div/div/tp-yt-paper-tab[4]/div"))).click()

@then("page include text '{text}'")
def step(context, text):
        assert "No results found." not in driver.page_source
        assert "JimTV" in driver.page_source

#driver.quit();