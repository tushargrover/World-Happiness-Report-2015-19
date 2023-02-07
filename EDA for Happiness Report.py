#!/usr/bin/env python
# coding: utf-8

# # Data Dictionary:
# 
# Rank - Rank of the country based on the Happiness Score
# 
# Country - name of the country
# 
# Region - region the country belongs to, mappings as per 2015 csv file
# 
# GDP per Capita(Economy) – World Bank data on country’s Economy in terms of Purchasing Power Parity (PPP)
# 
# Health (Life Expectancy) – WHO data on country’s life expectancy at birth.
# 
# Family – based on survey in terms of level of social support from relatives or friends.
# 
# Freedom - to make life choices.
# 
# Generosity – donated money to a charity
# 
# Trust- perceptions on corruption in Government

# In[1]:


import pandas as pd


# In[16]:


df_2015 = pd.read_csv("C:\\Users\\Acer\\Desktop\\self-Projects\\Happiness\\Data\\CSV\\2015.csv")
df_2016 = pd.read_csv("C:\\Users\\Acer\\Desktop\\self-Projects\\Happiness\\Data\\CSV\\2016.csv")
df_2017 = pd.read_csv("C:\\Users\\Acer\\Desktop\\self-Projects\\Happiness\\Data\\CSV\\2017.csv")
df_2018 = pd.read_csv("C:\\Users\\Acer\\Desktop\\self-Projects\\Happiness\\Data\\CSV\\2018.csv")
df_2019 = pd.read_csv("C:\\Users\\Acer\\Desktop\\self-Projects\\Happiness\\Data\\CSV\\2019.csv")


# In[17]:


df_2015.columns, df_2016.columns,df_2017.columns, df_2018.columns,df_2019.columns


# # Standardizing the columns name and data as per the following details - 
# 
# * Standardizing the column names as below.
#     "Rank",
#     "Country"
#     "Region"
#     "Happiness Score"
#     "GDP per Capita"
#     "Social Support"
#     "Health (Life Expectancy)"
#     "Freedom"
#     "Generosity",
#     "Trust
#     
# * Missing "Region" data in df_2017,df_2018 & df_2019 from df_2015
# 
# 
# 

# In[18]:


country_region = pd.read_csv("C:\\Users\Acer\\Desktop\\self-Projects\\Happiness\\Data\\CSV\\2015.csv")[["Country","Region"]]
country_region_dict = dict(zip(country_region["Country"], country_region["Region"]))


# # 2019

# In[19]:


df_2019.columns = ["Rank", "Country","Happiness Score",
                   "GDP per Capita", "Social Support",'Health (Life Expectancy)',
                  "Freedom", "Generosity","Trust"]


# In[20]:


df_2019["Region"] = df_2019["Country"].map(country_region_dict)


# In[22]:


df_2019 =df_2019[["Rank", "Country","Region","Happiness Score",
          "GDP per Capita", "Social Support",'Health (Life Expectancy)',
                  "Freedom", "Generosity","Trust"]]
df_2019.head()


# # 2018

# In[23]:


df_2018.columns = ['Rank', 'Country', 'Happiness Score', 'GDP per Capita',
        'Social Support', 'Health (Life Expectancy)',
        'Freedom', 'Generosity','Trust']


# In[24]:


df_2018 ["Region"] = df_2018["Country"].map(country_region_dict)


# In[27]:


df_2018 = df_2018[["Rank", "Country","Region","Happiness Score",
          "GDP per Capita", "Social Support",'Health (Life Expectancy)',
                  "Freedom", "Generosity","Trust"]]
df_2018.head()


# # 2017

# In[52]:


df_2017 = pd.read_csv("C:\\Users\\Acer\\Desktop\\self-Projects\\Happiness\\Data\\CSV\\2017.csv")


# In[53]:


df_2017 = df_2017.drop(['Whisker.high','Whisker.low','Dystopia.Residual'], axis=1)


# In[54]:


df_2017.columns


# In[56]:


df_2017.columns = ["Country" , "Rank", "Happiness Score",
          "GDP per Capita", "Social Support",'Health (Life Expectancy)',
                  "Freedom", "Generosity","Trust"]

#RENAME the columns


# In[59]:


df_2017["Region"] = df_2017["Country"].map(country_region_dict)
df_2017 =df_2017[["Rank", "Country","Region","Happiness Score",
          "GDP per Capita", "Social Support",'Health (Life Expectancy)',
                  "Freedom", "Generosity","Trust"]]
#adding region 


# In[58]:


df_2017.head()


# # 2016

# In[77]:


df_2016 = pd.read_csv("C:\\Users\\Acer\\Desktop\\self-Projects\\Happiness\\Data\\CSV\\2016.csv")


# In[78]:


df_2016.columns


# In[79]:


df_2016 = df_2016.drop(['Region','Lower Confidence Interval', 'Upper Confidence Interval', 'Dystopia Residual'], axis=1)


# In[80]:


