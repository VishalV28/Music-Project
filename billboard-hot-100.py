
    # for item in soup.select('div.o-chart-results-list-row-container'):
    #     rank_element = item.select_one('span.c-label.a-font-primary-bold-l.u-font-size-32@tablet.u-letter-spacing-0080@tablet')
    #     title_element = item.select_one('h3.c-title.a-no-trucate.a-font-primary-bold-s.u-letter-spacing-0021.u-font-size-23@tablet.lrv-u-font-size-16.u-line-height-125.u-line-height-normal@mobile-max.a-truncate-ellipsis.u-max-width-245.u-max-width-230@tablet-only.u-letter-spacing-0028@tablet')
    #     artist_element = item.select_one('span.c-label.a-no-trucate.a-font-primary-s.lrv-u-font-size-14@mobile-max.u-line-height-normal@mobile-max.u-letter-spacing-0021.lrv-u-display-block.a-truncate-ellipsis-2line.u-max-width-330.u-max-width-230@tablet-only.u-font-size-20@tablet')
#h3.c-title.a-no-truncate.a-font-primary-bold-s.u-letter-spacing-0021.lrv-u-font-size-16.u-line-height-125.a-truncate-ellipsis.u-max-width-245
#title_element = item.select_one('h3.c-title.a-no-trucate.a-font-primary-bold-s.u-letter-spacing-0021.lrv-u-font-size-16.u-line-height-125.a-truncate-ellipsis.u-max-width-245')

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape Billboard Hot 100
def scrape_billboard_hot_100():
    url = "https://www.billboard.com/charts/hot-100"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract relevant data
    data = []
    for item in soup.select('div.o-chart-results-list-row-container'):
        rank_element = item.select_one('span.c-label.a-font-primary-bold-l')
        #for item in soup.select('li.lrv-u-width-100p'):
        title_element = item.select_one('#title-of-a-story')
        artist_element = item.select_one('span.c-label.a-no-trucate.a-font-primary-s.u-letter-spacing-0021.lrv-u-display-block.a-truncate-ellipsis-2line.u-max-width-330')
        if rank_element and title_element and artist_element:
                rank = rank_element.text.strip()
                title = title_element.text.strip()
                artist = artist_element.text.strip()
                data.append([rank, title, artist])

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=['Rank', 'Title', 'Artist'])
    return df

# Scrape the data
billboard_hot_100_df = scrape_billboard_hot_100()
print(billboard_hot_100_df.head())

