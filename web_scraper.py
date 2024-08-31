import requests
from bs4 import BeautifulSoup
import pandas as pd

# replace URL
url = ""
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table with player stats
table = soup.find('table')  # Adjust table

# Extract data
data = []
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    data.append([col.text for col in cols])

# Convert to DataFrame
df = pd.DataFrame(data, columns=[])

# Save to CSV
df.to_csv('player_stats.csv', index=False)
