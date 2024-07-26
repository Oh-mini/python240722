from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (update the path to your WebDriver)
driver = webdriver.Chrome(executable_path='path/to/chromedriver')

def login(driver):
    driver.get("https://www.dataq.or.kr/www/main.do")
    time.sleep(5)

    username = driver.find_element(By.ID, "loginId")  # Replace with actual ID
    password = driver.find_element(By.ID, "loginPwd")  # Replace with actual ID

    username.send_keys("your_username")
    password.send_keys("your_password")
    password.send_keys(Keys.RETURN)

    time.sleep(5)

def navigate_to_exam_page(driver):
    mypage = driver.find_element(By.LINK_TEXT, "마이페이지")  # Replace with actual text if needed
    mypage.click()
    time.sleep(3)

    apply_status = driver.find_element(By.LINK_TEXT, "접수조회")  # Replace with actual text if needed
    apply_status.click()
    time.sleep(3)

    exam_selection = driver.find_element(By.PARTIAL_LINK_TEXT, "제54회 SQL 개발자(SQLD)")  # Replace with actual text if needed
    exam_selection.click()
    time.sleep(3)

    edit_info = driver.find_element(By.LINK_TEXT, "수험정보수정")  # Replace with actual text if needed
    edit_info.click()
    time.sleep(5)

def select_region_and_center(driver):
    region_dropdown = Select(driver.find_element(By.ID, "region"))  # Replace with actual ID
    region_dropdown.select_by_visible_text("서울특별시")

    test_center_dropdown = Select(driver.find_element(By.ID, "center"))  # Replace with actual ID

    def check_seat_availability():
        for option in test_center_dropdown.options:
            if option.text in ["경인중학교", "구일중학교"]:
                option.click()
                time.sleep(1)  # Wait for seat availability check
                seats_available = driver.find_element(By.ID, "seatAvailability")  # Replace with actual ID
                if "잔여좌석 있음" in seats_available.text:  # Update condition as needed
                    return True
        return False

    while True:
        if check_seat_availability():
            break
        print("No seats available, retrying...")
        time.sleep(30)  # Wait before retrying

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    change_button = driver.find_element(By.ID, "변경")  # Replace with actual ID
    change_button.click()

    time.sleep(5)

try:
    login(driver)
    navigate_to_exam_page(driver)
    select_region_and_center(driver)
finally:
    driver.quit()