df_2016.columns = ["Country","Rank","Happiness Score",
                   "GDP per Capita", "Social Support",'Health (Life Expectancy)',
                  "Freedom", "Generosity","Trust"]


# In[82]:


df_2016["Region"] = df_2016["Country"].map(country_region_dict)

df_2016 =df_2016[["Rank", "Country","Region","Happiness Score",
          "GDP per Capita", "Social Support",'Health (Life Expectancy)',
                  "Freedom", "Generosity","Trust"]]
df_2016.head()


# # 2015

# In[83]:


df_2015.columns


# In[84]:


df_2015 = df_2015.drop(['Standard Error','Dystopia Residual'], axis =1)


# In[85]:


df_2015.columns = ["Country","Region","Rank","Happiness Score",
                   "GDP per Capita", "Social Support",'Health (Life Expectancy)',
                  "Freedom", "Trust","Generosity"]


# In[86]:


df_2015 =df_2015[["Rank", "Country","Region","Happiness Score",
          "GDP per Capita", "Social Support",'Health (Life Expectancy)',
                  "Freedom", "Generosity","Trust"]]


# In[87]:


df_2015.head()


# In[88]:


set(df_2015.columns)==set(df_2016.columns)==set(df_2017.columns)==set(df_2018.columns)==set(df_2019.columns)


# # Checking for null values

# In[89]:


df_2015.isnull().sum()


# In[90]:


df_2016.isnull().sum()


# In[91]:


df_2017.isnull().sum()


# In[92]:


df_2018.isnull().sum()


# In[93]:


df_2015.isnull().sum()


# In[100]:


df_2018[["Country","Region"]][df_2018["Region"].isnull()]


# In[101]:


df_2017[["Country","Region"]][df_2017["Region"].isnull()]


# In[102]:


df_2016[["Country","Region"]][df_2016["Region"].isnull()]


# In[103]:


df_2019[["Country","Region"]][df_2019["Region"].isnull()]


# In[104]:


df_2018.iloc[[37,48]]


# In[106]:


set(zip(df_2015["Country"],df_2015["Region"]))


# In[107]:


#for missing values, we should use region value from its neighbours - 
nan_region_dict_2018 ={'Trinidad & Tobago':'Latin America and Caribbean',
                       'Belize':'Latin America and Caribbean',
                       'Northern Cyprus':'Western Europe',
                       'Somalia':'Middle East and Northern Africa',
                       'Namibia':'Sub-Saharan Africa',
                        'South Sudan':'Sub-Saharan Africa'
                  }


# In[108]:


df_2018.loc[df_2018["Region"].isnull(),"Region"] = list(nan_region_dict_2018.values())


# In[110]:


df_2018.isnull().sum()


# In[111]:


nan_region_dict_2019 ={'Trinidad & Tobago':'Latin America and Caribbean',
                       'Northern Cyprus':'Western Europe',
                       'North Macedonia': 'Western Europe',
                       'Somalia':'Middle East and Northern Africa',
                       'Namibia':'Sub-Saharan Africa',
                       'Gambia':'Sub-Saharan Africa',                  
                       'South Sudan':'Sub-Saharan Africa',
                       }


# In[112]:


df_2019.loc[df_2019["Region"].isnull(),"Region"] = list(nan_region_dict_2019.values())


# In[116]:


df_2017[["Country","Region"]][df_2017["Region"].isnull()]


# In[119]:


nan_region_dict_2017 ={'Somalia':'Middle East and Northern Africa',
                       'Namibia':'Sub-Saharan Africa',
                       'South Sudan':'Sub-Saharan Africa',
                       'Belize':'Latin America and Caribbean',
                       'Taiwan Province of China' :'Eastern Asia',
                       'Hong Kong S.A.R., China' : 'Eastern Asia',
                       
                      }


# In[120]:


df_2017.loc[df_2017["Region"].isnull(),"Region"] = list(nan_region_dict_2017.values())


# In[123]:


df_2016[["Country","Region"]][df_2016["Region"].isnull()]


# In[124]:


nan_region_dict_2016 ={'Somalia':'Middle East and Northern Africa',
                       'Namibia':'Sub-Saharan Africa',
                       'South Sudan':'Sub-Saharan Africa',
                       'Belize':'Latin America and Caribbean',
                       'Somaliland Region' :'Middle East and Northern Africa',
                       'Puerto Rico	' : 'Latin America and Caribbean',
                       
                      }


# In[125]:


df_2016.loc[df_2016["Region"].isnull(),"Region"] = list(nan_region_dict_2016.values())


# In[135]:


df_2018.isnull().sum()


# In[149]:



df_2016.to_csv("dfclean_2016.csv",index=False)
df_2017.to_csv("dfclean_2017.csv",index=False)
df_2018.to_csv("dfclean_2018.csv",index=False)
df_2019.to_csv("dfclean_2019.csv",index=False)


# In[150]:


df_2015.to_csv("dfclean_2015.csv",index=False)


# In[ ]:




