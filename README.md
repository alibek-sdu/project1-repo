
# Technodom Parser

What are Technodom's popular brands among the Smartphones, Gadgets and Laptops categories and their price relationship

Project parses whole products and categories of Technodom.kz and analyses data which got from web site.



## Tech Stack

**Parser:** Node.js, Puppeteer, JSON, CSV Writer, Beautiful Soup

**Analyser:** Pandas, matplotlib.pyplot, collections, seaborn


## Installation



To run the script you need to install Node.js and dependencies. Run the following commands in a terminal:

```bash
# Download Node.js: https://nodejs.org/
# Clone repo

git clone <URL repo>
cd <folder bane>
```

## Dependencies and launch

All the dependencies of projects are listed at package.json file. You can either use npm or yarn package managers. Here in example I use ```npm v9.6.7``` and Node.js ``` v18.17.1```
You can check your own version by commands ```npm -v``` and ```node -v```

```bash
npm install

node parse.js
```

## From JSON to CSV format

```bash
node technodomJson2csv.js
```

## Parsing laptops data from the site
First we try to parse technodom directly by sending request and parsing it with BeautifulSoap. We find pattern how data is created in the front and we send request and get less data than we intend. In the end it was failure, because for the most part data was organized in hard way to find other pattern of information. You can check our attempts in laptopsbyparsing.py.

## Getting Laptops data from api
Other way to get all data, that we need was by using techodom api. In this case we easily get information that we need for our analysis by directly sending get request to api by neccessary category. 

## Analysis on laptop
After anlysing data from laptop we get that most of the laptops price is lower than 400000 tg. And that Asus is dominating inside the technodom, which means it gets most of viewers attention by a lot.

## Price distribution
By the graphics we can see that most laptops costs less than 400000tg and the second place of price distribution is on 2500000-3000000tg.

## Laptop ratings
In rating part of laptop it's clear that only 4.7% of Laptops was rated high. And that most of them is less than 80% of appreciation. The reason for this kind of distribution is that most of the laptops has no review or ratings. If more people give their honest opinions about the product, that they buy we can rate them properly and get most precise analysis.
## Analyser

### Gadget Ratings
During the analysis, a bug in the rating data extraction was identified and promptly resolved. The focus was on investigating high ratings (above a specified threshold), providing valuable insights into the exceptional performance of certain gadgets within the dataset.

### Gadget Brands
An insightful analysis of gadget brands was conducted, revealing the distribution of gadgets among various brands. This section sheds light on the market presence and popularity of different brands in the dataset.

### Price Analysis
Accurate processing of gadget price data was executed, leading to a detailed examination of the price distribution within specified ranges. This analysis contributes to a comprehensive understanding of the pricing structure of the gadgets under consideration.

### Pre-order Analysis
A precise calculation of the number of pre-orders and the identification of gadgets that are not pre-orders were carried out. This analysis aids in understanding the prevalence and impact of pre-orders in the dataset.

### Discount Analysis
Discount Distribution
The distribution of discounts on gadgets was meticulously analyzed. Zero-value discounts were filtered out, and the distribution of non-zero discounts was visually presented, offering insights into the discount landscape.

### Feedback Analysis
The total number of reviews and the count of devices for each brand were accurately calculated. Additionally, the average number of reviews for each brand was graphically represented, providing a comparative overview of customer feedback across different brands.

> This Python-based analysis delivers a thorough exploration of key aspects related to gadget data, ensuring a nuanced understanding and facilitating informed decision-making in the realm of consumer electronics.

## Lessons Learned

How to parse web sites and analyze data


## 🚀 About Us
We are team of 5 students of Suleyman Demirel University

- Bekzat Makhanbet (211107030)

- Alibek Abdikassym (231107004) 

- Arman Kenessuly (231107005) 

- Saidakmal Oktamov (231103003)

- Darkhan Zhadyrayev (221107047)
- 
