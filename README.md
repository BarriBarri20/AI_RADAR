AI News Radar
This is a Django application that was created by Your Name for the AI_NIGHT_CHALLENGE competition. The application scrapes AI news from different websites asynchronously. The application uses Selenium, Redis, MySQL, Scrapy, and Celery to scrape news articles from various sources and store them in a database. The application is characterized by date and search, and it uses Tailwind CSS for styling.

Requirements
Python 3.7 or higher
Django 3.2 or higher
Redis
MySQL
Scrapy
Celery
Selenium
Tailwind CSS
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/ai-news-radar.git
Install the dependencies:

bash
Copy code
cd ai-news-radar
pip install -r requirements.txt
Set up the database:

Copy code
python manage.py migrate
Start the Redis server:

Copy code
redis-server
Start the Celery worker:

css
Copy code
celery -A ai_news_radar worker --concurrency=4 --loglevel=info
Start the Django server:

Copy code
python manage.py runserver
Open your browser and go to http://localhost:8000 to view the application.

Usage
The application automatically scrapes AI news from different websites every 20 seconds. You can also manually trigger the scraping process by clicking the "Scrape Now" button on the home page. The scraped news articles are displayed on the home page and are searchable by date and keyword.

You can click on the "Read More" button for each news article to view the full article on the source website.

Credits
This application was created by Your Name as a personal project for the AI_NIGHT_CHALLENGE competition. The AI news articles are scraped from various sources using Scrapy and Selenium.

License
This project is licensed under the MIT License. See the LICENSE file for details.
