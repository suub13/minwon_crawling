from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Chrome Driver 경로 설정
chrome_driver_path = '/path/to/chromedriver'

# Chrome 옵션 설정 (예: 브라우저 창을 숨기고 실행)
chrome_options = Options()
chrome_options.add_argument('--headless')  # 브라우저 창을 숨기고 실행

# WebDriver 실행
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
