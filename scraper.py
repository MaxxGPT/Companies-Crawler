from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--headless")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
url= 'https://growjo.com/industry/Cannabis'
driver.get(url)
time.sleep(2)

soup = BeautifulSoup(driver.page_source, "html.parser")

company_rows = soup.find_all("table",{"class":"jss31"})[0].find_all("tbody")[0].find_all("tr")

for company in company_rows:
    comapny_data = company.find_all("td")
    logo = logo = comapny_data[1].find_all("div",{"class":"lazyload-wrapper"})[0]
    name = comapny_data[1].text
    print(logo)

