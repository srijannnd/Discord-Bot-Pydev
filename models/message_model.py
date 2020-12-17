"""
    Message Model to create an appropriate response based on Authors message.
"""
from helpers.google_search import fetch_google_results
from db import (database, collection)
from datetime import datetime
import pymongo
from helpers.messages import (greet, greet_reply, google_wait_msg, recent_wait_msg, google_tag, recent_tag,
                              google_result_head, recent_result_head)


class Message:
    def __init__(self, msg_client, user):
        self.author = msg_client.author
        self.msg_text = msg_client.content.lower()
        self.msg_client = msg_client
        self.user = user

    # Send Response to Author
    async def send_response(self):
        msg_text = self.msg_text

        if self.author == self.user:
            return
        elif msg_text == greet:
            await self.greeting_response()
        elif msg_text.startswith(google_tag):
            await self.google_response()
        elif msg_text.startswith(recent_tag):
            await self.recent_search_response()

    # Send greeting response
    async def greeting_response(self):
        await self.msg_client.channel.send(greet_reply)

    # Send google search response
    async def google_response(self):
        msg_client = self.msg_client
        msg_text = self.msg_text
        search_term = msg_text[len(google_tag):].strip()
        await msg_client.channel.send(google_wait_msg)

        res = fetch_google_results(search_term)
        res_text = google_result_head.format(num=len(res)) + "\n".join(
            ["{counter}. {link}".format(counter=i + 1, link=elem['link']) for i, elem in enumerate(res)])
        self.save_search_request(search_term)
        await msg_client.channel.send(res_text)

    # Send recent search history response
    async def recent_search_response(self):
        msg_client = self.msg_client
        search_term = self.msg_text[len(recent_tag):].strip()
        await msg_client.channel.send(recent_wait_msg.format(term=search_term))

        res = self.get_recent_history(search_term)
        res_text = recent_result_head.format(num=len(res), term=search_term) + "\n".join(
            ["{counter}. {term}".format(counter=i + 1, term=doc['search_term']) for i, doc in enumerate(res)])
        await msg_client.channel.send(res_text)

    # Save Search Terms
    def save_search_request(self, search_term):
        database[collection].insert_one({'author_id': self.author.id, "search_term": search_term,
                                         'timestamp': datetime.now()})

    # Fetch Recent History wrt Search Term
    def get_recent_history(self, search_term):
        res = list(database[collection].find({'author_id': self.author.id, '$text': {'$search': search_term}},
                                             {"_id": 0, "search_term": 1}).sort(
            [("timestamp", pymongo.DESCENDING)]).limit(5))
        return res
