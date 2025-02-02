# -*- coding: utf-8 -*-
"""DIAMOND PRICE DATA SET .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zduLAE04D8--xGAjZKstQnXy9hx-CdiB

# **Diamond price data set**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""# **About this data**

This diamond dataset includes features that influence a diamond's value: carat (weight), cut, color, clarity (all indicators of quality), depth, table (proportions affecting appearance), and dimensions (x, y, z). The target is price. Carat weight and quality metrics like color, cut, and clarity often correlate with price, while depth and table ratios can impact brilliance. To improve predictions, we can calculate volume (x * y * z), encode categorical features (cut, color, clarity), and explore interaction terms. Log-transforming price might also help if its distribution is skewed.

## **Columns and Their Descriptions:**

- carat:

This represents the weight of the diamond and is usually a strong predictor of price. Higher carat values typically correlate with higher prices.

- cut:

A categorical variable indicating the quality of the diamond’s cut. Common categories include Ideal, Premium, Good, Very Good, and Fair.
The cut can affect how light reflects within the diamond, potentially influencing its visual appeal and price.

- color:

Represents the color grade of the diamond, usually ranging from D (colorless) to J (slightly colored).
Diamonds closer to colorless are generally more valuable, so this feature might correlate with price.

- clarity:

A categorical variable indicating the clarity or purity of the diamond. Common grades include IF (internally flawless), VVS1, VVS2, VS1, VS2, SI1, SI2, and I1, where fewer inclusions (flaws) generally lead to higher prices.

- depth:

The depth percentage, calculated as
(
𝑧
/
(
𝑥
+
𝑦
)
/
2
)
×
100
(z/(x+y)/2)×100.
It’s a measure of how tall the diamond is relative to its width and can affect how light passes through the diamond.

- table:

The width of the diamond's top facet (in percentage), often influencing how it catches light. Diamonds with ideal table percentages are typically more valuable.

- price:

The target variable in this dataset, representing the diamond’s price in U.S. dollars.

- x, y, z:

The diamond's length, width, and height (in millimeters), respectively.
These dimensions are often useful for calculating volume or approximate the diamond's size.

## **Target Varible:**
 - - price: The target variable in this dataset, representing the diamond’s price in U.S. dollars.

## **Problem statement:-**

-
Predict the price of a diamond based on its physical characteristics and quality attributes, including carat, cut, color, clarity, and dimensions. The goal is to create a model that accurately estimates diamond prices to support valuation. Feature engineering will focus on volume calculation, categorical encoding, and interaction terms for improved accuracy.

## Understanding the data
"""

# Loading the diamonds dataset
df=pd.read_csv('/content/diamonds.csv')
df

df.info()# Checking data types and missing values

df.head()

print(df.isnull().sum()) # there is no null values

"""## **data cleaning**"""

df.shape

df.drop_duplicates(inplace=True)
# there is duplicates in this data

df.shape

"""### In data cleaning step there is no null values, but there duplicates and its droped

# Descriptive statistics
"""

df.describe()

"""# Data Visualization"""

df

plt.figure(figsize=(10,8))
sns.histplot(data=df,x="carat",kde=True)

plt.figure(figsize=(10,8))
sns.countplot(data=df,x="cut")

plt.figure(figsize=(10,8))
sns.countplot(data=df,x="color")

plt.figure(figsize=(10,8))
sns.countplot(data=df,x="clarity")

plt.figure(figsize=(10,8))
sns.histplot(data=df,x="depth",kde=True)

plt.figure(figsize=(10,8))
sns.histplot(data=df,x="table",kde=True)

plt.figure(figsize=(10,8))
sns.histplot(data=df,x="price",kde=True)

plt.figure(figsize=(10,8))
sns.histplot(data=df,x="x",kde=True)

plt.figure(figsize=(10,8))
sns.histplot(data=df,x="y",kde=True)

plt.figure(figsize=(10,8))
sns.histplot(data=df,x="z",kde=True)

"""
# correlation statistics"""

# Converting all the strings to numerical values using labelencoder class
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
df['color'] = labelencoder.fit_transform(df['color'])
df

# Define the desired order
df["cut"].replace(['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'],[0,1,2,3,4],inplace=True)

df

df["clarity"].value_counts()

# Define the clarity mapping
clarity_mapping = {
    'IF': 7,
    'VVS1': 6,
    'VVS2': 5,
    'VS1': 4,
    'VS2': 3,
    'SI1': 2,
    'SI2': 1,
    'I1': 0
}  # replaced in order vise!

# Apply the mapping to the 'clarity' column
df['clarity_numeric'] = df['clarity'].map(clarity_mapping)

# Display the updated DataFrame with the numeric clarity column
print(df[['clarity', 'clarity_numeric']].head())


