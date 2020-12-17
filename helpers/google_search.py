"""
    google_search.py file consists of the helper functions to fetch the search results for a particular search term.
"""
from googleapiclient.discovery import build
from app_settings import debug
from helpers.sample_search_result import sample_results
from app_settings import (GOOGLE_API_KEY, GOOGLE_CSE_ID)


# Get google search response
def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']


# Parse the google search response to get result links
def fetch_google_results(search_term):
    if debug:
        return sample_results
    results = google_search(
        search_term, GOOGLE_API_KEY, GOOGLE_CSE_ID, num=5)
    return [{'title': i['title'], 'link': i['link'], 'displayLink': i['displayLink']} for i in results]
