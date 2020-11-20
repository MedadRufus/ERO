import json

import requests
from bs4 import BeautifulSoup

from json_parser import trip_advisor_page_from_dict, trip_advisor_page_to_dict

if __name__ == "__main__":

    conn = requests.get("https://www.tripadvisor.co.uk/Attractions-g294265-Activities-c26-Singapore.html#FILTERED_LIST")
    soup = BeautifulSoup(conn.text, 'html.parser')
    data = soup.find('script', type='application/ld+json').contents

    result = trip_advisor_page_from_dict(json.loads(data[0]))
    result_dict = trip_advisor_page_to_dict(result)

    for i in result.item_list_element:
        print(i.name, ":", "https://www.tripadvisor.co.uk"+i.url)

    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(result_dict)
