# %%
# import dependencies
import pandas as pd
import requests
from bs4 import BeautifulSoup as soup
import seaborn as sns
import matplotlib.pyplot as plt

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
columns = ['State', 'Population', 'Total Deaths', 'Murders', 'Gun Murders', 'Gun Ownership', 'Death Rate', 'Murder Rate', 'Gun Murder Rate']
gunViolenceDf.columns = columns

# %%
print(gunViolenceDf.columns)

# %%
# Display plot showing ownership vs murder rate
sns.scatterplot(data=gunViolenceDf, x='GunOwnership (%) (2013) [4]', y='GunMurder Rate (per 100,000) (2015)')
# %%
# with regressions
sns.pairplot(gunViolenceDf, kind="reg")
plt.show()
sns.pairplot(gunViolenceDf, kind="scatter")
plt.show()
# %%
plt.hist(gunViolenceDf['Population'])
# %%
plt.hist(gunViolenceDf['Total Deaths'])
# %%
plt.hist(gunViolenceDf['Murders'])
# %%
plt.hist(gunViolenceDf['Gun Murders'])
# %%
plt.hist(gunViolenceDf['Death Rate'])

# %%
plt.hist(gunViolenceDf['Murder Rate'])
# %%
plt.hist(gunViolenceDf['Gun Murder Rate'])
# %%
plt.scatter(x=gunViolenceDf['Population'], y=gunViolenceDf['Gun Murder Rate'])
# %%
plt.scatter(x=gunViolenceDf['Murders'], y=gunViolenceDf['Gun Murders'])
# %%
NewEngland = ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'Rhode Island', 'Vermont']
MidAtlantic = ['New Jersey', 'New York', 'Pennsylvania']
EastNorthCentral = ['Illinois', 'Indiana', 'Michigan', 'Ohio', 'Wisconsin']
WestNorthCentral = ['Iowa', 'Kansas', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'South Dakota']
SouthAtlantic = ['Delaware', 'Florida', 'Georgia', 'Maryland', 'North Carolina', 'South Carolina', 'Virginia', 'District of Columbia']
EastSouthCentral = ['Alabama', 'Kentucky', 'Mississippi', 'Tennessee']
WestSouthCentral = ['Arkansas', 'Louisiana', 'Oklahoma', 'Texas']
Mountain = ['Arizona', 'Colorado', 'Idaho', 'Montana', 'Nevada', 'New Mexico', 'Utah', 'Wyoming']
Pacific = ['Alaska', 'California', 'Hawaii', 'Oregon', 'Washington']