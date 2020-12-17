"""
    sample_search_results.py contains a sample search result which will be shown if in debug mode.
"""

sample_links = [
    'https://nodejs.org/',
    'https://github.com/nodejs/node',
    'https://nodejs.org/en/download/',
    'https://nodejs.dev/',
    'https://nodejs.org/en/about/',
]


sample_results = [
    {
        # 'title': 'Test Title {i}'.format(i=i),
        'link': link,
        # 'displayLink': 'testdisplaylink{i}.org/'.format(i=i),
    } for link in sample_links]

