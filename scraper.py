from urllib.request import Request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = 'https://growjo.com/industry/Cannabis'
request = Request(
    url,
    headers={'User-Agent': 'Mozilla/5.0'}
)
page = urlopen(request)
page_content_bytes = page.read()
page_html = page_content_bytes.decode("utf-8")

soup = BeautifulSoup(page_html, "html.parser")

company_rows = soup.find_all("table",{"class":"jss31"})[0].find_all("tbody")[0].find_all("tr")

for company in company_rows:
    company_data = company.find_all("td")
    logo = company_data[1].find_all("div",{"class":"lazyload-wrapper"})[0].find_all("a")
    name = company_data[1].text
    print(logo)
    break
