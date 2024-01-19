from app import settings


def extract_uuid_from_short_url(short_url):
    host = settings.HOST
    # Check if the given short_url starts with the specified HOST
    if short_url.startswith(f'{host}/'):
        # Split the URL by '/' and get the last part as the UUID
        uuid = short_url.split('/')[-1]
        return uuid
    else:
        # Return None if the URL doesn't match the expected format
        return None
