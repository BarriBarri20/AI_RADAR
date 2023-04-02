# AI News Radar

This is a Django application that was created by Your Name for the AI_NIGHT_CHALLENGE competition. The application scrapes AI news from different websites asynchronously. The application uses **Selenium**, **Redis**, **MySQL**, **Scrapy**, and **Celery** to scrape news articles from various sources and store them in a database. The application is characterized by date and search, and it uses ***Tailwind CSS*** for styling.

### Installation

	$ git clone https://github.com/BarriBarri20/AI_RADAR.git
	$ cd ai-news-radar
	
	#install requirement
	$ pyenv install 
	$ pyenv shell
	
	# make the necessary migration
	$ python manage.py migrate
	
	# run the redis server
	$ redis-server
	
	#Start the Celery worker
	celery -A newsscraper worker --concurrency=4 --loglevel=info

	#start the django server
	$ python manage.py runserver

Now you can test it on :
http://localhost:8000
	
### Usage

The application automatically scrapes AI news from different websites every 20 seconds. You can also manually trigger the scraping process by clicking the "Scrape Now" button on the home page. The scraped news articles are displayed on the home page and are searchable by date and keyword.

With the ability to categorize fields by their unique HTML tags, you can easily scrape news articles from other websites and add them to the application. Additionally, it's possible to scrape from other websites as well. The key is to invest time in figuring out how to categorize the fields of each article based on their unique HTML tag. This will enable you to expand the scope of the application and provide a wider range of AI news to users.

You can click on the article to view the full article on the source website.

### Credits

This application was created by ***Lovelace team*** as a personal project for the AI_NIGHT_CHALLENGE competition. The AI news articles are scraped from dev.to.

