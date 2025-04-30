# Analyzing Data with Pandas and Visualizing Results with Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Suppress warnings
import warnings
warnings.filterwarnings("ignore")

# Task 1: Load and Explore the Dataset
try:
    # Load the iris dataset
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

    # Display first few rows
    print("First five rows of the dataset:")
    print(df.head())

    # Data structure
    print("\nDataset Info:")
    print(df.info())

    # Check for missing values
    print("\nMissing values:")
    print(df.isnull().sum())

except FileNotFoundError:
    print("Dataset not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Task 2: Basic Data Analysis

# Basic statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Group by species
grouped = df.groupby('species').mean()
print("\nMean values by species:")
print(grouped)

# Task 3: Data Visualization

sns.set(style="whitegrid")  # Set seaborn style

# 1. Line Chart: Sepal and Petal Lengths by Sample Index
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
plt.plot(df.index, df['petal length (cm)'], label='Petal Length')
plt.title('Line Chart of Sepal and Petal Lengths')
plt.xlabel('Sample Index')
plt.ylabel('Length (cm)')
plt.legend()
plt.tight_layout()
plt.show()

# 2. Bar Chart: Average Petal Length by Species
plt.figure(figsize=(6, 4))
sns.barplot(x=grouped.index, y=grouped['petal length (cm)'], palette="viridis")
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.tight_layout()
plt.show()

# 3. Histogram: Sepal Width Distribution
plt.figure(figsize=(6, 4))
plt.hist(df['sepal width (cm)'], bins=10, color='teal', edgecolor='black')
plt.title('Histogram of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 4. Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', palette='Set2')
plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.tight_layout()
plt.show()
