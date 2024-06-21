import os
import sys
from bs4 import BeautifulSoup
from httpx import get
import skeleton as ht

# Set UTF-8 encoding for stdout
os.environ['PYTHONIOENCODING'] = 'utf-8'
sys.stdout.reconfigure(encoding='utf-8')

url = 'https://www.mobiledokan.co/product/vivo-watch-gt/'
res = get(url)
soup = BeautifulSoup(res.text, features='html.parser')

# Dictionary to hold the extracted data
data_dict = {}

# Find all the groups
groups = soup.findAll('div', class_='aps-group')


# Function to clean the attribute title
def clean_title(title):
    # Split the title by spaces and take the first part if there are explanations
    return title.split(' ', 1)[0]


# Iterate through each group
for group in groups:
    # Find all the rows in the table within the group
    rows = group.findAll('tr')

    for row in rows:
        # Get the attribute title and clean it
        attr_title = row.find('td', class_='aps-attr-title').text.strip()
        clean_attr_title = clean_title(attr_title)

        # Get the attribute value
        attr_value = row.find('td', class_='aps-attr-value').text.strip()

        # Add to the main data dictionary
        data_dict[clean_attr_title] = attr_value

# Print the extracted data dictionary
# print(data_dict)

# Buyer's Information table
price = data_dict.get('Expected')
announce = data_dict.get('Announced')
status = data_dict.get('Status')

info_tab = {
    "Bangladeshi Price": price,
    'Announced in Bangladesh': announce,
    "Current Status": status
}

info_table = ht.table(info_tab)
info_h2 = ht.h2_gen('Buyer\'s Information')
info = info_h2 + info_table

# ----------------Network----------------
techno = data_dict.get('Technology')
tg = data_dict.get('2G')
thg = data_dict.get('3G')
fg = data_dict.get('4G')
speed = data_dict.get('Speed')
gprs = data_dict.get('GPRS')
edge = data_dict.get('EDGE')

net_tab = {
    'Technology': techno,
    '2G Bands': tg,
    '3G Bands': thg,
    '4G Bands': fg,
    'Speed': speed,
    'GPRS': gprs,
    'EDGE': edge
}

net_table = ht.table(net_tab)
net_h2 = ht.h2_gen("Network")
net = net_h2 + net_tab

# -----------------Body-----------------
dimen = data_dict.get('')
weight = data_dict.get('')
build = data_dict.get('')
sim = data_dict.get('')
others = data_dict.get('')








