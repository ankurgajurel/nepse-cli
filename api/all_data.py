import json 
import requests

ALL_APIS = {
    'top_sectors': 'https://www.nepsealpha.com/trading-menu/top-stocks/',
    'live_nepse': 'https://www.nepsealpha.com/ajax/live-scan-nepse',
    'breaking_news': 'https://www.nepsealpha.com/api/smx9841/get_breaking_news',
    'scrip_data': 'https://merolagani.com/handlers/webrequesthandler.ashx?type=market_summary',
    'indices_data': 'https://www.nepsealpha.com/api/smx9841/dashboard_board',
    'list-companies': 'https://merolagani.com/handlers/AutoSuggestHandler.ashx?type=Company',
}

def send_req_basic(scrip: str) -> dict:
    """This is the basic send request function that will get the basic info of a company"""
    base_url = ALL_APIS['top_sectors']
    return json.loads(requests.get(base_url + scrip.upper(), timeout=10).text)

def send_req_nepse(command: str = "live") -> float:
    """
        This function will extract a dictinary with data related to nepse as a whole
    """

    base_url = ALL_APIS['live_nepse']
    live_data = json.loads(requests.get(base_url, timeout=10).text)

    corresponding_key = {
        'live': 'ltp',
        'percent_change': 'percent_change',
        'status': 'market_status'
    }

    try:
        return live_data[corresponding_key[command]]
    except Exception as get_exception:
        print(f"Please report this issue on our github repo along with this Error: {get_exception}")

def send_req_news() -> dict:
    """
        This send req will requests data for latest day's breaking news. 
        The news might be less in number because they are special ones.
    """

    base_url = ALL_APIS['breaking_news']
    return json.loads(requests.get(base_url, timeout=5).text)['breaking']
    
def send_req_scrip_data(scrip: str) -> tuple:
    """
        This function will request raw data for the price-related data of the company. We have used api from another website called merolagani.
    """
    base_url = ALL_APIS['scrip_data']
    all_scrip = json.loads(requests.get(base_url, timeout=5).text)["turnover"]["detail"]
    
    for each_scrip in all_scrip:
        if each_scrip["s"] == scrip.upper():
            return float(each_scrip["lp"]), float(each_scrip["pc"]), float(each_scrip["h"]), float(each_scrip["l"])

def send_req_top_stocks(rank: int, field: str) -> tuple:
    """
        This function will request raw data about top gainer or looser or turnover.
    """
    base_url = ALL_APIS['top_sectors']
    return json.loads(requests.get(base_url, timeout=5).text)['topStocks'][rank][field][0:2]

def send_req_indices(index: str) -> dict:
    """
        This function will request raw data about indices.
    """
    base_url = ALL_APIS['indices_data']
    data = json.loads(requests.get(base_url, timeout=10).text)

    for i in data['home_table']:
        if i['index_name'].lower() == index.lower():
            return i


def company_names() -> dict:
    """
        This function will return all company names.
    """
    base_url = ALL_APIS['list-companies']
    data = json.loads(requests.get(base_url, timeout=10).text)

    companies = []
    for i in data:
        companies.append(i['l'])

    return companies

