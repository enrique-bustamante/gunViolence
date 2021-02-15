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
sns.scatterplot(data=gunViolenceDf, x='Gun Ownership', y='Gun Murder Rate')
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
# Create sub-region lists of states
NewEngland = ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'Rhode Island', 'Vermont']
MidAtlantic = ['New Jersey', 'New York', 'Pennsylvania']
EastNorthCentral = ['Illinois', 'Indiana', 'Michigan', 'Ohio', 'Wisconsin']
WestNorthCentral = ['Iowa', 'Kansas', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'South Dakota']
SouthAtlantic = ['Delaware', 'Florida', 'Georgia', 'Maryland', 'North Carolina', 'South Carolina', 'Virginia', 'District of Columbia']
EastSouthCentral = ['Alabama', 'Kentucky', 'Mississippi', 'Tennessee']
WestSouthCentral = ['Arkansas', 'Louisiana', 'Oklahoma', 'Texas']
Mountain = ['Arizona', 'Colorado', 'Idaho', 'Montana', 'Nevada', 'New Mexico', 'Utah', 'Wyoming']
Pacific = ['Alaska', 'California', 'Hawaii', 'Oregon', 'Washington']

# %%
subregion = []


# %%
# Run loop to add sub-regions
for i in gunViolenceDf.index:
    if gunViolenceDf['State'][i] in NewEngland:
        subregion.append('New England')
    elif gunViolenceDf['State'][i] in MidAtlantic:
        subregion.append('Mid Atlantic')
    elif gunViolenceDf['State'][i] in EastNorthCentral:
        subregion.append('East North Central')
    elif gunViolenceDf['State'][i] in WestNorthCentral:
        subregion.append('West North Central')
    elif gunViolenceDf['State'][i] in SouthAtlantic:
        subregion.append('South Atlantic')
    elif gunViolenceDf['State'][i] in EastSouthCentral:
        subregion.append('East South Central')
    elif gunViolenceDf['State'][i] in WestSouthCentral:
        subregion.append('West South Central')
    elif gunViolenceDf['State'][i] in Mountain:
        subregion.append('Mountain')
    else:
        subregion.append('Pacific')
    
# %%
gunViolenceDf['Sub-region'] = subregion
print(gunViolenceDf)
# %%
# create region lists
NorthEast = ['New England', 'Mid Atlantic']
Midwest = ['East North Central', 'West North Central']
South = ['South Atlantic', 'East South Central', 'West South Central']
West = ['Mountain', 'Pacific']
# %%
region = []
# %%
for i in gunViolenceDf.index:
    if gunViolenceDf['Sub-region'][i] in NorthEast:
        region.append('North East')
    elif gunViolenceDf['Sub-region'][i] in Midwest:
        region.append('Midwest')
    elif gunViolenceDf['Sub-region'][i] in South:
        region.append('South')
    else:
        region.append('West')
# %%
gunViolenceDf['Region'] = region
print(gunViolenceDf.head())