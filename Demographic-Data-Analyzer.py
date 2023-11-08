#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import pandas as pd


# In[3]:


file_path = ("C:/Users/Tanmay/Downloads/adult.data.csv")
data = pd.read_csv(file_path)


# In[4]:


data.head()


# In[6]:


# How many people of each race are represented in this dataset ?

race_count = data['race'].value_counts()
race_count


# In[7]:


# What is the average age of men ?

average_age_men = data[data['sex'] == 'Male']['age'].mean()
average_age_men


# In[8]:


# what is the percentage of people who have bachelor's degree

bachelors_degree = (data['education'] == 'Bachelors').mean() * 100
bachelors_degree


# In[9]:


# what percentage of people with advanced education ( Bachelors, Masters, or Doctorate) make more than 50K ?
advanced_degrees = ['Bachelors','Masters','Doctorate']

advanced_education = data['education'].isin(advanced_degrees)

advanced_education_50K_percentage = (data[advanced_education]['salary'] == '>50K').mean() * 100
advanced_education_50K_percentage


# In[10]:


# what percentage of people without advanced education make more than 50K ?
no_advanced_education_50K_percentage = (data[~advanced_education]['salary'] == '>50K').mean() * 100
no_advanced_education_50K_percentage


# In[12]:


# what is the minimum number of hours a person works per week ?

min_hours_per_week = data['hours-per-week'].min()
min_hours_per_week


# In[13]:


# what percentage of the people who work the minimum number of hours per week have a salary of more than 50K ?


min_hours_workers = data[data['hours-per-week'] == min_hours_per_week]


min_hours_more_than_50K_percentage = (min_hours_workers['salary'] == '>50K').mean() * 100
min_hours_more_than_50K_percentage


# In[15]:


#what country has the highest percentage of people than earn > 50K and what is that percentage ?


country_salary_distribution = data.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
country_salary_distribution['>50K_percentage'] = country_salary_distribution['>50K'] * 100


highest_earning_country = country_salary_distribution['>50K_percentage'].idxmax()
highest_earning_country_percentage = country_salary_distribution['>50K_percentage'].max()

highest_earning_country, highest_earning_country_percentage


# In[16]:


#identify the most popular occupation for those who earn > 50K in india.


india_high_earners = data[(data['native-country'] == 'India') & (data['salary'] == '>50K')]


most_popular_occupation_india = india_high_earners['occupation'].mode()[0]
most_popular_occupation_india


# In[ ]:




