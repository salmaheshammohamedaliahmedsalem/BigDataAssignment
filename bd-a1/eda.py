import pandas as pd

# Load the preprocessed data
data = pd.read_csv('/home/doc-bd-a1/res_dpre.csv')

# Generate EDA insights with the correct column names
insights = [
    f"Total records: {len(data)}",
    f"Mean sepal length: {data['sepal.length'].mean()}",
    f"Median petal width: {data['petal.width'].median()}",
]

# Save insights to text files
for i, insight in enumerate(insights, start=1):
    with open(f"/home/doc-bd-a1/eda-in-{i}.txt", "w") as file:
        file.write(insight)

print("EDA insights saved to eda-in-1.txt, eda-in-2.txt, etc.")
