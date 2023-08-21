#!/usr/bin/env python
# coding: utf-8

# In[105]:


from bs4 import BeautifulSoup
import requests


# In[106]:


url = 'https://stockanalysis.com/stocks/tsla/revenue/'


# In[107]:


response = requests.get(url)


# In[108]:


Soup = BeautifulSoup(response.text, 'html')


# In[109]:


Table_data = Soup.find('table', class_='svelte-1jtwn20')


# In[111]:


Column = Table_data.find_all('th')


# In[113]:


Column_header = [data.text.strip() for data in Column]


# In[114]:


import pandas as pd


# In[133]:


df = pd.DataFrame(columns = Column_header)


# In[118]:


row_data = Table_data.find_all('tr')


# In[127]:


for data in row_data[1:]:
    individual_data = data.find_all('td')
    final_data = [data.text.strip() for data in individual_data]
    length = len(df)
    df.loc[length] = final_data

    


# In[131]:


df.to_csv(r'C:\Users\skbsd\Desktop\Python Codes\Tesla1.csv', index= False)


# In[132]:


df.tail()


# In[150]:


import yfinance as yf
import pandas as pd


# In[151]:


gme_data = yf.Ticker('GME')


# In[161]:


stock_data = gme_data.history()


# In[162]:


stock_data.reset_index(inplace=True)


# In[163]:


stock_data.head()


# In[209]:


from bs4 import BeautifulSoup
import requests
import matplotlib as plt
import seaborn as sb
url = "https://stockanalysis.com/stocks/gme/revenue/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
Table_data = soup.find('table', class_='svelte-1jtwn20')
Table_header = Table_data.find_all('th')
Table_final_header = [data.text.strip() for data in Table_header]


# In[210]:


gme_revenue = pd.DataFrame(columns = Table_final_header)
Table_row_data = Table_data.find_all('tr')


# In[211]:


for data in Table_row_data[1:]:
    table_td = data.find_all('td')
    table_final_td = [data.text.strip() for data in table_td]
    length = len(gme_revenue)
    gme_revenue.loc[length] = table_final_td


# In[212]:


gme_revenue.tail()


# In[217]:


gme_revenue.to_csv(r'C:\Users\skbsd\Desktop\Python Codes\gme_revenue.csv', index=False)


# In[267]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def make_graph(df, title, x_label, y_label):
    plt.figure(figsize=(25,6))
    plt.bar(df['Fiscal Year End'], df['Revenue'])
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
df = pd.read_csv(r'C:\Users\skbsd\Desktop\Python Codes\Tesla1.csv')
make_graph(df,'Tesla_revenue_data','Year', 'Revenue')


# In[270]:


import pandas as pd
import matplotlib.pyplot as plt


# In[277]:


def make_graph(df, title, X_label, Y_label):
    plt.figure(figsize=(35,8))
    plt.bar(df['Fiscal Year End'], df['Revenue'])
    plt.title(title)
    plt.xlabel(X_label)
    plt.ylabel(Y_label)
    plt.show()
df = pd.read_csv(r'C:\Users\skbsd\Desktop\Python Codes\gme_revenue.csv')
make_graph(df, 'GME_Revenue', 'year', 'Revenue')


# In[ ]:




