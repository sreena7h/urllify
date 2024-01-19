from app.utils.helpers import TextGen, ShortURL


def get_short_url():
    text_gen_obj = TextGen()
    short_url_obj = ShortURL(text_gen_obj)
    short_url = short_url_obj.generate()
    return short_url
