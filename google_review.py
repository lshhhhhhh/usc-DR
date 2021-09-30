from google_play_scraper import Sort, reviews, app
import pandas as pd
#https://github.com/JoMingyu/google-play-scraper

app_packages = [
  'com.whatsapp'
]
app_reviews = []

# Loop through all the app packages and collect review for each of them
for ap in app_packages:
    for score in list(range(1, 6)):
        for sort_order in [Sort.MOST_RELEVANT, Sort.NEWEST]:
            rvs, _ = reviews(
                ap,
                lang='en',
                country='us',
                sort=sort_order,
                count=200,
                filter_score_with=score
            )
        for r in rvs:
            r['sortOrder'] = 'most_relevant' if sort_order == Sort.MOST_RELEVANT else 'newest'
            r['appId'] = ap

        app_reviews.extend(rvs)

app_reviews_df = pd.DataFrame(app_reviews)
app_reviews_df.to_csv('reviews.csv', index=None, header=True)