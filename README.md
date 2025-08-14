# 🛒 BestDeals – Product Price Comparison Website

BestDeals is a Django-based web app that compares product details like price, brand, description, and reviews from Amazon and Flipkart. Product data is stored in PostgreSQL and fetched through a search feature for quick, side-by-side comparison.

## Features
- Search bar to find products
- Price, brand, description, and reviews display
- Side-by-side comparison for Amazon & Flipkart
- Responsive design

## Tech Stack
- Django (Python)
- PostgreSQL
- HTML, CSS

## Running Locally
```bash
git clone https://github.com/safna925/bestdeals-django.git
cd bestdeals-django
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
