from bs4 import BeautifulSoup
import requests 
import pandas as pd
from datetime import datetime


url = 'https://satruck.org/Home/DonationValueGuide'
year = datetime.now().year
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
tables = soup.find_all('table', class_ = 'dvg-table')

data = []
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if len(cols) > 1:
            item_name = cols[0].text.strip()
            price = cols[2].text.strip().replace('$', '').replace(',', '')
            data.append([item_name, float(price)])

df = pd.DataFrame(data, columns = ['Item', 'Value'])
df.to_csv(f'charitableContributions_{year}.csv', index=False)

