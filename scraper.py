import json
from json_parser import trip_advisor_page_from_dict,trip_advisor_page_to_dict
import pprint
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":

    conn = requests.get("https://www.tripadvisor.co.uk/Attractions-g294265-Activities-c26-Singapore.html#FILTERED_LIST")


    soup = BeautifulSoup(conn.text, 'html.parser')


    data = soup.find('script', type='application/ld+json').contents
    #print(data)
    pp = pprint.PrettyPrinter(indent=4)
    result = trip_advisor_page_from_dict(json.loads(data[0]))
    result_dict = trip_advisor_page_to_dict(result)

    for i in result.item_list_element:
        print(i.name,":",i.url)


    #pp.pprint(result_dict)