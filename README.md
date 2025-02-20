
- kyuceak-api-84f479b86a99.herokuapp.com/products/ --> get all products
- kyuceak-api-84f479b86a99.herokuapp.com/products/?popularity_score=0.51 --> get filter result for popularity score
- kyuceak-api-84f479b86a99.herokuapp.com/products/?price_range_min=400&price_range_max=500 --> get filter result for price range


# Product API

This project is a Django-based RESTful API that serves product data from a JSON file. It calculates dynamic pricing based on product attributes and real-time gold price data, and supports filtering by price range and popularity score.

## Features

- **RESTful Endpoints:** Serves product information with details such as name, popularity score, weight, and images.
- **Dynamic Price Calculation:**
  - **Formula:** Price = (popularityScore + 1) * weight * goldPrice
  - **Gold Price:** Retrieved in real-time from a chosen data source.
- **Filtering (Bonus):** Allows filtering of products based on:
  - Price range
  - Popularity score

## Requirements

- Python 3.x
- Django
- Django REST Framework
- Requests (or any HTTP client library) for fetching the real-time gold price
