import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the preprocessed data
data = pd.read_csv('/home/doc-bd-a1/res_dpre.csv')

# Create a scatter plot using the correct column names
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal.length', y='petal.length', data=data)
plt.title("Sepal Length vs Petal Length")
plt.savefig("/home/doc-bd-a1/vis.png")
print("Visualization saved as vis.png")
