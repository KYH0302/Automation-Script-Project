from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import datetime as dt
import pandas as pd

# 웹드라이버 초기화
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # 네이버
    driver.get("https://www.naver.com/")
    
    # 네이버 증권
    stock = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#shortcutArea > ul > li:nth-child(6) > a'))
    )
    stock.click()

    # 모든 탭 핸들 가져오기
    original_window = driver.current_window_handle
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))  # 두 번째 탭이 열릴 때까지 기다림

    # 새 탭으로 전환
    for handle in driver.window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break

    # 국내 증권
    stock_korea = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#menu > ul > li.m2 > a'))
    )
    stock_korea.click()

    #코스피
    stock_kospi = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#newarea > div.snb.snb2 > ul > li.frst > ul > li.type1.lst1_1 > a'))
    )
    stock_kospi.click()

    point = []
    plus_minus = []
    percent = []
    time = []

    point_now = (driver.find_element(By.CSS_SELECTOR,'#now_value').text)
    point_now = point_now.replace(",","")
    point_now = float(point_now)
    plus_minus_now = (driver.find_element(By.CSS_SELECTOR,'#change_value_and_rate > span').text)
    plus_minus_now = float(plus_minus_now)
    a = point_now - plus_minus_now
    percent_now = round((plus_minus_now/a)*100,2)
    percent_now = f"{percent_now}%"
    e = dt.datetime.now()
    point.append(point_now)
    plus_minus.append(plus_minus_now)
    percent.append(percent_now)
    time.append(e.strftime("%Y-%m-%d-%H-%M"))

    #코스닥
    stock_kospi = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#newarea > div.snb.snb2 > ul > li.frst > ul > li.type1.lst1_2 > a'))
    )
    stock_kospi.click()

    point_now = (driver.find_element(By.CSS_SELECTOR,'#now_value').text)
    point_now = point_now.replace(",","")
    point_now = float(point_now)
    plus_minus_now = (driver.find_element(By.CSS_SELECTOR,'#change_value_and_rate > span').text)
    plus_minus_now = float(plus_minus_now)
    a = point_now - plus_minus_now
    percent_now = round((plus_minus_now/a)*100,2)
    percent_now = f"{percent_now}%"
    e = dt.datetime.now()
    point.append(point_now)
    plus_minus.append(plus_minus_now)
    percent.append(percent_now)
    time.append(e.strftime("%Y-%m-%d-%H-%M"))

    #해외증시   
    stock_kospi = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#menu > ul > li.m3 > a > span'))
    )
    stock_kospi.click()

    #다우 산업
    stock_kospi = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#americaIndex > thead > tr:nth-child(2) > td.tb_td2 > a'))
    )
    stock_kospi.click()

    point_now = (driver.find_elements(By.CSS_SELECTOR,'#content > div.rate_info > div.today > p.no_today > em span'))
    g = ""
    for span in point_now:
        g +=span.text
    g = g.replace(",","")
    point_now = float(g)

    plus_minus_now = (driver.find_elements(By.CSS_SELECTOR,'#content > div.rate_info > div.today > p.no_exday > em:nth-child(2) span'))
    g = ""
    for span in plus_minus_now:
        g +=span.text
    g = g.replace(",","")
    plus_minus_now = float(g)

    a = point_now - plus_minus_now
    percent_now = round((plus_minus_now/a)*100,2)
    percent_now = f"{percent_now}%"
    e = dt.datetime.now()
    point.append(point_now)
    plus_minus.append(plus_minus_now)
    percent.append(percent_now)
    time.append(e.strftime("%Y-%m-%d-%H-%M"))

    #해외 증시
    stock_kospi = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#menu > ul > li.m3.on > a'))
    )
    stock_kospi.click()
    
    #  나스닥100
    stock_kospi = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#americaIndex > thead > tr:nth-child(5) > td.tb_td2 > a'))
    )
    stock_kospi.click()

    point_now = (driver.find_elements(By.CSS_SELECTOR,'#content > div.rate_info > div.today > p.no_today > em span'))
    g = ""
    for span in point_now:
        g +=span.text
    g = g.replace(",","")
    point_now = float(g)

    plus_minus_now = (driver.find_elements(By.CSS_SELECTOR,'#content > div.rate_info > div.today > p.no_exday > em:nth-child(2) span'))
    g = ""
    for span in plus_minus_now:
        g +=span.text
    g = g.replace(",","")
    plus_minus_now = float(g)

    a = point_now - plus_minus_now
    percent_now = round((plus_minus_now/a)*100,2)
    percent_now = f"{percent_now}%"
    e = dt.datetime.now()
    point.append(point_now)
    plus_minus.append(plus_minus_now)
    percent.append(percent_now)
    time.append(e.strftime("%Y-%m-%d-%H-%M"))


    #해외 증시
    stock_kospi = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#menu > ul > li.m3.on > a'))
    )
    stock_kospi.click()
    
    #S&P500
    stock_kospi = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#americaIndex > thead > tr:nth-child(6) > td.tb_td2 > a'))
    )
    stock_kospi.click()

    point_now = (driver.find_elements(By.CSS_SELECTOR,'#content > div.rate_info > div.today > p.no_today > em span'))
    g = ""
    for span in point_now:
        g +=span.text
    g = g.replace(",","")
    point_now = float(g)

    plus_minus_now = (driver.find_elements(By.CSS_SELECTOR,'#content > div.rate_info > div.today > p.no_exday > em:nth-child(2) span'))
    g = ""
    for span in plus_minus_now:
        g +=span.text
    g = g.replace(",","")
    plus_minus_now = float(g)

    a = point_now - plus_minus_now
    percent_now = round((plus_minus_now/a)*100,2)
    percent_now = f"{percent_now}%"
    e = dt.datetime.now()
    point.append(point_now)
    plus_minus.append(plus_minus_now)
    percent.append(percent_now)
    time.append(e.strftime("%Y-%m-%d-%H-%M"))

    result = pd.DataFrame()
    result['종합 지수'] = point
    result['포인트 변화량'] = plus_minus
    result['퍼센트 변화량'] = percent
    result['시간'] = time
    result.index = ["코스피", "코스닥", "다우 존수", "나스닥100", "S&P500"]
    

    
    result.to_csv(f"web_scraping_{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")

    # 추가 작업을 위해 페이지가 로드될 때까지 기다림
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#element_on_new_page'))  # 여기에 올바른 선택자 입력
    )

    

finally:
    # 모든 탭을 종료하고 웹드라이버 종료
    driver.quit()
