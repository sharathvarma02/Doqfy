# Nifty 50 Web Scraper

This web application scrapes the 'Nifty 50' table from Yahoo Finance every 5 minutes, stores the data in a Redis instance, and displays the values in a card layout. The application is built using a Python framework and includes background scraping.

## Features
- **Data Scraping:** Scrapes the 'Nifty 50' table from Yahoo Finance every 5 minutes.
- **Data Persistence:** Stores the scraped data in a Redis instance.
- **Card Layout Display:** Displays the data in a card layout on the web app.
- **Background Processing:** Scrapes data in the background on a different thread.
