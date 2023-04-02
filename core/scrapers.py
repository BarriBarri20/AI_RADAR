import datetime
from dateutil.relativedelta import relativedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from django.utils import timezone
from .models import NewsItem, ScrapeHistory
from webdriver_manager.chrome import ChromeDriverManager



def scrape(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument(" - icognito")
    options.add_argument("--disable-infobars")

    browser = webdriver.Chrome(
        ChromeDriverManager().install(), chrome_options=options)

    browser.get(url)

    timeout = 15

    try:
        WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located(
                (By.XPATH, 
                "//div[@class='substories search-results-loaded']")
            )
        )
    except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()


    try:

        article_elements = browser.find_elements(By.XPATH, 
            "//article[@class='crayons-story']"
        )

        # print(len(article_elements))


        for article in article_elements:
            # Find all the data by targetting parent div
            result = article.find_element(By.XPATH,
                ".//div[@role='presentation']"
            )
        
            # Find the title and link for article
            news_item_data = result.find_element(By.XPATH, ".//div[@class='crayons-story__indention']")
            news_item_anchor_tag = news_item_data.find_element(By.TAG_NAME, "a")
            
            
            news_item_link = news_item_anchor_tag.get_attribute("href")
            news_item_title = news_item_anchor_tag.text

            # Find the date and time

            timestamp_result = result.find_element(By.TAG_NAME, "time")
            news_item_time = timestamp_result.text

            # Removing (3 hours ago)
            if '(' in news_item_time:
                bracket_index = news_item_time.index('(')
                news_item_time = news_item_time[:(bracket_index-1)]
            else:
                pass

            # formatting news_item_time

        
            # Converting news_item_date into python date

            if "'" in news_item_time:
                # extract the date
                news_item_date = datetime.datetime.strptime(news_item_time, "%b %d '%y").date()
            else:
                # Extract current year
                news_item_date = datetime.datetime.strptime(news_item_time, "%b %d")
                today = datetime.date.today()
                news_item_date = news_item_date.replace(year=today.year).date()


            NewsItem.objects.get_or_create(
                source='dev.to',
                link = news_item_link,
                title = news_item_title,
                published_date = news_item_date
            )


            ScrapeHistory.objects.create(finished_time = timezone.now(), finished = True)

    except Exception as e:
        print ('type is:', e.__class__.__name__)