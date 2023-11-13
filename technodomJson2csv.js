import { createObjectCsvWriter } from "csv-writer";
import json from "./myjsonfile.json" assert { type: "json" };

const writer = createObjectCsvWriter({
  path: "./technomod.csv",
  header: [
    { id: "sku", title: "SKU" },
    { id: "title", title: "title" },
    { id: "price", title: "price" },
    { id: "price_usd", title: "price_usd" },
    { id: "old_price", title: "old_price" },
    { id: "discount", title: "discount" },
    { id: "type", title: "type" },
    { id: "brand", title: "brand" },
    { id: "brand_code", title: "brand_code" },
    { id: "rating", title: "rating" },
    { id: "reviews", title: "reviews" },
    { id: "cashback_amount", title: "cashback_amount" },
    { id: "categories", title: "categories" },
    { id: "credit_terms", title: "credit_terms" },
    { id: "color", title: "color" },
    { id: "showcase", title: "showcase" },
    { id: "short_description", title: "short_description" },
    { id: "delivery_info", title: "delivery_info" },
    { id: "variants", title: "variants" },
    { id: "is_new", title: "is_new" },
    { id: "categories_ru", title: "categories_ru" },
  ],
  fieldDelimiter: ";"
});

const records = [];

Object.values(json).map((i) =>
  i.data.map((j) =>
    records.push({
      ...j,
      color: JSON.stringify(j.color),
      short_description: JSON.stringify(j.short_description),
      delivery_info: JSON.stringify(j.delivery_info),
      variants: JSON.stringify(j.variants),
      categories_ru: JSON.stringify(j.categories_ru),
    })
  )
);

console.log(records);

writer
  .writeRecords(records) // returns a promise
  .then(() => {
    console.log("...Done");
  });
