from utilities.configurations import *


# Returns dictionary type
def add_book_payload(isbn, aisle):
    body = {

        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": aisle,
        "author": "John foe"
    }
    return body


# Returns dictionary type
def build_payload_from_db(query):
    body = {}
    tp = get_query(query)
    body['name'] = tp[0]
    body['isbn'] = tp[1]
    body['aisle'] = tp[2]
    body['author'] = tp[3]
    return body
