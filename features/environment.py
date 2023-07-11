import requests

from api.api_resources import *
from utilities.configurations import *


# This method will run after each scenario
def after_scenario(context, scenario):
    # Execute this step only for scenarios with @Library tag
    if "Library" in scenario.tags:
        url = get_config()['API']['endpoint'] + ApiResources.deleteBook
        headers = {"Content-Type": "application/json"}
        response = requests.post(url,
                                 json={
                                     "ID": context.book_id
                                 }, headers=headers, )

        assert response.status_code == 200
        res_json = response.json()
        print(res_json["msg"])
        assert res_json["msg"] == "book is successfully deleted"
