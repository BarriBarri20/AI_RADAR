from celery import Celery
from celery import shared_task
from .scrapers import scrape

app = Celery('tasks', broker='redis://guest@localhost//')

url = 'https://dev.to/search?q=artificial%20intelligence'


@app.task
def scrap_dev_to():
    result = scrape(url)
    return


@shared_task
def scrape_async():
    scrape(url)
    return