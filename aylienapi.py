from aylienapiclient import textapi
import aylien_news_api
from aylien_news_api.rest import ApiException

# Text API client initialization
textclient = textapi.Client('0cb57f68','3a4f6a2ec37e163270a03d36a366f414')
# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = ' 56704c5d'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '07bbab7a5042002d9746890051e1f27f'
# create an instance of the API class
newsclient = aylien_news_api.DefaultApi()


text = 'This is extremely bad'
sentiment = textclient.Sentiment(text)
print (sentiment)

opts = {
        'title': 'Apple',
        'body': 'Iphone',
        'sort_by': 'social_shares_count.facebook',
        'language': ['en'],
        'not_language': ['es', 'it'],
        'published_at_start': 'NOW-1MONTH',
        'published_at_end': 'NOW',
        'entities_body_links_dbpedia': [
        'http://dbpedia.org/resource/Donald_Trump',
        'http://dbpedia.org/resource/Hillary_Rodham_Clinton'
        ]
}
try:
        # List stories
        api_response = newsclient.list_stories(**opts)
        print("API called successfully. Returned data: ")
        print("========================================")
        for story in api_response.stories:
            print(story.title + " / " + story.source.name)
            print (story.published_at)
            print (story.sentiment.body)
            senti=textclient.Sentiment(story.body)
            print(senti['polarity'], senti['polarity_confidence'])
            print(senti['subjectivity'], senti['subjectivity_confidence'])
except ApiException as e:
        print("Exception when calling DefaultApi->list_stories: %s\n" % e)

# print (help(api_response.stories[0].source))
