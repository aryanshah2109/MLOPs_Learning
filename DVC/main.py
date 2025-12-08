import pandas as pd
import os

# Create a small dataset (example: student info)
data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Jenny', 'Quil', 'Sid', 'Freya', 'Henry'],
    'Age': [20, 21, 19, 22, 20, 14, 39, 23, 21, 22],
    'Branch': ['CSE', 'ECE', 'ME', 'CSE', 'IT', 'ME', 'CSE', 'EE', 'ME', 'ECE'],
    'Marks': [85, 78, 90, 88, 76, 95, 35, 84, 55, 79]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create 'data' folder if it doesn't exist
os.makedirs('data', exist_ok=True)

# Save to CSV
csv_path = os.path.join('data', 'students.csv')
df.to_csv(csv_path, index=False)

print(f" Dataset saved successfully at: {csv_path}")
print(df)
