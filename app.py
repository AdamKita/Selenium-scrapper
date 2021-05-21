###SELENIUM imports###
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

###Other imports###
import pandas as pd
import asyncio

##driver path and setup
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH);

def data_to_csv(data,search_term):
    df = pd.DataFrame(data)
    df.to_csv(r'C:\Users\Adam\Desktop\export_dataframe.csv', index = True, header=True)

def get_page_data(drive):
        results = driver.find_elements_by_class_name("search-item")
        car_list = [];

        for r in results:
            price = r.find_element_by_class_name('price').text
            title =  r.find_element_by_class_name('title').text
            distance =  r.find_element_by_class_name('distance').text
            location =r.find_element_by_class_name('location').text
            description = r.find_element_by_class_name('description').text

            car_item = {
                    'title':title,
                    'distance': distance,
                    'price':price,
                    'location':location,
                    'description':description
                }
            car_list.append(car_item)
        return car_list

def next_page(driver):
        try:
            next_button = driver.find_element_by_xpath('//*[@title="Next"]')
            next_button.click();
            return True
        except StaleElementReferenceException:
            return False
        except NoSuchElementException:
            return False



def main():
    data_list = []
    search_term = "subaru"
    driver.get("https://www.kijiji.ca/")

    search = driver.find_element_by_id("SearchKeyword")
    search.send_keys(search_term)
    search.send_keys(Keys.RETURN)
    ##wait for page to fully load
    try:
        main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "mainPageContent"))
        )
        while next_page(driver):
            temp =  get_page_data(driver)
            data_list.append(temp)
        data_to_csv(data_list, search_term)
    finally :
        driver.quit()




if __name__ == "__main__":
    main()
