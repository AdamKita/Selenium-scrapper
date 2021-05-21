###SELENIUM imports###
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains

###padans imports###
import pandas as pd

##driver path and setup
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH);

def main():
    print("setup complete")
if __name__ == "__main__":
    main()
