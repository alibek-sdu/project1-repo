#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import json
from collections import Counter
from pandas import json_normalize


# In[5]:


df = pd.read_json('myjsonfile.json')


# In[6]:


print(df.head())


# In[9]:


smartfony_data = df['planshety']['data']

smartphone_names = [item['score'] for item in smartfony_data]


# In[10]:


print(len(smartphone_names))


# In[8]:


smartfony_data = df['smartfony']['data']

ratings = [item['rating'] for item in smartfony_data]

threshold = 80

high_ratings = [item for item in smartfony_data if item['rating'] > threshold]

count_high_ratings = len(high_ratings)

count_low_ratings = len(smartfony_data) - count_high_ratings

labels = ['High Ratings (>80%)', 'Low Ratings (<=80%)']
sizes = [count_high_ratings, count_low_ratings]
colors = ['lightblue', 'lightcoral']
explode = (0.1, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Distribution of Smartphone Ratings')
plt.axis('equal')

plt.show()


# In[8]:


import matplotlib.pyplot as plt
from collections import Counter

smartfony_data = df['smartfony']['data']

brands = [item['brand'] for item in smartfony_data]

brand_counts = Counter(brands)

brand_names, brand_counts = zip(*brand_counts.items())

sorted_brand_names, sorted_brand_counts = zip(*sorted(zip(brand_names, brand_counts), key=lambda x: x[1], reverse=True))

plt.figure(figsize=(12, 6))
plt.bar(sorted_brand_names, sorted_brand_counts, color='skyblue')
plt.xlabel('Brands')
plt.ylabel('Count')
plt.title('Counts of Smartphones by Brand')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# In[9]:


import matplotlib.pyplot as plt

smartfony_data = df['smartfony']['data']

prices = [int(item['price']) for item in smartfony_data]

price_threshold = 400000

count_prices_over_threshold = sum(1 for price in prices if price > price_threshold)
count_prices_below_threshold = sum(1 for price in prices if price <= price_threshold)

categories = ['Prices Over 400,000', 'Prices 400,000 and Below']
counts = [count_prices_over_threshold, count_prices_below_threshold]
colors = ['lightcoral', 'lightblue']

plt.bar(categories, counts, color=colors)
plt.ylabel('Count')
plt.title('Smartphone Counts Based on Price')
plt.show()


# In[10]:


import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

smartfony_data = df['smartfony']['data']

prices = [int(item['price']) for item in smartfony_data]

price_range = range(0, 500001, 50000)

price_counts = Counter(np.digitize(prices, price_range))

most_popular_price_range = max(price_counts, key=price_counts.get)

price_range_labels = [f"{low}-{high} tenge" for low, high in zip(price_range, price_range[1:])]
price_range_counts = [price_counts[i] for i in range(1, len(price_range))]

plt.figure(figsize=(10, 6))
plt.bar(price_range_labels, price_range_counts, color='lightblue')
plt.xlabel('Price Range')
plt.ylabel('Count')
plt.title('Distribution of Smartphone Prices')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()


# In[11]:


import matplotlib.pyplot as plt

smartfony_data = df['smartfony']['data']

is_preorder_values = [item['is_preorder'] for item in smartfony_data]

count_preordered = is_preorder_values.count(True)
count_not_preordered = is_preorder_values.count(False)

categories = ['Preordered', 'Not Preordered']
counts = [count_preordered, count_not_preordered]
colors = ['lightcoral', 'lightblue']

plt.bar(categories, counts, color=colors)
plt.ylabel('Count')
plt.title('Preordered and Not Preordered Smartphones')
plt.show()


# In[12]:


import matplotlib.pyplot as plt
from collections import Counter

smartfony_data = df['smartfony']['data']

discounts = [int(item['discount']) for item in smartfony_data]

non_zero_discounts = [d for d in discounts if d > 0]

discount_counts = Counter(non_zero_discounts)

discount_values, count_values = zip(*discount_counts.items())

sorted_discount_values, sorted_count_values = zip(*sorted(zip(discount_values, count_values)))

plt.figure(figsize=(12, 6))
plt.bar(sorted_discount_values, sorted_count_values, color='skyblue')
plt.xlabel('Discount Value')
plt.ylabel('Count')
plt.title('Count of Smartphones by Non-Zero Discount Value')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[41]:


import matplotlib.pyplot as plt
from collections import Counter

smartfony_data = df['smartfony']['data']

colors_hex = [item['color']['hex'] for item in smartfony_data]

color_counts = Counter(colors_hex)

top_colors = color_counts.most_common(10)

total_count = len(smartfony_data)

custom_color_mapping = {
    "#000000": "Black",
    "#FF0000": "Red",
    "#00FF00": "Green",
    "#0000FF": "Blue",
    "#BEC2CB": "Silver",
    "#175DD6": "Dark Blue",
    "#1E7814": "Light Green",
    "#6A0DAD": "Purple",
    "#706F70": "Grey",
    "#5EACFF": "Sky Blue",
    "#8F848F": "Mamba",
    "#FFD900": "Light Yellow",
    "#E34FD2": "Orchid",
    "#FAF7FA": "White"
}

average_counts = {custom_color_mapping.get(color_hex, color_hex): count / total_count for color_hex, count in top_colors}

color_names, average_counts_values = zip(*average_counts.items())

plt.figure(figsize=(12, 6))
plt.bar(color_names, average_counts_values, color='lightblue')
plt.xlabel('Color Name')
plt.ylabel('Average Count of Smartphones')
plt.title('Top 10 Popular Smartphone Colors')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# In[14]:


import matplotlib.pyplot as plt
from collections import defaultdict

smartfony_data = df['smartfony']['data']

brand_scores = defaultdict(list)
for item in smartfony_data:
    brand = item['brand']
    score = item['score']
    if score != 0:
        brand_scores[brand].append(score)

average_brand_scores = {brand: sum(scores) / len(scores) for brand, scores in brand_scores.items()}

brands, average_scores = zip(*average_brand_scores.items())

plt.figure(figsize=(12, 6))
plt.bar(brands, average_scores, color='lightblue')
plt.xlabel('Brand')
plt.ylabel('Average Score')
plt.title('Average Score for Each Smartphone Brand (Ignoring 0 Scores)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[25]:


import matplotlib.pyplot as plt
from collections import defaultdict

smartfony_data = df['smartfony']['data']

brand_reviews_scores = defaultdict(list)

for item in smartfony_data:
    brand = item['brand']
    reviews_score = item['reviews']
    brand_reviews_scores[brand].append(reviews_score)

average_brand_reviews_scores = {brand: sum(scores) / len(scores) for brand, scores in brand_reviews_scores.items()}

sorted_brands = sorted(average_brand_reviews_scores.keys(), key=lambda brand: average_brand_reviews_scores[brand], reverse=True)
sorted_scores = [average_brand_reviews_scores[brand] for brand in sorted_brands]

plt.figure(figsize=(12, 6))
plt.bar(sorted_brands, sorted_scores, color='lightblue')
plt.xlabel('Brand')
plt.ylabel('Average count of Reviews')
plt.title('Average count of Reviews for Each Smartphone Brand')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[ ]:




