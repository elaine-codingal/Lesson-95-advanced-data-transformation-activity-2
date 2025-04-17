####Import Libraries**

# Import Libraries 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns


# Import dataset 
data = pd.read_csv('Titanic Dataset.csv')

data.head(5)

""""###**Check association between Embarked and Age*"""

sns.boxplot(data = data, x = 'Embarked', y = 'Age') 
plt.show()

"""**There is too much overlapping in the boxplots, which means there is no much association between Embarked and Age**"""
plt.scatter(x = data['Fare'], y = data['Survived'])
plt.ylabel('Survived')
plt.xlabel('Fare')
plt.show()

plt.scatter(x = data['Parch'], y = data['Survived'])
plt.ylabel('Survived')
plt.xlabel('Parch')
plt.show()

plt.scatter(x = data['SibSp'], y = data['Survived'])
plt.ylabel('Survived')
plt.xlabel('SibSp')
plt.show()

### **Check association between Gender and Embarked**
association_categorical = pd.crosstab(data['Gender'], data['Embarked'])
print(association_categorical)