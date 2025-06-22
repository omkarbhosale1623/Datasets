import pandas as pd
import numpy as np
import random

# Number of rows in the dataset
num_rows = 202

# Create empty lists for each column
hours = []
age = []
internet = []
marks = []

# Generate random data for the dataset
for _ in range(num_rows):
    # Generate random values for 'Hours' column with some missing data
    hours.append(random.choice([3.0, 3.5, 4.0, 4.5, 5.0, np.nan]))

    # Generate random values for 'Age' column (between 18 and 24)
    age.append(random.randint(18, 24))

    # Generate random values for 'Internet' column (0 for 'No' and 1 for 'Yes')
    internet.append(random.choice([0, 1]))

    # Generate random values for 'Marks' column (between 50 and 100)
    marks.append(random.randint(50, 100))

# Create a DataFrame
data = {
    'Hours': hours,
    'Age': age,
    'Internet': internet,
    'Marks': marks
}

df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('exam_marks_dataset.csv', index=False)
