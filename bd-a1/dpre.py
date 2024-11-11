import pandas as pd

# Load the data from the previous stage
data = pd.read_csv('/home/doc-bd-a1/loaded_data.csv')

# Print the column names to verify them
print("Columns in loaded_data.csv:", data.columns)

# Data Cleaning (Example: Fill missing values only for numeric columns)
numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

# Data Transformation (Example: Log transformation on numeric columns)
for col in numeric_cols:
    data[col] = data[col].apply(lambda x: x if x <= 0 else x ** 0.5)  # Example transformation

# Select specific columns with correct names
data = data[['sepal.length', 'sepal.width', 'petal.length', 'petal.width', 'variety']]

# Data Discretization (Example: Binning a numeric column)
data['sepal_length_bin'] = pd.cut(data['sepal.length'], bins=3, labels=['Short', 'Medium', 'Long'])

# Save the preprocessed data
data.to_csv('/home/doc-bd-a1/res_dpre.csv', index=False)
print("Preprocessed data saved to res_dpre.csv")
