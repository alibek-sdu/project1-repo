# -*- coding: utf-8 -*-
"""Laptops.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LyvLj8V-fB1AKTEFVNULIkKNDfD4AY4-

#LIB
"""

import pandas as pd
import matplotlib.pyplot as plt
import requests
import csv
import json
import numpy as np
from collections import Counter
import seaborn as sns
from collections import defaultdict

"""#DATA"""

BASE_URL = "https://api.technodom.kz/katalog/api/v1/products/category/noutbuki-i-aksessuary"
params = {"city_id": "5f5f1e3b4c8a49e692fefd70", "limit": "234", "sorting": "score", "price": "0"}
response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    csv_filename = 'output.csv'
    print(data)
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)

        csv_writer.writerow(data['payload'][0].keys())

        for item in data['payload']:
            csv_writer.writerow(item.values())

else:
    print(f"Error: {response.status_code}")
    print(response.text)

df = pd.read_csv('output.csv')

"""#PLOT"""

threshold = 80

high_ratings = df[df['rating'] > threshold]
low_ratings = df[df['rating'] <= threshold]

count_high_ratings = len(high_ratings)
count_low_ratings = len(low_ratings)

labels = ['High Ratings (>80%)', 'Low Ratings (<=80%)']
sizes = [count_high_ratings, count_low_ratings]
colors = ['lightblue', 'lightcoral']
explode = (0.1, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Distribution of Laptop Ratings')
plt.axis('equal')

plt.show()

brand_counts = df['brand'].value_counts()


plt.figure(figsize=(12, 6))
sns.barplot(x=brand_counts.index, y=brand_counts.values, color='red')
plt.xlabel('Brands')
plt.ylabel('Count')
plt.title('Counts of Laptops by Brand')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

prices = df['price']

price_threshold = 400000

count_prices_over_threshold = sum(1 for price in prices if price > price_threshold)
count_prices_below_threshold = sum(1 for price in prices if price <= price_threshold)

categories = ['Prices Over 400,000', 'Prices 400,000 and Below']
counts = [count_prices_over_threshold, count_prices_below_threshold]
colors = ['lightcoral', 'lightblue']

plt.bar(categories, counts, color=colors)
plt.ylabel('Count')
plt.title('Laptop Counts Based on Price')
plt.show()

prices = df["price"]

price_range = range(0, 500001, 50000)

price_counts = Counter(np.digitize(prices, price_range))

most_popular_price_range = max(price_counts, key=price_counts.get)

price_range_labels = [f"{low}-{high} tenge" for low, high in zip(price_range, price_range[1:])]
price_range_counts = [price_counts[i] for i in range(1, len(price_range))]

plt.figure(figsize=(10, 6))
plt.bar(price_range_labels, price_range_counts, color='lightblue')
plt.xlabel('Price Range')
plt.ylabel('Count')
plt.title('Distribution of Laptop Prices')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()

is_preorder_values = df["is_preorder"]

count_preordered = (df['is_preorder'] == True).sum()
count_not_preordered = (df['is_preorder'] == False).sum()

categories = ['Preordered', 'Not Preordered']
counts = [count_preordered, count_not_preordered]
colors = ['lightcoral', 'lightblue']

plt.bar(categories, counts, color=colors)
plt.ylabel('Count')
plt.title('Preordered and Not Preordered Gadgets')
plt.show()

discounts = df["discount"]

non_zero_discounts = [d for d in discounts if d > 0]

discount_counts = Counter(non_zero_discounts)

discount_values, count_values = zip(*discount_counts.items())

sorted_discount_values, sorted_count_values = zip(*sorted(zip(discount_values, count_values)))

plt.figure(figsize=(12, 6))
plt.bar(sorted_discount_values, sorted_count_values, color='red')
plt.xlabel('Discount Value')
plt.ylabel('Count')
plt.title('Count of Laptop by Non-Zero Discount Value')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

brand_scores = defaultdict(list)

brand = df['brand'].all()
score = df['score'].all()

if score != 0:
    brand_scores[brand].append(score)

average_brand_scores = {brand: sum(scores) / len(scores) for brand, scores in brand_scores.items()}

brands, average_scores = zip(*average_brand_scores.items())

plt.figure(figsize=(12, 6))
plt.bar(brands, average_scores, color='pink')
plt.xlabel('Brand')
plt.ylabel('Average Score')
plt.title('Average Score for Each Laptop Brand (Ignoring 0 Scores)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df['reviews'] = pd.to_numeric(df['reviews'], errors='coerce')

brand_reviews_sum = defaultdict(int)
brand_reviews_count = defaultdict(int)

for brand, reviews in zip(df['brand'], df['reviews']):
    brand_reviews_sum[brand] += reviews
    brand_reviews_count[brand] += 1

average_brand_reviews = {brand: brand_reviews_sum[brand] / brand_reviews_count[brand] for brand in brand_reviews_sum}

sorted_brands = sorted(average_brand_reviews.keys(), key=lambda brand: average_brand_reviews[brand], reverse=True)
sorted_scores = [average_brand_reviews[brand] for brand in sorted_brands]

plt.figure(figsize=(12, 6))
plt.bar(sorted_brands, sorted_scores, color='pink')
plt.xlabel('Brand')
plt.ylabel('Average Count of Reviews')
plt.title('Average Count of Reviews for Each Laptop Brand')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()