# then droping previous feature
df.drop('clarity', axis=1, inplace=True)

df

# Correlation matrix
Corr_matrix = df.corr()

# Heatmap of correlation matrix

sns.heatmap(Corr_matrix,annot=True, fmt='0.01f', cmap='coolwarm',annot_kws=None, linewidths=0.5, robust=True,square=True) # 0.01f should be given for float values.
plt.title('Correlation Matrix')

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Calculate the correlation between 'price' and all other columns
price_corr = df.corr()['price']

# Remove the correlation of 'price' with itself (which is always 1)
price_corr = price_corr.drop('price')

# Create a heatmap to visualize the correlations
sns.heatmap(price_corr.to_frame(), annot=True, fmt='.2f', cmap='coolwarm',
            cbar=True, annot_kws={'size': 10})  # to_frame() converts Series to DataFrame for heatmap
plt.title('Correlation between Price and Other Features')
plt.show()

# droping less correlated feature
df.drop("cut",axis=1,inplace=True)
df.drop("depth",axis=1,inplace=True)

"""### in correlation step  color column converted to numeric with label encoder step , and clarity and cut columns are manually replaced because its ordianl data, and after cheking  correlation step less correlated features cut and depth are droped

# **skewness and loging**
"""

# Normal distribution it is


sns.histplot(df["color"],bins=30, kde=True)
plt.figure(figsize=(30,8))

sns.histplot(df["table"],bins=30, kde=True)
plt.figure(figsize=(30,8))

df['table'] = np.log1p(df['table'])

sns.histplot(df["x"],bins=30, kde=True)
plt.figure(figsize=(30,8))

df['x'] = np.log1p(df['x'])

sns.histplot(df["y"],bins=30, kde=True)
plt.figure(figsize=(30,8))

df['y'] = np.log1p(df['y'])

sns.histplot(df["z"],bins=30, kde=True)
plt.figure(figsize=(30,8))

df['z'] = np.log1p(df['z'])

sns.histplot(df["carat"],bins=30, kde=True)
plt.figure(figsize=(30,8))

df['carat'] = np.log1p(df['carat'])

"""### in the skewness cheking logaritham aplying step color column is no noraml distribution  another columns have skewness so exept color column and target varible column are log transformed

# Outlier detection
"""

df.shape

df.boxplot()

# Function to remove outliers using the IQR method except for one column
def remove_outliers_iqr(df, exclude_column):
    for col in df.columns:
        # Skip the specified column
        if col == exclude_column:
            continue
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        # Filter the DataFrame to remove rows with outliers in each column
        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    return df

# Specify the column to exclude
df_cleaned = remove_outliers_iqr(df, exclude_column='price')
df_cleaned

"""### before outliers removing shape of data=(49874, 8),  after removing outliers shape of data changed to = (49235 × 8)  """

df=df_cleaned

"""# Feature engineering"""

# Feature Engineering
df['volume'] = df['x'] * df['y'] * df["z"]# we can calculate the diamond's approximate volume using their diamonsion column  its compained to one feature
df['price'] = np.log1p(df['price'])  # Applying a log transformation to price can normalize the target variable, helping models to perform better with less skewed distributions.

df1=df
df2=df
df3=df

"""### in this feature engineering step  the columns x,y,z are compained to volume, we can calculate the diamond's approximate volume using their diamonsion column(x,y,z)  its compained to one feature

- and applied to log transform to target varible because  Applying a log transformation to price can normalize the target variable, helping models to perform better with less skewed distributions.

## predicting without scaled data
"""

from sklearn.model_selection import train_test_split
X = df[['color', 'table',"volume","carat","clarity_numeric"]]  # Features
y = df['price']  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42) # You can adjust the test_size and random_state



from sklearn.linear_model import LinearRegression
model = LinearRegression() #creating a variable of LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print(f"MSE: {mse}, RMSE: {rmse}, R-squared: {r2}")

"""###  non scaled data prediction result is so accurate

## Daimansionality reduction
"""

from sklearn.preprocessing import StandardScaler

# Standardize the features before PCA
features = ['color', 'table',"volume","carat","clarity_numeric"]
scaler = StandardScaler().fit_transform(df[features])


# Apply PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2)  # choosing 2 n_components
pca_result = pca.fit_transform(scaler)


# Add PCA results to the DataFrame
df1['pca1'] = pca_result[:, 0]
df1['pca2'] = pca_result[:, 1]

from sklearn.model_selection import train_test_split
X = df1[["pca1","pca2"]]  # Features
y = df1['price']  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42) # You can adjust the test_size and random_state



from sklearn.linear_model import LinearRegression
model = LinearRegression() #creating a variable of LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print(f"MSE: {mse}, RMSE: {rmse}, R-squared: {r2}")

