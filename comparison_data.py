from httpx import get
from bs4 import BeautifulSoup

url = 'https://www.gsmarena.com.bd/compare/realme-c17-vs-xiaomi-redmi-note-10/'
res = get(url)
soup = BeautifulSoup(res.text, "html.parser")

phone_div = soup.find('div', {'class': 'panel-box'})

tables = soup.findAll('table', {'class': 'table-hover'})
for table in tables:
    trows = table.findAll('tr')
    for row in trows:
        h3_data = row.find('td', {'class': 'specs_name'})
        # ('td', class_='col-sm-2 col-xs-4 specs_name')
        # h3 = h3_data.text.strip()
        print(h3_data)



