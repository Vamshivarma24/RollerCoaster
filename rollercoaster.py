# Importing the libraries

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sea

# Setting the style of graphical presentation 
plt.style.use('ggplot')

# Importing the data
df=pd.read_csv('coaster_db.csv')

# Details about the data

# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# print(df.describe())

# Cleaning the data

df=df[['coaster_name', 'Location', 'Status','Manufacturer', 'year_introduced', 'latitude', 'longitude', 'Type_Main','opening_date_clean','speed_mph', 'height_ft','Inversions_clean', 'Gforce_clean']].copy()
df['opening_date_clean']=pd.to_datetime(df['opening_date_clean'])
df=df.rename(columns={'coaster_name':'Coaster_Name', 'year_introduced': 'Year_Introduced','opening_date_clean':'Opening_Date','Inversions_clean':'Inversions', 'Gforce_clean':'GForce'})
df=df.loc[~df.duplicated(subset=['Coaster_Name','Location','Opening_Date'])].reset_index(drop=True).copy()

# Feature Understanding
# Top 10 Years RollerCoasters Introduced

ax=df['Year_Introduced'].value_counts().head(10)\
    .plot(kind='bar',title='Top 10 Years RollerCoasters Introduced')
ax.set_xlabel('Year Introduced')
ax.set_ylabel('Count')    
plt.show()

# RollerCoaster Speed (Mph)

ay=df['speed_mph'].plot(kind='hist',bins=30, title='RollerCoaster Speed (Mph)')
ay.set_xlabel('Speed')
ay.set_ylabel('Frequency')
plt.show()

# RollerCoaster Speed vs. Height

az=sea.scatterplot(x='speed_mph',y='height_ft', hue='Year_Introduced',data=df)
az.set_title('RollerCoaster Speed vs. Height')
plt.show()

# Creating a Pairplot using Seaborn

aa=sea.pairplot(df, vars=['Year_Introduced','speed_mph','height_ft','Inversions','GForce'],hue='Type_Main')
plt.show()

# Correlation between Years introduced, Speed, Height, Inversions, GForce

Df_co=df[['Year_Introduced','speed_mph','height_ft','Inversions','GForce']].dropna().corr()
print(Df_co)

# Finding Correlation using Seaborn

sea.heatmap(Df_co,annot=True)
plt.show()
