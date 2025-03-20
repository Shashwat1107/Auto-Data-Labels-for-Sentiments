import pandas as pd
import random
from faker import Faker

# Initialize Faker for fake names and dates
fake = Faker()

# Parameters
num_records = 150  # Set to 150 to match ratings
user_ids = [f'U{str(i).zfill(3)}' for i in range(1, num_records + 1)]
product_ids = [f'P{str(i).zfill(4)}' for i in range(1001, 2001)]
ratings = list(range(1, num_records + 1))  # Ratings from 1 to 150
sentiments = []
with open("custom_unique_reviews.txt", "r") as file:
    try:
        for i in range(133):
            sentiments.append(file.readline().strip())
    except EOFError:
        pass

# Only include Reordered and Returned
behaviors = ["Reordered", "Returned"]

# Generate data
data = []
for i in range(num_records):
    row = {
        "userID": user_ids[i],  # Ensure uniqueness
        "userName": fake.first_name(),
        "productID": random.choice(product_ids),
        "date_of_order": fake.date_between(start_date='-2y', end_date='today'),
        "rating": ratings[i],  # Assign sequential rating from 1 to 150
        "review": random.choice(sentiments),
        "behavior": random.choices(behaviors, weights=[0.5, 0.5])[0]  # Balanced behavior distribution
    }
    data.append(row)

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
output_file = "customer_reviews_with_ratings.csv"
df.to_csv(output_file, index=False)

print(f"Dataset saved to {output_file}")
