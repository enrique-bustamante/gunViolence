# %%
# import dependencies
import pandas as pd
import requests
from bs4 import BeautifulSoup as soup
import seaborn as sns

# %%
# Get the response in html form
wikiURL = 'https://en.wikipedia.org/wiki/Gun_violence_in_the_United_States_by_state'
tableClass = 'wikitable sortable'
response = requests.get(wikiURL)
print(response.status_code)  # if code is 200 the connection is good

# %%
# Parse data
soupTable = soup(response.text, 'html.parser')
gunDataTable = soupTable.find('table',{'class': 'wikitable sortable'})

# %%
# Convert to dataframe
gunViolenceData = pd.read_html(str(gunDataTable))
gunViolenceDf = pd.DataFrame(gunViolenceData[0])
print(gunViolenceDf.head())

# %%
print(gunViolenceDf.columns)

# %%
# Display plot showing ownership vs murder rate
sns.scatterplot(data=gunViolenceDf, x='GunOwnership (%) (2013) [4]', y='GunMurder Rate (per 100,000) (2015)')
# %%
