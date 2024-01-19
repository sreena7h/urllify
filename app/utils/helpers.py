import hashlib
import random
import string

from app.collections.identifier import collection
from app.utils.interfaces import ITextGen, IShortURL
from app.settings import HOST

import threading


lock = threading.Lock()


class TextGen(ITextGen):
    length = 5

    def generate_unique_string(self):
        while True:
            characters = string.ascii_letters + string.digits
            identifier = ''.join(random.choice(characters)
                                 for _ in range(self.length))

            while lock:
                if not collection.find_one({"uuid": identifier}):
                    # Insert the short identifier into MongoDB
                    collection.insert_one({"uuid": identifier})
                    return identifier


class ShortURL(IShortURL):

    def __init__(self, text_gen_obj):
        self.text_gen_obj = text_gen_obj

    def generate(self):
        uuid = self.text_gen_obj.generate_unique_string()
        return f'{HOST}/{uuid}'