"""### **after pca prediction there will be lesser r^2 so skiping to another step**

## Data scaling
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Assuming  DataFrame is called 'df'
# Select the features that  want to scale
features = ['color', 'table',"volume","carat","clarity_numeric"]

# Create a MinMaxScaler object
scaler = MinMaxScaler()

# Fit the scaler to  data and transform it
scaled_data = scaler.fit_transform(df[features])

# Create a new DataFrame with the scaled data (optional)
scaled_df = pd.DataFrame(scaled_data, columns=features, index=df.index)
scaled_df["price"]=df['price']
df=scaled_df
df

from sklearn.model_selection import train_test_split
X = df[['color', 'table',"volume","carat","clarity_numeric"]]  # Features
y = df['price']  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42) # You can adjust the test_size and random_state



from sklearn.linear_model import LinearRegression
model = LinearRegression() #creating a variable of LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print(f"MSE: {mse}, RMSE: {rmse}, R-squared: {r2}")

"""### minimaxscaled and non scaled data have same prediction and its r^2 is higer mse lower so choosing this as the final model

## **another prediction methods**
"""

# Importing the metrics (measurements) for linear regression algorithms
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Regression algorithms
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor  # Multi-layer perceptron regressor (MLP)

X = df1[['color', 'table',"volume","carat","clarity_numeric"]]  # Features
y = df1['price']  # Target variable # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train

y_train

# Standardize the dataset (only for some algorithms like SVR and Neural network-which gives better results )
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# List of linear regression models to apply
models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(),
    "Lasso Regression": Lasso(),
    "ElasticNet Regression": ElasticNet(),
    "Decision Tree": DecisionTreeRegressor(),
    "Random Forest": RandomForestRegressor(),
    "Gradient Boosting": GradientBoostingRegressor(),
    "Support Vector Regressor": SVR(),
    "K-Nearest Neighbors": KNeighborsRegressor(),
    "Neural Network": MLPRegressor(max_iter=1000)
}

# Function to evaluate model performance
def evaluate_model(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    return mae, rmse, r2

# Dictionary to store the results
results = {}

# Apply each model and compute metrics
for name, model in models.items(): # When you call items() on a dictionary, returns a list of the dictionary’s key-value tuple pairs.
                                   # Here "name" represents the "key", and "model" represents the "value"
  if name in ["Support Vector Regressor", "Neural Network"]: # Standardised value is only applied to support vector regressor and Neural network
        # Apply scaling for models that need it
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
  else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Compute evaluation metrics
  mae, rmse, r2 = evaluate_model(y_test, y_pred)
  results[name] = {"MAE": mae, "RMSE": rmse, "R²": r2} # name represents the "key" of the dictionary. Here key is the name of the algorithms
  # In the new dictionary "results", the key is the name of the algorithm; and the "key" is the MAE, RMSE,and R2 values
  # results[name] will be the different key when the name of the algorithm changes

# Convert results to a DataFrame for better visualization
results_df = pd.DataFrame(results).T
print(results_df)

"""# **.Documentation and reporting**"""

# comparing to all predictions Gradient Boosting data has less mse and higher r^2 so decided to report with  this linear regression model
print( "comparing to all predictions Gradient Boosting data has less mse and higher r^2 so decided to report with  this linear regression model")




from sklearn.model_selection import train_test_split
X = df3[['color', 'table',"volume","carat","clarity_numeric"]]  # Features
y = df3['price']  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42) # You can adjust the test_size and random_state



from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
model = GradientBoostingRegressor() #creating a variable of LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print(f"MSE: {mse}, RMSE: {rmse}, R-squared: {r2}")

print()
print()


# Summarize key findings
summary = {
    'Dataset Shape': df.shape,
    'Missing Values': df.isnull().sum().sum(),
    'Correlation with price': df.corr()['price'].sort_values(ascending=False)
}
print("EDA Summary:")
for key, value in summary.items():
    print(f"{key}: {value}")

"""**Based on the analysis of Diamonds price dataset for predicting the price , the Gradient Boosting  model demonstrated the best perfomance.**

 Based on the evaluation of the regression models for predicting price , the Gradient Boosting  model with learning rate of 0.25 and random state set to 42 emerged as the best-performing  model. it achived the highest accuracy and consistently strong results.

- Best model is that the non scaled models have better prediction and highest accuracy and consistancy

- some changes on datsets given below:

 - in this data set prediction step after reffering some chatbots and datsets i decided to logaritham applying on target variable.  because chatbot says  target varible has skewness so logaritham applying helps to improve model performance.
 - if we need model deploying part log transformed target varible should reverse with exponantioal method  **Thats  important because target varible log transformed**.
"""